from app.agents.base_agent import BaseAgent
from app.services.llm_service import GroqService
from app.retriever.retrieval_service import RetrievalService
from app.prompts.agent_prompts import REGULATORY_AGENT_PROMPT


class RegulatoryAgent(BaseAgent):
    def __init__(self, llm_service: GroqService, retrieval_service: RetrievalService):
        super().__init__(
            name="regulatory_agent",
            llm_service=llm_service,
            retrieval_service=retrieval_service,
            system_prompt=REGULATORY_AGENT_PROMPT,
            knowledge_domains=[
                "regulations",
                "FDA_recalls",
                "warning_letters",
            ],
        )
