"""OCR Extraction Agent — extracts complaint data from uploaded documents (PDF/text/image)."""
import json
from app.services.groq_service import GroqService
from app.retriever.retrieval_service import RetrievalService
from app.core.logger import get_logger

logger = get_logger("agents.ocr")

OCR_SYSTEM_PROMPT = """You are an expert Pharmaceutical Complaint Data Extractor for an FDA-regulated drug manufacturer.

Your job: Given extracted text from a document (complaint letter, email, report, CAPA, deviation), extract ALL available complaint form fields.

You MUST return ONLY a valid JSON object with EXACTLY these fields (no markdown, no extra text):

{
  "status": "Pending Triage",
  "complaintSource": "string - infer from document type (email=Email Intake, letter=Customer Portal, report=Field Report)",
  "customerName": "string - company or person who filed the complaint",
  "productName": "string - full product name with strength and dosage form",
  "productStrength": "string - strength and packaging",
  "batchNumber": "string - batch/lot number",
  "manufacturingDate": "string - YYYY-MM-DD or empty",
  "expiryDate": "string - YYYY-MM-DD or empty",
  "quantityAffected": "string - quantity affected",
  "quantityUnit": "string - unit (kg, tablets, capsules, vials, strips, packs)",
  "complaintType": "string - specific defect/description",
  "complaintDate": "string - YYYY-MM-DD",
  "detailedDescription": "string - comprehensive description (minimum 50 words)",
  "suggestedSeverity": "Critical or Major or Minor",
  "suggestedNextAction": "string - recommended immediate action",
  "riskAssessment": "string - risk assessment referencing ICH Q9",
  "extracted_fields": {
    "document_type": "string - type of document (email, letter, report, form)",
    "date_received": "string - when the document was received",
    "contact_info": "string - any contact information found",
    "key_claims": "array of strings - main complaint claims",
    "evidence_references": "array of strings - any referenced batch numbers, dates, etc."
  }
}

RULES:
1. Extract EVERY piece of relevant information from the document text
2. If a field is not found in the document, leave it as an empty string (except status which defaults to "Pending Triage")
3. For detailedDescription: synthesize the complaint narrative from the document content
4. Severity assessment based on: patient safety risk = Critical, product quality = Major, cosmetic = Minor
5. Infer complaintSource from the document format (email header → Email Intake, etc.)
6. Return ONLY the JSON object, nothing else"""


class OCRextractionAgent:
    """Extracts complaint data from uploaded documents using Groq + RAG."""

    name = "ocr_extraction"

    def __init__(self, groq: GroqService, retrieval: RetrievalService):
        self.groq = groq
        self.retrieval = retrieval

    async def run(self, document_text: str, filename: str = "unknown") -> dict:
        # Step 1: RAG retrieval for pharmaceutical context
        rag_docs = self.retrieval.retrieve_for_agent(
            query=document_text[:500],
            agent_domains=[
                "complaint_terms", "complaint_categories", "complaint_examples",
                "medicines", "manufacturing", "packaging",
                "root_cause_library", "regulations",
            ],
            n_results=5,
        )

        rag_context = ""
        if rag_docs:
            rag_context = "\n\nRELEVANT PHARMACEUTICAL KNOWLEDGE:\n"
            for i, doc in enumerate(rag_docs[:3], 1):
                rag_context += f"\n[{i}] {doc.get('source', '')}: {doc['content'][:400]}\n"

        # Step 2: Build prompt
        user_msg = f"""Extract complaint data from this document:

DOCUMENT FILENAME: {filename}

DOCUMENT TEXT:
{document_text[:4000]}

Extract all complaint form fields from this document and return as JSON."""

        if rag_context:
            user_msg += rag_context

        messages = [
            {"role": "system", "content": OCR_SYSTEM_PROMPT},
            {"role": "user", "content": user_msg},
        ]

        # Step 3: Generate
        response = await self.groq.agenerate(messages, temperature=0.2, max_tokens=2048)

        # Step 4: Parse
        try:
            clean = response.strip()
            if clean.startswith("```"):
                clean = clean.split("\n", 1)[1]
            if clean.endswith("```"):
                clean = clean.rsplit("```", 1)[0]
            clean = clean.strip()
            result = json.loads(clean)
        except (json.JSONDecodeError, IndexError):
            logger.error(f"Failed to parse OCR output: {response[:300]}")
            result = {
                "status": "Pending Triage",
                "complaintSource": "Document Upload",
                "customerName": "",
                "productName": "",
                "productStrength": "",
                "batchNumber": "",
                "manufacturingDate": "",
                "expiryDate": "",
                "quantityAffected": "",
                "quantityUnit": "units",
                "complaintType": "Document Upload",
                "complaintDate": "",
                "detailedDescription": document_text[:2000],
                "suggestedSeverity": "Major",
                "suggestedNextAction": "Route to QA Investigation",
                "riskAssessment": "Requires investigation per ICH Q9 framework",
                "extracted_fields": {
                    "document_type": "unknown",
                    "date_received": "",
                    "contact_info": "",
                    "key_claims": [],
                    "evidence_references": [],
                },
            }

        # Ensure required fields
        defaults = {
            "status": "Pending Triage",
            "complaintSource": "Document Upload",
            "customerName": "",
            "productName": "",
            "productStrength": "",
            "batchNumber": "",
            "manufacturingDate": "",
            "expiryDate": "",
            "quantityAffected": "",
            "quantityUnit": "units",
            "complaintType": "",
            "complaintDate": "",
            "detailedDescription": "",
            "suggestedSeverity": "Major",
            "suggestedNextAction": "Route to QA Investigation",
            "riskAssessment": "",
        }
        for field, default in defaults.items():
            if field not in result or not result[field]:
                result[field] = default

        # Ensure extracted_fields dict exists
        if "extracted_fields" not in result:
            result["extracted_fields"] = {}

        logger.info(
            f"OCR agent extracted: product={result.get('productName', 'N/A')}, "
            f"source={result.get('complaintSource', 'N/A')}"
        )

        return {
            "form_data": result,
            "confidence": 0.8,
            "sources_used": [d.get("source", "") for d in rag_docs[:3]],
        }
