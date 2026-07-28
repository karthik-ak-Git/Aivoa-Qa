from app.agents.base_agent import BaseAgent
from app.services.llm_service import GroqService
from app.retriever.retrieval_service import RetrievalService
from app.prompts.agent_prompts import CAPA_AGENT_PROMPT


class CAPAAgent(BaseAgent):
    def __init__(self, llm_service: GroqService, retrieval_service: RetrievalService):
        super().__init__(
            name="capa_agent",
            llm_service=llm_service,
            retrieval_service=retrieval_service,
            system_prompt=CAPA_AGENT_PROMPT,
            knowledge_domains=[
                "CAPA",
                "root_cause_library",
                "regulations",
            ],
        )
