import os
import json
from pathlib import Path
from typing import Any
from app.core.logger import get_logger

logger = get_logger("knowledge.loader")

KNOWLEDGE_DOMAINS = {
    "complaint_terms": {
        "path": "complaint_terms/complaint_terms.md",
        "description": "Complaint terminology and classification",
    },
    "complaint_categories": {
        "path": "complaint_categories/complaint_categories.md",
        "description": "Complaint category taxonomy",
    },
    "complaint_examples": {
        "path": "complaint_examples/complaint_examples.json",
        "description": "Structured complaint case studies",
    },
    "root_cause_library": {
        "path": "root_cause_library/root_cause_library.md",
        "description": "Root cause analysis library (6M taxonomy)",
    },
    "CAPA": {
        "path": "CAPA/CAPA_knowledge.md",
        "description": "Corrective and Preventive Action knowledge",
    },
    "medicines": {
        "path": "medicines/medicines_index.md",
        "description": "Drug knowledge base",
    },
    "regulations": {
        "path": "regulations/regulatory_framework.md",
        "description": "Regulatory framework (FDA, ICH, EU GMP, WHO)",
    },
    "FDA_recalls": {
        "path": "FDA_recalls/FDA_recalls.md",
        "description": "FDA recall case studies and classifications",
    },
    "warning_letters": {
        "path": "warning_letters/FDA_warning_letters.md",
        "description": "FDA warning letter analyses",
    },
    "manufacturing": {
        "path": "manufacturing/manufacturing_stages.md",
        "description": "Manufacturing stages with CPPs",
    },
    "packaging": {
        "path": "packaging/packaging_knowledge.md",
        "description": "Packaging systems and defect taxonomy",
    },
    "quality_control": {
        "path": "quality_control/quality_control_extended.md",
        "description": "Testing procedures and OOS/OOT handling",
    },
    "validation": {
        "path": "validation/validation_documentation_extended.md",
        "description": "Process, equipment, cleaning validation",
    },
    "supplier_management": {
        "path": "supplier_management/supplier_management_extended.md",
        "description": "Supplier qualification and auditing",
    },
    "deviations": {
        "path": "deviations/deviations.md",
        "description": "Deviation management framework",
    },
    "investigations": {
        "path": "investigations/investigations.md",
        "description": "Investigation procedures and RCA methods",
    },
    "training": {
        "path": "training/training_materials_extended.md",
        "description": "GMP training and competency requirements",
    },
    "equipment": {
        "path": "equipment/pharmaceutical_equipment.md",
        "description": "Pharmaceutical equipment knowledge",
    },
    "pharmaceutical_dictionary": {
        "path": "pharmaceutical_dictionary/pharmaceutical_dictionary.md",
        "description": "Pharmaceutical terminology glossary",
    },
    "dosage_forms": {
        "path": "dosage_forms/dosage_forms.md",
        "description": "Dosage form specifications",
    },
}


def find_knowledge_base() -> str:
    backend_dir = Path(__file__).parent.parent.parent  # backend/
    project_root = backend_dir.parent  # project root (Aivoa-Qa/)
    candidates = [
        project_root / "knowledge-base",
        backend_dir / "knowledge-base",
        Path("knowledge-base"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate.resolve())
    raise FileNotFoundError(
        f"Knowledge base directory not found. Tried: {[str(c) for c in candidates]}"
    )


def load_knowledge_base() -> list[dict[str, Any]]:
    kb_path = find_knowledge_base()
    documents = []
    for domain, info in KNOWLEDGE_DOMAINS.items():
        file_path = os.path.join(kb_path, info["path"])
        if not os.path.exists(file_path):
            logger.warning(f"Knowledge file not found: {file_path}")
            continue
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            chunks = chunk_document(content, domain)
            for i, chunk in enumerate(chunks):
                documents.append({
                    "id": f"{domain}_{i}",
                    "content": chunk,
                    "domain": domain,
                    "source": info["path"],
                    "title": f"{domain} - chunk {i}",
                    "metadata": {
                        "domain": domain,
                        "description": info["description"],
                        "source_file": info["path"],
                        "chunk_index": i,
                        "total_chunks": len(chunks),
                    },
                })
            logger.info(f"Loaded {len(chunks)} chunks from domain: {domain}")
        except Exception as e:
            logger.error(f"Failed to load domain {domain}: {e}")
    logger.info(f"Total documents loaded: {len(documents)}")
    return documents


def chunk_document(content: str, domain: str, chunk_size: int = 1000, overlap: int = 200) -> list[str]:
    lines = content.split("\n")
    chunks = []
    current_chunk = []
    current_size = 0

    for line in lines:
        current_chunk.append(line)
        current_size += len(line)
        if current_size >= chunk_size:
            chunks.append("\n".join(current_chunk))
            if overlap > 0:
                overlap_lines = current_chunk[-overlap // 10:]
                current_chunk = overlap_lines
                current_size = sum(len(l) for l in overlap_lines)
            else:
                current_chunk = []
                current_size = 0

    if current_chunk:
        chunks.append("\n".join(current_chunk))

    return chunks if chunks else [content[:chunk_size]]
