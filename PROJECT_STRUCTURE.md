# Project Structure

Detailed guide to the repository layout.

---

## Root Level

| File | Description |
|------|-------------|
| `README.md` | Project overview, quick start, and documentation |
| `LICENSE` | MIT License |
| `CONTRIBUTING.md` | Contribution guidelines |
| `CODE_OF_CONDUCT.md` | Community standards |
| `SECURITY.md` | Security vulnerability reporting |
| `CHANGELOG.md` | Version history |
| `ROADMAP.md` | Planned improvements |
| `ARCHITECTURE.md` | System architecture documentation |
| `PROJECT_STRUCTURE.md` | This file |
| `RELEASE_NOTES_v1.md` | v1.0 release notes |

---

## knowledge-base/

The core knowledge repository with 18 domains.

### Index Files

| File | Description |
|------|-------------|
| `knowledge_base_index.json` | Master structured index of all directories and files |
| `Source_Index.md` | Registry of 36+ authoritative sources with citation counts |
| `Knowledge_Map.md` | Domain relationships and knowledge graph |
| `README.md` | Knowledge base overview and usage guide |

### Knowledge Domains

#### Complaint Management
- `complaint_categories/` — 14 complaint categories with severity matrices, root-cause mappings, and hierarchical taxonomy
- `complaint_terms/` — 120+ pharmaceutical complaint terms with QA language mapping
- `complaint_examples/` — 9 structured case studies with JSON schemas

#### Quality Processes
- `root_cause_library/` — 80+ root causes organized by 6M taxonomy
- `CAPA/` — Corrective and Preventive Action lifecycle with 7-step process
- `deviations/` — Deviation classification and investigation framework
- `investigations/` — Phase I/II investigation methodology and RCA methods

#### Regulatory
- `regulatory_framework.md` — FDA 21 CFR, ICH Q7-Q12, EU GMP, WHO guidelines
- `FDA_recalls/` — 11 FDA recall case studies (1982–2025)
- `warning_letters/` — 10 FDA warning letter analyses (2016–2025)

#### Pharmaceutical Products
- `medicines/` — 100+ drugs across 10 therapeutic categories
- `dosage_forms/` — 24 dosage forms with stability profiles
- `packaging/` — 14 packaging types with defect taxonomy

#### Manufacturing
- `manufacturing/` — 7 manufacturing stages (API + FDF) with CPPs
- `equipment/` — 25 equipment types with maintenance schedules
- `quality_control/` — Testing procedures and OOS/OOT handling
- `quality_metrics/` — KPIs and benchmarking data

#### Support Functions
- `training/` — Competency requirements and GMP training topics
- `validation/` — Process, equipment, cleaning, and CSV validation
- `supplier_management/` — Qualification, audits, quality agreements

#### Templates & Reference
- `templates/` — QMS document templates
- `forms/` — QMS form templates
- `SOP_examples/` — Standard Operating Procedure templates
- `pharmaceutical_dictionary/` — 150+ term glossary
- `abbreviations/` — 200+ pharmaceutical abbreviations

#### Data Standards
- `datasets/` — Data standards and schemas
- `vectors/` — Vector store and embedding standards
- `images/` — Image metadata standards
- `pdfs/` — PDF processing standards
- `sources/` — Source management standards

---

## frontend_prototype/

React + TypeScript complaint management UI with Express + Gemini AI backend.

| Directory | Description |
|-----------|-------------|
| `src/` | React source code (components, services, types) |
| `public/` | Static assets |
| `server.ts` | Express backend with Gemini AI integration |

| Config File | Description |
|-------------|-------------|
| `package.json` | Node.js dependencies and scripts |
| `vite.config.ts` | Vite build configuration |
| `tsconfig.json` | TypeScript configuration |
| `tailwind.config.js` | Tailwind CSS configuration |
| `eslint.config.js` | ESLint configuration |

---

## docs/

Internal documentation and pre-release reports.

| Directory | Description |
|-----------|-------------|
| `audit_reports/` | Quality assessments and readiness reviews |

---

## Naming Conventions

- **Knowledge files:** `snake_case.md`
- **Documentation files:** `kebab-case.md`
- **Schema files:** `snake_case.schema.json`
- **Directories:** `snake_case/` or `kebab-case/`
