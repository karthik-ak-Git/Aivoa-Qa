"""Complaint Editor Agent — edits/refines existing complaint forms based on user feedback."""
import json
from app.services.groq_service import GroqService
from app.retriever.retrieval_service import RetrievalService
from app.core.logger import get_logger

logger = get_logger("agents.editor")

EDITOR_SYSTEM_PROMPT = """You are an expert Pharmaceutical Complaint Editor for an FDA-regulated drug manufacturer.

Your job: Given the CURRENT complaint form data AND a user's edit instruction, update ONLY the fields the user requests while keeping the rest intact.

You MUST return ONLY a valid JSON object with EXACTLY these fields (no markdown, no extra text):

{
  "status": "string - complaint status",
  "complaintSource": "string",
  "customerName": "string",
  "productName": "string - full product name with strength and dosage form",
  "productStrength": "string",
  "batchNumber": "string",
  "manufacturingDate": "string - YYYY-MM-DD or empty",
  "expiryDate": "string - YYYY-MM-DD or empty",
  "quantityAffected": "string",
  "quantityUnit": "string",
  "complaintType": "string",
  "complaintDate": "string - YYYY-MM-DD",
  "detailedDescription": "string",
  "suggestedSeverity": "Critical or Major or Minor",
  "suggestedNextAction": "string",
  "riskAssessment": "string"
}

RULES:
1. Apply ONLY the changes the user requested
2. Keep ALL other fields exactly as they were in the current form
3. If user says "change severity to Critical", ONLY change suggestedSeverity
4. If user says "update the description", ONLY change detailedDescription
5. If user says "change the product name to Paracetamol 500mg", update productName AND productStrength
6. Return ONLY the complete JSON object (all fields), not just the changed ones
7. Use the RAG knowledge context to validate pharmaceutical terminology when editing
8. Return ONLY the JSON object, nothing else"""


class EditorAgent:
    """Edits existing complaint forms based on user instructions using Groq + RAG."""

    name = "complaint_editor"

    def __init__(self, groq: GroqService, retrieval: RetrievalService):
        self.groq = groq
        self.retrieval = retrieval

    async def run(self, instruction: str, current_form: dict) -> dict:
        # Step 1: RAG retrieval for edit context
        combined_query = f"{instruction} {current_form.get('productName', '')} {current_form.get('complaintType', '')}"
        rag_docs = self.retrieval.retrieve_for_agent(
            query=combined_query,
            agent_domains=[
                "complaint_terms", "complaint_categories",
                "medicines", "dosage_forms", "packaging",
                "regulations",
            ],
            n_results=5,
        )

        rag_context = ""
        if rag_docs:
            rag_context = "\n\nRELEVANT KNOWLEDGE BASE CONTEXT:\n"
            for i, doc in enumerate(rag_docs[:3], 1):
                rag_context += f"\n[{i}] Source: {doc.get('source', 'unknown')}\n"
                rag_context += f"Content: {doc['content'][:400]}\n"

        # Step 2: Build prompt
        user_msg = f"""CURRENT COMPLAINT FORM:
{json.dumps(current_form, indent=2)}

USER EDIT INSTRUCTION:
{instruction}

Apply the user's edit to the form above. Return the COMPLETE updated form as JSON."""

        if rag_context:
            user_msg += rag_context

        messages = [
            {"role": "system", "content": EDITOR_SYSTEM_PROMPT},
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
            form_data = json.loads(clean)
        except (json.JSONDecodeError, IndexError):
            logger.error(f"Failed to parse editor output: {response[:300]}")
            # Return current form unchanged
            form_data = current_form.copy()

        # Ensure all required fields exist (merge with current form)
        for key in current_form:
            if key not in form_data:
                form_data[key] = current_form[key]

        logger.info(
            f"Editor agent applied edits: product={form_data.get('productName', 'N/A')}, "
            f"severity={form_data.get('suggestedSeverity', 'N/A')}"
        )

        return {
            "form_data": form_data,
            "confidence": 0.9,
            "sources_used": [d.get("source", "") for d in rag_docs[:3]],
        }
