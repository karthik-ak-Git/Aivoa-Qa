import json
from langgraph.graph import StateGraph, END
from app.graph.state import CopilotState
from app.agents.medicine_agent import MedicineAgent
from app.agents.complaint_agent import ComplaintAgent
from app.agents.root_cause_agent import RootCauseAgent
from app.agents.capa_agent import CAPAAgent
from app.agents.regulatory_agent import RegulatoryAgent
from app.agents.summary_agent import SummaryAgent
from app.services.validation_service import ResponseValidationService
from app.core.logger import get_logger

logger = get_logger("graph.workflow")


class CopilotWorkflow:
    """LangGraph workflow for the AI copilot."""

    def __init__(
        self,
        medicine_agent: MedicineAgent,
        complaint_agent: ComplaintAgent,
        root_cause_agent: RootCauseAgent,
        capa_agent: CAPAAgent,
        regulatory_agent: RegulatoryAgent,
        summary_agent: SummaryAgent,
        validation_service: ResponseValidationService,
        retrieval_service=None,
    ):
        self.agents = {
            "medicine": medicine_agent,
            "complaint": complaint_agent,
            "root_cause": root_cause_agent,
            "capa": capa_agent,
            "regulatory": regulatory_agent,
            "summary": summary_agent,
        }
        self.validation_service = validation_service
        self._retrieval_service = retrieval_service
        self.graph = self._build_graph()

    def _build_graph(self) -> StateGraph:
        graph = StateGraph(CopilotState)

        graph.add_node("detect_intent", self._detect_intent)
        graph.add_node("retrieve_knowledge", self._retrieve_knowledge)
        graph.add_node("select_agent", self._select_agent)
        graph.add_node("generate_response", self._generate_response)
        graph.add_node("validate_response", self._validate_response)

        graph.set_entry_point("detect_intent")
        graph.add_edge("detect_intent", "retrieve_knowledge")
        graph.add_edge("retrieve_knowledge", "select_agent")
        graph.add_edge("select_agent", "generate_response")
        graph.add_edge("generate_response", "validate_response")
        graph.add_edge("validate_response", END)

        return graph.compile()

    async def _detect_intent(self, state: CopilotState) -> CopilotState:
        message = state["message"].lower()
        intent = "general"

        medicine_keywords = [
            "drug", "tablet", "capsule", "dosage", "formulation", "api",
            "active ingredient", "excipient", "dissolution", "stability",
        ]
        complaint_keywords = [
            "complaint", "defect", "damage", "broken", "contamination",
            "foreign matter", "wrong product", "label", "packaging defect",
        ]
        root_cause_keywords = [
            "root cause", "investigation", "why did", "cause of",
            "analysis", "fishbone", "ishikawa", "5 why", "6m",
        ]
        capa_keywords = [
            "capa", "corrective", "preventive", "action plan",
            "recurrence", "effectiveness", "corrective action",
        ]
        regulatory_keywords = [
            "fda", "regulation", "21 cfr", "ich", "eu gmp", "who",
            "compliance", "warning letter", "recall", "guideline",
        ]
        summary_keywords = [
            "summary", "summarize", "overview", "report", "trend",
        ]

        for kw in medicine_keywords:
            if kw in message:
                intent = "medicine"
                break
        if intent == "general":
            for kw in complaint_keywords:
                if kw in message:
                    intent = "complaint"
                    break
        if intent == "general":
            for kw in root_cause_keywords:
                if kw in message:
                    intent = "root_cause"
                    break
        if intent == "general":
            for kw in capa_keywords:
                if kw in message:
                    intent = "capa"
                    break
        if intent == "general":
            for kw in regulatory_keywords:
                if kw in message:
                    intent = "regulatory"
                    break
        if intent == "general":
            for kw in summary_keywords:
                if kw in message:
                    intent = "summary"
                    break

        logger.info(f"Intent detected: {intent} for message: '{state['message'][:60]}...'")
        return {**state, "intent": intent}

    async def _retrieve_knowledge(self, state: CopilotState) -> CopilotState:
        intent = state["intent"]
        message = state["message"]

        domain_map = {
            "medicine": ["medicines", "dosage_forms", "pharmaceutical_dictionary"],
            "complaint": ["complaint_terms", "complaint_categories", "complaint_examples"],
            "root_cause": ["root_cause_library", "investigations", "deviations"],
            "capa": ["CAPA", "root_cause_library", "regulations"],
            "regulatory": ["regulations", "FDA_recalls", "warning_letters"],
            "summary": ["complaint_terms", "complaint_categories", "root_cause_library", "CAPA"],
            "general": [],
        }

        domains = domain_map.get(intent, [])
        docs = []
        if self._retrieval_service:
            docs = self._retrieval_service.retrieve_for_agent(
                query=message, agent_domains=domains, n_results=5
            )

        logger.info(f"Retrieved {len(docs)} documents for intent: {intent}")
        return {**state, "retrieved_docs": docs}

    async def _select_agent(self, state: CopilotState) -> CopilotState:
        agent_map = {
            "medicine": "medicine",
            "complaint": "complaint",
            "root_cause": "root_cause",
            "capa": "capa",
            "regulatory": "regulatory",
            "summary": "summary",
            "general": "complaint",
        }
        agent_key = agent_map.get(state["intent"], "complaint")
        agent = self.agents.get(agent_key)
        if agent:
            return {**state, "agent_used": agent.name}
        return {**state, "agent_used": "complaint_agent"}

    async def _generate_response(self, state: CopilotState) -> CopilotState:
        agent_name = state.get("agent_used", "complaint_agent")
        agent_key = agent_name.replace("_agent", "").replace("_", "")
        agent = self.agents.get(agent_key) or self.agents.get("complaint")

        if not agent:
            return {
                **state,
                "response": "Unable to process the request. Please try again.",
                "citations": [],
                "sources": [],
                "confidence": 0.0,
            }

        result = await agent.run(
            query=state["message"],
            conversation_history=state.get("conversation_history"),
        )
        return {
            **state,
            "response": result["response"],
            "citations": result["citations"],
            "sources": result["sources"],
            "confidence": result["confidence"],
        }

    async def _validate_response(self, state: CopilotState) -> CopilotState:
        validation = self.validation_service.validate(
            response=state["response"],
            citations=state["citations"],
            confidence=state["confidence"],
        )
        return {
            **state,
            "validation_result": validation,
            "confidence": validation["adjusted_confidence"],
        }

    async def run(self, initial_state: dict) -> dict:
        result = await self.graph.ainvoke(initial_state)
        return dict(result)
