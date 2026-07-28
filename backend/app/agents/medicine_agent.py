from app.agents.base_agent import BaseAgent
from app.services.llm_service import GroqService
from app.retriever.retrieval_service import RetrievalService
from app.prompts.agent_prompts import MEDICINE_AGENT_PROMPT


class MedicineAgent(BaseAgent):
    def __init__(self, llm_service: GroqService, retrieval_service: RetrievalService):
        super().__init__(
            name="medicine_agent",
            llm_service=llm_service,
            retrieval_service=retrieval_service,
            system_prompt=MEDICINE_AGENT_PROMPT,
            knowledge_domains=[
                "medicines",
                "dosage_forms",
                "pharmaceutical_dictionary",
            ],
        )
