# Pharmaceutical Quality Management System (QMS) Knowledge Base

A comprehensive, structured pharmaceutical quality management knowledge base powering AI agents across the full QMS lifecycle: Medicine, Complaint Understanding/Extraction/Editing/Validation, Risk Assessment, Root Cause, CAPA, Regulatory Compliance.

---

## Overview

This knowledge base provides **150+ structured documents** covering:

- **Complaint Management**: Terms, categories, examples, intake forms
- **Quality Events**: Deviations, investigations, root cause analysis
- **CAPA**: Corrective and Preventive Actions
- **Regulatory**: FDA regulations, ICH guidelines, warning letters, recalls
- **Reference**: Medicines, dosage forms, equipment, manufacturing, packaging
- **Templates**: SOPs, forms, and document templates

### Key Features

| Feature | Description |
|---------|-------------|
| **Citation-Backed** | All facts include source, URL, retrieval date, and confidence rating |
| **Source Priority** | P1: Regulatory bodies → P2: Manufacturers → P3: Academic |
| **AI-Ready** | Structured JSON schemas for vector store ingestion |
| **Structured Data** | Machine-readable formats for programmatic access |

---

## Directory Structure

```
knowledge-base/
├── README.md                           # This file
├── knowledge_base_index.json           # Master index with metadata
│
├── abbreviations/                      # Pharmaceutical abbreviations (200+)
│   └── abbreviations.md
├── CAPA/                              # Corrective & Preventive Actions
│   └── CAPA_knowledge.md
├── complaint_categories/              # Complaint taxonomy (14 categories, 40+ sub-types)
│   └── complaint_categories.md
├── complaint_examples/                # Case study database (20 records)
│   └── complaint_examples.json
├── complaint_terms/                   # Complaint terminology mapping (120+ terms)
│   └── complaint_terms.md
├── datasets/                          # Data standards and schemas
├── deviations/                        # Deviation management
│   └── deviations.md
├── dosage_forms/                      # Dosage forms reference (24 types)
│   └── dosage_forms.md
├── equipment/                         # Pharmaceutical equipment (25 types)
│   └── pharmaceutical_equipment.md
├── FDA_recalls/                       # FDA recall knowledge
│   └── FDA_recalls.md
├── forms/                             # QMS form templates
│   ├── complaint_intake_form.md
│   └── investigation_report_form.md
├── images/                            # Visual aids and diagrams
├── investigations/                    # Investigation procedures
│   └── investigations.md
├── manufacturing/                     # Manufacturing stages (10 stages)
│   └── manufacturing_stages.md
├── medicines/                         # Drug knowledge base (100+ drugs)
│   └── medicines_index.md
├── packaging/                         # Packaging knowledge (14 types)
│   └── packaging_knowledge.md
├── pdfs/                              # Reference PDF documents
├── pharmaceutical_dictionary/         # Pharmaceutical terminology (150 terms)
│   └── pharmaceutical_dictionary.md
├── quality_control/                   # Quality control processes
├── quality_metrics/                   # Quality metrics and KPIs
├── regulations/                       # Regulatory standards
│   ├── 21_CFR_210_211_cGMP.md
│   ├── 21_CFR_Part_11.md
│   ├── ICH_Q7_GMP_API.md
│   └── regulatory_framework.md
├── regulatory/                        # Regulatory knowledge
├── root_cause_library/                # Root cause analysis library
├── SOP_examples/                      # SOP templates
│   └── SOP_template.md
├── sources/                           # Source management
│   └── sources_index.md
├── supplier_management/               # Supplier quality management
├── templates/                         # Document templates
│   └── capar_template.md
├── training/                          # Training materials
├── validation/                        # Validation documentation
├── vectors/                           # Vector store for RAG pipeline
└── warning_letters/                   # FDA warning letters
    └── FDA_warning_letters.md
```

---

## AI Agent Capabilities

This knowledge base powers:

| Agent | Purpose |
|-------|---------|
| **Medicine Agent** | Drug information, product lookup, defect patterns |
| **Complaint Understanding** | Complaint classification, severity assessment |
| **Complaint Extraction** | Structured data extraction from complaints |
| **Complaint Editing** | Complaint text normalization |
| **Complaint Validation** | Complaint data quality checks |
| **Risk Assessment** | Risk scoring, prioritization |
| **Root Cause Analysis** | RCA methods, root cause library |
| **CAPA Management** | CAPA workflow, effectiveness tracking |
| **Regulatory Compliance** | Regulatory requirements, inspection readiness |

---

## Data Standards

### Citation Format
All facts include:
- **Source**: Regulatory body or authoritative source
- **URL**: Stable reference URL
- **Date Retrieved**: When accessed
- **Confidence**: Accuracy rating (0-1 scale)
- **Category**: Content classification
- **Tags**: Searchable keywords

### Source Priority
1. **FDA, OpenFDA, DailyMed, NIH** (US regulatory)
2. **EMA, EudraLex, EMA Prac** (EU regulatory)
3. **WHO, ICH, PIC/S** (International)
4. **USP, ISPE, PDA** (Industry standards)
5. **RxNorm, DrugBank** (Drug databases)
6. **Manufacturers, Academic sources** (Secondary)

### Quality Principles
- **Never fabricate information** - cite all facts
- **Preserve references** - maintain traceability
- **Structured data** - JSON schemas for all records
- **Timely updates** - regular source verification

---

## Quick Start

1. **Browse by Category**: Use `Folder_Index.md` to navigate
2. **Search by Source**: Use `Source_Index.md` for source-specific queries
3. **Check Quality**: Use `Quality_Report.md` for completeness assessment
4. **Find Gaps**: Use `Missing_Data.md` for remediation priorities

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-07-28 | Initial release — merged duplicates, cleaned structure, added GitHub standards |

---

## Metadata

```json
{
  "document_id": "knowledge_base_readme",
  "category": "meta",
  "subcategory": "readme",
  "source_type": "Internal_Documentation",
  "authority": "QMS Knowledge Base Team",
  "version": "1.0.0",
  "format": "Markdown",
  "retrieved": "2026-07-28",
  "confidence": 0.99,
  "tags": ["README", "Knowledge_Base", "QMS", "Overview", "Directory_Structure", "AI_Agents", "Quick_Start", "Data_Standards"]
}
```
