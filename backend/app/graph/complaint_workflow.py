"""LangGraph Complaint Workflow — orchestrates Writer, Editor, and OCR agents."""
from typing import TypedDict, Annotated, Any
from operator import add
from langgraph.graph import StateGraph, END

from app.services.groq_service import GroqService
from app.retriever.retrieval_service import RetrievalService
from app.agents.writer_agent import WriterAgent
from app.agents.editor_agent import EditorAgent
from app.agents.ocr_agent import OCRextractionAgent
from app.core.logger import get_logger

logger = get_logger("graph.complaint_workflow")


class ComplaintState(TypedDict):
    """State for the complaint workflow graph."""
    mode: str  # "write" | "edit" | "ocr"
    query: str  # user message / instruction / document text
    filename: str  # for OCR mode
    current_form: dict | None  # for edit mode
    form_data: dict | None  # output form
    confidence: float
    sources_used: list[str]
    agent_used: str
    errors: Annotated[list[str], add]


class ComplaintWorkflow:
    """LangGraph workflow for complaint creation, editing, and extraction."""

    def __init__(self, groq: GroqService, retrieval: RetrievalService):
        self.writer = WriterAgent(groq, retrieval)
        self.editor = EditorAgent(groq, retrieval)
        self.ocr = OCRextractionAgent(groq, retrieval)
        self.graph = self._build_graph()

    def _build_graph(self) -> StateGraph:
        graph = StateGraph(ComplaintState)

        graph.add_node("route_mode", self._route_mode)
        graph.add_node("run_writer", self._run_writer)
        graph.add_node("run_editor", self._run_editor)
        graph.add_node("run_ocr", self._run_ocr)

        graph.set_entry_point("route_mode")

        def route(state: ComplaintState) -> str:
            mode = state.get("mode", "write")
            if mode == "edit":
                return "run_editor"
            elif mode == "ocr":
                return "run_ocr"
            else:
                return "run_writer"

        graph.add_conditional_edges(
            "route_mode",
            route,
            {
                "run_writer": "run_writer",
                "run_editor": "run_editor",
                "run_ocr": "run_ocr",
            },
        )

        graph.add_edge("run_writer", END)
        graph.add_edge("run_editor", END)
        graph.add_edge("run_ocr", END)

        return graph.compile()

    async def _route_mode(self, state: ComplaintState) -> ComplaintState:
        logger.info(f"Complaint workflow routing: mode={state.get('mode', 'write')}")
        return state

    async def _run_writer(self, state: ComplaintState) -> ComplaintState:
        result = await self.writer.run(
            query=state["query"],
            current_form=state.get("current_form"),
        )
        return {
            **state,
            "form_data": result["form_data"],
            "confidence": result["confidence"],
            "sources_used": result["sources_used"],
            "agent_used": self.writer.name,
        }

    async def _run_editor(self, state: ComplaintState) -> ComplaintState:
        result = await self.editor.run(
            instruction=state["query"],
            current_form=state.get("current_form", {}),
        )
        return {
            **state,
            "form_data": result["form_data"],
            "confidence": result["confidence"],
            "sources_used": result["sources_used"],
            "agent_used": self.editor.name,
        }

    async def _run_ocr(self, state: ComplaintState) -> ComplaintState:
        result = await self.ocr.run(
            document_text=state["query"],
            filename=state.get("filename", "unknown"),
        )
        return {
            **state,
            "form_data": result["form_data"],
            "confidence": result["confidence"],
            "sources_used": result["sources_used"],
            "agent_used": self.ocr.name,
        }

    async def run(self, mode: str, query: str, current_form: dict | None = None, filename: str = "unknown") -> dict:
        initial = ComplaintState(
            mode=mode,
            query=query,
            filename=filename,
            current_form=current_form,
            form_data=None,
            confidence=0.0,
            sources_used=[],
            agent_used="",
            errors=[],
        )
        result = await self.graph.ainvoke(initial)
        return dict(result)
