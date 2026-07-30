"""OCR Extraction Agent — extracts complaint data from uploaded documents."""

import json
import re
from app.services.groq_service import GroqService
from app.retriever.retrieval_service import RetrievalService
from app.core.logger import get_logger

logger = get_logger("agents.ocr")

OCR_SYSTEM_PROMPT = """You are a Pharmaceutical Complaint Data Extractor for an FDA-regulated drug manufacturer.

Given document text, extract ALL available complaint form fields. Return ONLY a valid JSON object.

EXAMPLES:

Input: "Dear Sir, We received a complaint from ABC Pharma about Metformin 500mg tablets batch MT-23145. The tablets show discoloration. Received via email on 2026-03-15."
Output:
{
  "complaintSource": "Email Intake",
  "customerName": "ABC Pharma",
  "productName": "Metformin 500mg Tablets",
  "productStrength": "500mg",
  "batchNumber": "MT-23145",
  "manufacturingDate": "",
  "expiryDate": "",
  "quantityAffected": "",
  "quantityUnit": "tablets",
  "complaintType": "Discoloration in tablets",
  "complaintDate": "2026-03-15",
  "detailedDescription": "ABC Pharma reported discoloration found in Metformin 500mg tablets from batch MT-23145. The affected tablets show visible color change indicating possible degradation or contamination.",
  "suggestedSeverity": "Major",
  "suggestedNextAction": "Quarantine batch and initiate laboratory investigation",
  "riskAssessment": "Product quality defect affecting appearance; no immediate patient safety risk reported but requires investigation per ICH Q9"
}

Input: "URGENT: Patient reported burning sensation after using Hand Sanitizer Gel 70% batch HS-8872. Report from hospital pharmacy."
Output:
{
  "complaintSource": "Field Report",
  "customerName": "Hospital Pharmacy",
  "productName": "Hand Sanitizer Gel 70%",
  "productStrength": "70%",
  "batchNumber": "HS-8872",
  "manufacturingDate": "",
  "expiryDate": "",
  "quantityAffected": "1",
  "quantityUnit": "bottles",
  "complaintType": "Adverse skin reaction to hand sanitizer",
  "complaintDate": "",
  "detailedDescription": "A patient reported a burning sensation after using Hand Sanitizer Gel 70% batch HS-8872. The report was filed by the hospital pharmacy. The complaint suggests a potential adverse reaction requiring immediate safety evaluation.",
  "suggestedSeverity": "Critical",
  "suggestedNextAction": "Immediate batch recall assessment and safety evaluation",
  "riskAssessment": "Patient safety concern - adverse reaction reported. Critical severity per ICH Q9 risk management principles. Immediate investigation required."
}

RULES:
1. Extract EVERY piece of relevant information from the document text
2. If a field is not found, leave as empty string
3. detailedDescription: synthesize a clear complaint narrative from the document content (minimum 30 words)
4. Severity: patient safety risk = Critical, product quality = Major, cosmetic/minor = Minor
5. complaintSource: email = "Email Intake", letter/report = "Customer Portal", field/hospital = "Field Report"
6. Return ONLY valid JSON — no markdown, no code fences, no explanation text"""


class OCRextractionAgent:
    """Extracts complaint data from uploaded documents using LLM."""

    name = "ocr_extraction"

    def __init__(self, groq: GroqService, retrieval: RetrievalService):
        self.groq = groq
        self.retrieval = retrieval

    async def run(self, document_text: str, filename: str = "unknown") -> dict:
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
                rag_context += f"\n[{i}] {doc.get('source', '')}: {doc['content'][:500]}\n"

        user_msg = f"""DOCUMENT FILENAME: {filename}

DOCUMENT TEXT:
{document_text[:5000]}

Extract complaint form fields from this document and return as JSON."""
        if rag_context:
            user_msg += rag_context

        messages = [
            {"role": "system", "content": OCR_SYSTEM_PROMPT},
            {"role": "user", "content": user_msg},
        ]

        response = await self.groq.agenerate(messages, temperature=0.1, max_tokens=2048)

        result = self._parse_response(response, document_text)

        logger.info(
            f"OCR agent extracted: product={result.get('productName', 'N/A')}, "
            f"source={result.get('complaintSource', 'N/A')}, "
            f"batch={result.get('batchNumber', 'N/A')}"
        )

        confidence = 0.8
        completed = sum(1 for v in result.values() if isinstance(v, str) and len(v) > 2)
        total = sum(1 for v in result.values() if isinstance(v, str))
        if total > 0:
            confidence = round(0.4 + 0.5 * (completed / total), 2)

        return {
            "form_data": result,
            "confidence": min(confidence, 0.95),
            "sources_used": [d.get("source", "") for d in rag_docs[:3]],
        }

    def _parse_response(self, response: str, fallback_text: str) -> dict:
        clean = response.strip()
        match = re.search(r"\{.*\}", clean, re.DOTALL)
        if match:
            clean = match.group()
        else:
            logger.error(f"No JSON found in OCR output: {clean[:200]}")
            return self._defaults(fallback_text)

        try:
            result = json.loads(clean)
        except json.JSONDecodeError:
            logger.error(f"Failed to parse OCR JSON: {clean[:300]}")
            return self._defaults(fallback_text)

        defaults = self._defaults("")
        for field in defaults:
            if field not in result or not result.get(field):
                result[field] = defaults[field]

        if "extracted_fields" not in result or not isinstance(result["extracted_fields"], dict):
            result["extracted_fields"] = {
                "document_type": "unknown",
                "date_received": "",
                "contact_info": "",
                "key_claims": [],
                "evidence_references": [],
            }
        if not result.get("detailedDescription") and fallback_text:
            result["detailedDescription"] = fallback_text[:2000]

        return result

    def _defaults(self, fallback_text: str = "") -> dict:
        return {
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
            "detailedDescription": fallback_text[:2000] if fallback_text else "",
            "suggestedSeverity": "Major",
            "suggestedNextAction": "Route to QA Investigation",
            "riskAssessment": "",
            "extracted_fields": {
                "document_type": "unknown",
                "date_received": "",
                "contact_info": "",
                "key_claims": [],
                "evidence_references": [],
            },
        }
