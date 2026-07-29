"""Complaint Writer Agent — generates complaint form fields from natural language using RAG."""
import json
from app.services.groq_service import GroqService
from app.retriever.retrieval_service import RetrievalService
from app.core.logger import get_logger

logger = get_logger("agents.writer")

WRITER_SYSTEM_PROMPT = """You are an expert Pharmaceutical Complaint Writer for an FDA-regulated drug manufacturer.

Your job: Given a user's description of a complaint, generate a COMPLETE pharmaceutical complaint form.

You MUST return ONLY a valid JSON object with EXACTLY these fields (no markdown, no extra text):

{
  "status": "Pending Triage",
  "complaintSource": "string - where the complaint came from (Email Intake, Phone Call, Customer Portal, Field Report, Regulatory Notification, Internal Audit)",
  "customerName": "string - name of the customer or reporter",
  "productName": "string - full product name with strength and dosage form",
  "productStrength": "string - strength and packaging (e.g. 500mg Alu-Alu Blister)",
  "batchNumber": "string - batch/lot number",
  "manufacturingDate": "string - YYYY-MM-DD format or empty",
  "expiryDate": "string - YYYY-MM-DD format or empty",
  "quantityAffected": "string - numeric quantity affected",
  "quantityUnit": "string - unit (kg, tablets, capsules, vials, strips, packs)",
  "complaintType": "string - specific defect/description type",
  "complaintDate": "string - YYYY-MM-DD format, today if unknown",
  "detailedDescription": "string - comprehensive complaint description (minimum 50 words)",
  "suggestedSeverity": "Critical or Major or Minor",
  "suggestedNextAction": "string - recommended immediate action",
  "riskAssessment": "string - risk assessment referencing ICH Q9 and pharmaceutical impact"
}

RULES:
1. Use the RAG knowledge context to make the complaint scientifically accurate
2. Reference specific pharmaceutical terminology from the knowledge base
3. If the user doesn't provide a field, use intelligent defaults based on context
4. Risk assessment MUST reference relevant ICH Q9 principles when applicable
5. Severity: Critical = patient safety risk, Major = product quality failure, Minor = cosmetic/labeling
6. Return ONLY the JSON object, nothing else"""


class WriterAgent:
    """Generates complaint form fields from user descriptions using Groq + RAG."""

    name = "complaint_writer"

    def __init__(self, groq: GroqService, retrieval: RetrievalService):
        self.groq = groq
        self.retrieval = retrieval

    async def run(self, query: str, current_form: dict | None = None) -> dict:
        # Step 1: RAG retrieval
        rag_docs = self.retrieval.retrieve_for_agent(
            query=query,
            agent_domains=[
                "complaint_terms", "complaint_categories", "complaint_examples",
                "medicines", "dosage_forms", "manufacturing", "packaging",
                "root_cause_library", "regulations",
            ],
            n_results=8,
        )

        rag_context = ""
        if rag_docs:
            rag_context = "\n\nRELEVANT KNOWLEDGE BASE CONTEXT:\n"
            for i, doc in enumerate(rag_docs[:5], 1):
                rag_context += f"\n[{i}] Source: {doc.get('source', 'unknown')} (domain: {doc.get('domain', 'unknown')})\n"
                rag_context += f"Content: {doc['content'][:500]}\n"

        # Step 2: Build prompt
        user_msg = f"Create a pharmaceutical complaint from this description:\n\n{query}"

        if current_form:
            existing = {k: v for k, v in current_form.items() if v and k not in ("id", "createdAt")}
            if existing:
                user_msg += f"\n\nEXISTING FORM DATA (use as reference, improve where possible):\n{json.dumps(existing, indent=2)}"

        if rag_context:
            user_msg += rag_context

        messages = [
            {"role": "system", "content": WRITER_SYSTEM_PROMPT},
            {"role": "user", "content": user_msg},
        ]

        # Step 3: Generate
        response = await self.groq.agenerate(messages, temperature=0.3, max_tokens=4096)

        # Step 4: Parse
        def extract_json(raw: str) -> dict | None:
            raw = raw.strip()
            # Strip markdown fences: ```json ... ``` or ``` ... ```
            if raw.startswith("```"):
                for prefix in ("```json\n", "```json\n", "```\n", "```"):
                    if raw.startswith(prefix):
                        raw = raw[len(prefix):]
                        break
            if raw.endswith("```"):
                raw = raw[:-3]
            raw = raw.strip()
            try:
                return json.loads(raw)
            except json.JSONDecodeError:
                # Try to find the JSON object with regex
                import re
                match = re.search(r'\{.*"suggestedSeverity"\s*:\s*"[^"]*"[^}]*\}', raw, re.DOTALL)
                if match:
                    try:
                        return json.loads(match.group())
                    except json.JSONDecodeError:
                        pass
                # Last resort: try to find any JSON object
                brace_start = raw.find('{')
                brace_end = raw.rfind('}')
                if brace_start != -1 and brace_end != -1 and brace_end > brace_start:
                    try:
                        partial = raw[brace_start:brace_end + 1]
                        return json.loads(partial)
                    except json.JSONDecodeError:
                        pass
            return None

        form_data = extract_json(response)
        if form_data is None:
            logger.error(f"Failed to parse writer output: {response[:300]}")
            # Return a minimal valid form
            form_data = {
                "status": "Pending Triage",
                "complaintSource": "Email Intake",
                "customerName": "Unknown",
                "productName": "Unknown",
                "productStrength": "",
                "batchNumber": "",
                "manufacturingDate": "",
                "expiryDate": "",
                "quantityAffected": "",
                "quantityUnit": "units",
                "complaintType": "General Complaint",
                "complaintDate": "",
                "detailedDescription": query,
                "suggestedSeverity": "Major",
                "suggestedNextAction": "Route to QA Investigation",
                "riskAssessment": "Requires investigation per ICH Q9 framework",
            }

        # Ensure all required fields exist
        defaults = {
            "status": "Pending Triage",
            "complaintSource": "Email Intake",
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
            if field not in form_data or not form_data[field]:
                form_data[field] = default

        logger.info(
            f"Writer agent produced form: product={form_data.get('productName', 'N/A')}, "
            f"severity={form_data.get('suggestedSeverity', 'N/A')}"
        )

        return {
            "form_data": form_data,
            "confidence": 0.85,
            "sources_used": [d.get("source", "") for d in rag_docs[:5]],
        }
