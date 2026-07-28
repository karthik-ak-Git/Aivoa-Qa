# Architecture

## System Overview

The PharmaQMS Knowledge Base is a structured, citable pharmaceutical quality management knowledge repository designed to power AI-native quality operations.

## Architecture Principles

1. **Source Authority** — Every fact cites an authoritative regulatory source
2. **Machine-Readable** — Structured JSON schemas alongside human-readable Markdown
3. **AI-Ready** — Embedding strategies, chunking standards, and RAG pipeline support
4. **Modular** — Independent knowledge domains that can be used separately or together
5. **Audit-Traceable** — Full provenance from claim to source document

## Knowledge Layer Architecture

```
┌─────────────────────────────────────────────────────┐
│                  AI / Application Layer             │
│  (RAG Pipelines, Knowledge Graphs, AI Agents, APIs) │
├─────────────────────────────────────────────────────┤
│                  Knowledge Layer                    │
│  Markdown Documents + JSON Schemas + Citations      │
├─────────────────────────────────────────────────────┤
│                  Index Layer                        │
│  knowledge_base_index.json + Source_Index.md        │
├─────────────────────────────────────────────────────┤
│                  Standards Layer                    │
│  Vector Store + Embedding + Chunking Standards      │
├─────────────────────────────────────────────────────┤
│                  Source Layer                       │
│  FDA, ICH, EMA, WHO, USP, ISPE, PDA, PIC/S         │
└─────────────────────────────────────────────────────┘
```

## Data Flow

```
Regulatory Sources
        ↓
  Knowledge Documents (Markdown + JSON)
        ↓
  Structured Index (JSON)
        ↓
  Embedding / Vectorization
        ↓
  Vector Store (Pinecone, Weaviate, etc.)
        ↓
  RAG Pipeline / Knowledge Graph
        ↓
  AI Agents / Applications
```

## Domain Relationships

The knowledge base forms a connected graph where domains reference each other:

```
Customer Complaints
    ├── Root Cause Analysis
    ├── CAPA Management
    ├── Deviation Management
    ├── Investigation Management
    └── Regulatory Compliance
            ├── FDA 21 CFR
            ├── ICH Guidelines
            ├── EU GMP
            └── WHO Standards

Manufacturing
    ├── Equipment
    ├── Quality Control
    ├── Validation
    └── Supplier Management

Medicines
    ├── Dosage Forms
    ├── Packaging
    └── Manufacturing
```

## AI Agent Architecture

10 pre-defined agent roles with mapped knowledge dependencies:

| Agent | Primary Domains | Secondary Domains |
|-------|----------------|-------------------|
| complaint-intake | complaint_terms, complaint_categories | pharmaceutical_dictionary, abbreviations |
| complaint-classify | complaint_categories, medicines | dosage_forms, root_cause_library |
| complaint-analyze | root_cause_library, investigations | deviations, CAPA |
| capa-generate | CAPA, root_cause_library | regulations, templates |
| regulatory-check | regulations, FDA_recalls, warning_letters | deviations, complaints |
| quality-monitor | quality_metrics, training | quality_control, deviations |
| audit-support | regulations, training, SOP_examples | validations, suppliers |
| training-deliver | training, pharmaceutical_dictionary | all domains |
| supplier-evaluate | supplier_management, complaints | deviations, CAPA |
| manufacturing-context | manufacturing, equipment, quality_control | validation, packaging |

## Schema Standards

All structured data follows JSON Schema (Draft-07):

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["id", "name", "category"],
  "properties": {
    "id": { "type": "string" },
    "name": { "type": "string" },
    "category": { "type": "string" },
    "severity": { "type": "string", "enum": ["critical", "major", "minor"] },
    "source": { "type": "string", "format": "uri" },
    "confidence": { "type": "number", "minimum": 0, "maximum": 1 }
  }
}
```

## Vector Store Strategy

Recommended configuration for RAG deployment:

| Parameter | Value |
|-----------|-------|
| Embedding Model | text-embedding-3-large (OpenAI) or voyage-3 |
| Chunk Size | 512–1024 tokens |
| Chunk Overlap | 50–100 tokens |
| Metadata | Source, domain, confidence, category |
| Index Type | HNSW (Hierarchical Navigable Small World) |
| Similarity Metric | Cosine similarity |

## Security Considerations

- No patient-identifiable information in knowledge base
- No proprietary company data included
- All sources are publicly available regulatory documents
- MIT License allows broad reuse
