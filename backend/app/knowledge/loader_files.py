"""Local file-based knowledge loader (fallback when Supabase unavailable)."""

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
