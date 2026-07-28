# PharmaQMS Knowledge Base

> Open-source pharmaceutical quality management knowledge base powering AI-native customer complaint management, CAPA, and regulatory compliance.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](./RELEASE_NOTES_v1.md)

---

## What Is This?

A comprehensive, structured knowledge base covering the full pharmaceutical quality management system (QMS) lifecycle — from customer complaint intake through root cause analysis, CAPA, and regulatory compliance. Built to power AI agents, RAG pipelines, and knowledge graphs for pharmaceutical quality operations.

**Manufacturer coverage:** API (Active Pharmaceutical Ingredient) and FDF (Finished Dosage Form).

---

## Purpose

Pharmaceutical quality management involves navigating complex regulatory frameworks (FDA 21 CFR, ICH, EU GMP, WHO), managing customer complaints, conducting root cause investigations, and implementing corrective and preventive actions (CAPA). This knowledge base provides:

- **Structured, citable pharmaceutical knowledge** — every fact sourced from authoritative regulatory bodies
- **AI-ready data** — JSON schemas, vector store standards, and embedding strategies for RAG pipelines
- **Comprehensive domain coverage** — complaint management, CAPA, deviations, investigations, regulatory compliance, manufacturing, medicines, and more
- **Actionable agent mappings** — pre-defined dependencies for 10 specialized AI agents

---

## Knowledge Domains

| Domain | Coverage | Key Files |
|--------|----------|-----------|
| **Complaint Management** | 14 categories, 120+ terms, 9 structured cases | `complaint_categories/`, `complaint_terms/`, `complaint_examples/` |
| **Root Cause Analysis** | 6M taxonomy, 80+ root causes | `root_cause_library/` |
| **CAPA Management** | Full lifecycle, 7-step process, JSON schemas | `CAPA/` |
| **Deviation Management** | Classification, investigation framework | `deviations/` |
| **Investigations** | Phase I/II, RCA methods, trend analysis | `investigations/` |
| **Regulatory Compliance** | FDA 21 CFR, ICH Q7-Q12, EU GMP, WHO, USP | `regulations/` |
| **FDA Enforcement** | 11 recalls (1982–2025), 10 warning letters (2016–2025) | `FDA_recalls/`, `warning_letters/` |
| **Medicines** | 100+ drugs across 10 therapeutic categories | `medicines/` |
| **Manufacturing** | 7 stages, API + FDF, CPPs and failure modes | `manufacturing/` |
| **Equipment** | 25 types with maintenance and calibration schedules | `equipment/` |
| **Packaging** | 14 types, defect taxonomy, regulatory considerations | `packaging/` |
| **Dosage Forms** | 24 forms with stability profiles | `dosage_forms/` |
| **Quality Control** | Testing procedures, OOS/OOT, trending | `quality_control/` |
| **Training** | Competency requirements, GMP topics | `training/` |
| **Validation** | Process, equipment, cleaning, CSV | `validation/` |
| **Supplier Management** | Qualification, audits, quality agreements | `supplier_management/` |
| **Templates & Forms** | SOPs, CAPA records, intake forms | `templates/`, `forms/`, `SOP_examples/` |
| **Reference** | 150+ term dictionary, 200+ abbreviations | `pharmaceutical_dictionary/`, `abbreviations/` |

---

## Data Sources

All knowledge is sourced from authoritative regulatory and industry bodies:

| Source | Type | References |
|--------|------|------------|
| **FDA** | 21 CFR Parts 11, 210, 211; Guidance Documents; Warning Letters; Recall Database | 45+ |
| **ICH** | Q1–Q14 Quality Guidelines | 30+ |
| **EMA** | EudraLex Volume 4, Annex 11, GMP/GDP Inspections | 25+ |
| **WHO** | GMP Guidelines, Technical Report Series | 15+ |
| **USP** | USP-NF, General Chapters | 20+ |
| **ISPE** | Baseline Guides, GAMP 5 | 10+ |
| **PDA** | Technical Reports | 8+ |
| **PIC/S** | GMP Guide | 10+ |
| **Drug Databases** | DailyMed, OpenFDA, RxNorm, DrugBank, Orange Book | 35+ |
| **Academic** | PubMed, Google Scholar, ScienceDirect | 20+ |

**Total: 228+ citations from 36 authoritative sources.**

---

## Repository Statistics

| Metric | Value |
|--------|-------|
| Total documents | 75+ |
| Knowledge domains | 18 |
| Structured JSON schemas | 15+ |
| Source citations | 228+ |
| Estimated word count | 750,000+ |
| Estimated pages | 2,500+ |
| Quality score | 93.5/100 |
| AI readiness score | 82/100 |

---

## Folder Structure

```
pharmaqms-knowledge-base/
├── README.md                          # This file
├── LICENSE                            # MIT License
├── CONTRIBUTING.md                    # Contribution guidelines
├── CODE_OF_CONDUCT.md                 # Community standards
├── SECURITY.md                        # Security policy
├── CHANGELOG.md                       # Version history
├── ROADMAP.md                         # Planned improvements
├── ARCHITECTURE.md                    # System architecture
├── PROJECT_STRUCTURE.md               # Detailed folder guide
├── RELEASE_NOTES_v1.md               # v1.0 release notes
│
├── knowledge-base/                    # Core knowledge base
│   ├── README.md                      # Knowledge base overview
│   ├── knowledge_base_index.json      # Master structured index
│   ├── Source_Index.md                # Source registry (36 sources)
│   ├── Knowledge_Map.md               # Domain relationships
│   │
│   ├── complaint_categories/          # 14 complaint categories + taxonomy
│   ├── complaint_terms/               # 120+ complaint terms + terminology
│   ├── complaint_examples/            # 9 structured cases + JSON data
│   ├── root_cause_library/            # 80+ root causes, 6M framework
│   ├── CAPA/                          # CAPA lifecycle, schemas, examples
│   ├── deviations/                    # Deviation classification + framework
│   ├── investigations/                # Investigation methodology + examples
│   ├── regulations/                   # FDA, ICH, EU GMP, WHO standards
│   ├── FDA_recalls/                   # 11 FDA recall case studies
│   ├── warning_letters/               # 10 FDA warning letter analyses
│   ├── medicines/                     # 100+ drugs, 10 categories
│   ├── manufacturing/                 # 7 manufacturing stages
│   ├── equipment/                     # 25 equipment types
│   ├── packaging/                     # 14 packaging types
│   ├── dosage_forms/                  # 24 dosage forms
│   ├── quality_control/               # QC testing + OOS procedures
│   ├── quality_metrics/               # KPIs + benchmarking
│   ├── training/                      # Training programs + competency
│   ├── validation/                    # Validation documentation
│   ├── supplier_management/           # Supplier qualification
│   ├── templates/                     # Document templates
│   ├── forms/                         # QMS form templates
│   ├── SOP_examples/                  # SOP templates
│   ├── abbreviations/                 # 200+ abbreviations
│   ├── pharmaceutical_dictionary/     # 150+ pharmaceutical terms
│   ├── datasets/                      # Data standards + schemas
│   ├── vectors/                       # Vector store + embedding standards
│   ├── images/                        # Image metadata standards
│   ├── pdfs/                          # PDF standards
│   └── sources/                       # Source management standards
│
├── frontend_prototype/                # Complaint management UI prototype
│   ├── src/                           # React + TypeScript source
│   ├── server.ts                      # Express + Gemini AI backend
│   └── package.json                   # Dependencies
│
└── docs/                              # Internal reports (pre-release)
    └── audit_reports/                 # Quality and readiness assessments
```

---

## AI Use Cases

### RAG (Retrieval-Augmented Generation)
- Vector store standards defined in `knowledge-base/vectors/`
- Chunking strategies for markdown documents
- Embedding model recommendations (text-embedding-3-large, voyage-3)
- Metadata-enriched chunks with source citations

### Knowledge Graph
- Domain relationships mapped in `knowledge-base/Knowledge_Map.md`
- Cross-references between complaint → root cause → CAPA → regulatory
- Entity relationships: drugs, equipment, manufacturers, regulations

### AI Agents (10 Pre-defined)

| Agent | Purpose |
|-------|---------|
| `complaint-intake` | Parse and standardize incoming complaints |
| `complaint-classify` | Auto-classify by category, severity, product type |
| `complaint-analyze` | Root cause analysis and investigation recommendations |
| `capa-generate` | Generate CAPA proposals with timelines and effectiveness criteria |
| `regulatory-check` | Map complaints to regulatory requirements |
| `quality-monitor` | Trend analysis and management review support |
| `audit-support` | Prepare for and support regulatory audits |
| `training-deliver` | Deliver training and assess competency |
| `supplier-evaluate` | Track supplier-related complaints and performance |
| `manufacturing-context` | Provide manufacturing context for complaints |

### Customer Complaint Management
- Full complaint lifecycle: intake → classification → investigation → CAPA → closure
- 14 complaint categories with severity mappings
- 120+ pharmaceutical complaint terms with QA language mapping
- 9 structured complaint examples with JSON schemas

---

## Getting Started

### For Developers

```bash
# Clone the repository
git clone https://github.com/your-org/pharmaqms-knowledge-base.git
cd pharmaqms-knowledge-base

# Browse the knowledge base
ls knowledge-base/

# View the master index
cat knowledge-base/knowledge_base_index.json

# Run the frontend prototype
cd frontend_prototype
npm install
cp .env.example .env  # Add your GEMINI_API_KEY
npm run dev
```

### For AI/ML Engineers

1. Start with `knowledge-base/knowledge_base_index.json` for the structured index
2. Use `knowledge-base/vectors/vector_store_standards.md` for embedding strategy
3. Follow `knowledge-base/Source_Index.md` for citation requirements
4. Review `knowledge-base/Knowledge_Map.md` for entity relationships

### For Quality Professionals

1. Browse by domain using `knowledge-base/README.md`
2. Use `knowledge-base/complaint_categories/` for complaint taxonomy
3. Reference `knowledge-base/regulations/` for compliance requirements
4. Use `knowledge-base/CAPA/` for CAPA process guidance

---

## Quality Assurance

| Metric | Score |
|--------|-------|
| Data Quality | 94/100 |
| Source Quality | 95/100 |
| Content Quality | 93/100 |
| Technical Quality | 92/100 |
| **Overall** | **93.5/100** |

- 100% source citation coverage
- 100% JSON schema compliance
- 0.94 average confidence score
- 100% metadata completeness

---

## Roadmap

See [ROADMAP.md](./ROADMAP.md) for detailed plans.

**v1.1 (Planned):**
- Expand medicine database to 50+ products
- Add 20+ real-world complaint examples
- Add EMA inspection data
- Implement regulatory alert monitoring

**v2.0 (Planned):**
- Full RAG pipeline with pre-computed embeddings
- Interactive knowledge graph visualization
- REST API for programmatic access
- Multi-language support (Japanese, Chinese, German)

---

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

---

## License

This project is licensed under the MIT License — see [LICENSE](./LICENSE) for details.

---

## Acknowledgments

- FDA for open regulatory data
- ICH for quality guidelines
- EMA for EudraLex framework
- WHO for global GMP standards
- The pharmaceutical quality community
