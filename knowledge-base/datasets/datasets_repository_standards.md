# Datasets Repository Standards

## Comprehensive Standards for Structured Data Management in Pharmaceutical QMS

---

## Source References
- FDA 21 CFR Part 11 (Electronic Records)
- EU GMP Annex 11 (Computerised Systems)
- FAIR Data Principles (Findable, Accessible, Interoperable, Reusable)
- CDISC Standards (SDTM, ADaM, SEND)
- HL7 FHIR (Healthcare Interoperability)
- ISO 8000 (Data Quality)
- FAIRsharing.org Standards
- Date Retrieved: 2026-07-28
- Confidence: 0.95

---

## 1. Dataset Categories & Structure

### 1.1 Core Dataset Categories

| Category Code | Category | Description | Format Standards |
|---------------|----------|-------------|------------------|
| **MED** | Medicines/Product Master Data | Product catalog, specifications, compositions | JSON, CSV, Parquet |
| **BATCH** | Batch/Lot Genealogy | Batch records, genealogy, dispositions | JSON, CSV, Parquet |
| **DEV** | Deviation/Quality Events | Deviations, investigations, dispositions | JSON, CSV, Parquet |
| **CAPA** | CAPA Records | CAPA initiation, actions, verification | JSON, CSV, Parquet |
| **CMP** | Complaint/ADR Data | Complaints, ADRs, signals | JSON, CSV, Parquet |
| **RCL** | Recall Data | Recall strategies, execution, effectiveness | JSON, CSV, Parquet |
| **AUD** | Audit/Inspection Data | Audit plans, findings, responses | JSON, CSV, Parquet |
| **CHG** | Change Control Data | Change requests, assessments, implementations | JSON, CSV, Parquet |
| **SUP** | Supplier Data | Qualifications, audits, performance | JSON, CSV, Parquet |
| **TRN** | Training Data | Records, competencies, schedules | JSON, CSV, Parquet |
| **ENV** | Environmental Monitoring | EM trends, excursions, recoveries | JSON, CSV, Parquet, Time-series |
| **STB** | Stability Data | Protocols, results, statistical analysis | JSON, CSV, Parquet, SDTM |
| **LAB** | Laboratory Data | Test results, OOS, instrument data | JSON, CSV, Parquet, Allot |
| **EQP** | Equipment Data | Maintenance, calibration, qualification | JSON, CSV, Parquet |
| **RIS** | Risk Management | FMEA, HACCP, risk assessments | JSON, CSV, Parquet |
| **CAP** | CAPA Data | CAPA records, effectiveness, trends | JSON, CSV, Parquet |
| **SUB** | Regulatory Submissions | CTD metadata, submission tracking | JSON, XML, eCTD |
| **SIG** | Signal Detection | Statistical signals, trends, evaluations | JSON, CSV, Parquet |

---

## 2. Data Format Standards

### 2.1 Primary Formats

| Format | Use Case | Advantages | Tools |
|--------|----------|------------|-------|
| **JSON/JSON Lines** | APIs, NoSQL, flexible schemas | Human-readable, schema evolution | jq, Python, Spark |
| **CSV** | Tabular data, imports/exports | Universal compatibility | Excel, Python, R, SQL |
| **Parquet** | Analytics, big data, columnar | Compression, predicate pushdown | Spark, DuckDB, Athena |
| **Avro** | Streaming, schema evolution | Compact, fast serialization | Kafka, Spark |
| **XML** | Regulatory submissions (eCTD), HL7 | Standards compliance | XSLT, XPath |
| **HDF5** | Scientific arrays, time-series | Hierarchical, compression | h5py, PyTables |

### 2.2 Format Selection Guide

| Data Characteristic | Recommended Format |
|---------------------|-------------------|
| **Transactional/Relational** | Parquet, CSV |
| **Nested/Hierarchical** | JSON, Avro |
| **Time-series/High-volume** | Parquet, HDF5 |
| **Schema Evolution Needed** | Avro, JSON |
| **Regulatory Submission** | XML (eCTD), PDF/A |
| **Interoperability/Exchange** | JSON, CSV, FHIR |
| **Long-term Archival** | Parquet, CSV, PDF/A |

---

## 3. Schema Standards

### 3.1 Schema Definition (JSON Schema Example)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://pharma-qms.example.com/schemas/deviation-v1.0.json",
  "title": "Deviation Record",
  "type": "object",
  "required": ["deviation_id", "report_date", "product", "batch", "severity", "description"],
  "properties": {
    "deviation_id": {
      "type": "string",
      "pattern": "^DEV-\\d{4}-\\d{4}$",
      "description": "Unique deviation identifier"
    },
    "report_date": {
      "type": "string",
      "format": "date",
      "description": "Date deviation reported"
    },
    "detection_date": {
      "type": "string",
      "format": "date",
      "description": "Date deviation detected"
    },
    "product": {
      "type": "object",
      "required": ["name", "strength", "dosage_form"],
      "properties": {
        "name": {"type": "string"},
        "strength": {"type": "string"},
        "dosage_form": {"type": "string", "enum": ["Tablet", "Capsule", "Injection", "Other"]}
      }
    },
    "batch": {
      "type": "array",
      "items": {"type": "string", "pattern": "^[A-Z]{2,4}\\d{6,8}[A-Z]?$"}
    },
    "severity": {
      "type": "string",
      "enum": ["Critical", "Major", "Minor"]
    },
    "category": {
      "type": "string",
      "enum": ["Process", "Equipment", "Material", "Documentation", "Environmental", "Human Error"]
    },
    "description": {"type": "string", "minLength": 50},
    "immediate_actions": {"type": "string"},
    "investigation": {
      "type": "object",
      "properties": {
        "root_cause": {"type": "string"},
        "root_cause_category": {"type": "string", "enum": ["Man", "Machine", "Material", "Method", "Environment", "Measurement", "Management"]},
        "contributing_factors": {"type": "array", "items": {"type": "string"}},
        "impact_assessment": {"type": "object"}
      }
    },
    "capa_reference": {"type": "string", "pattern": "^CAPA-\\d{4}-\\d{4}$"},
    "status": {"type": "string", "enum": ["Open", "Under Investigation", "Under Review", "Closed", "Cancelled"]},
    "closure_date": {"type": "string", "format": "date"}
  }
}
```

### 3.2 Common Field Standards

| Field Type | Format | Validation | Examples |
|------------|--------|------------|----------|
| **ID Fields** | UUID v4 or Prefixed | Regex pattern | `DEV-2026-0045`, `CAPA-2026-0089` |
| **Dates** | ISO 8601 (YYYY-MM-DD) | ISO 8601 | `2026-07-28` |
| **Timestamps** | ISO 8601 UTC | ISO 8601 | `2026-07-28T14:30:00Z` |
| **Product Names** | Controlled vocabulary | Master data lookup | `Lipitor 10mg` |
| **Batch Numbers** | Site-specific pattern | Regex | `LOT20260715A`, `INJ20240315B` |
| **Categories** | Controlled vocabulary | Enum | `Critical`, `Major`, `Minor` |
| **Status Fields** | Controlled vocabulary | Enum | `Open`, `Closed`, `Under Review` |
| **Monetary Values** | Decimal(15,2) + Currency | ISO 4217 | `{"amount": 125000.00, "currency": "USD"}` |
| **Percentages** | Decimal(5,2) | 0-100 | `95.50` |
| **Counts** | Integer ≥ 0 | Min 0 | `42` |
| **Boolean** | true/false | Boolean | `true` |

---

## 4. Data Quality Standards

### 4.1 Data Quality Dimensions (ISO 8000)

| Dimension | Definition | Metric | Target |
|-----------|------------|--------|--------|
| **Completeness** | Required fields populated | % required fields populated | 100% |
| **Accuracy** | Values match reality | Error rate vs source | < 0.1% |
| **Consistency** | No contradictions | Cross-field validation | 0 conflicts |
| **Timeliness** | Data available when needed | Latency (source to warehouse) | < 1 hour |
| **Validity** | Conforms to schema/rules | Schema validation pass rate | 100% |
| **Uniqueness** | No duplicate records | Duplicate rate | 0% |
| **Integrity** | Referential integrity maintained | FK violations | 0 |

### 4.2 Data Quality Rules (Examples)

| Rule ID | Rule Description | Severity | Implementation |
|---------|------------------|----------|----------------|
| **DQ-001** | Deviation ID must be unique | Critical | Unique constraint |
| **DQ-002** | Batch number must exist in batch master | Critical | Foreign key |
| **DQ-003** | Closure date ≥ Report date | Major | Check constraint |
| **DQ-004** | Required fields not null | Critical | Not null constraint |
| **DQ-005** | Severity enum valid | Major | Enum constraint |
| **DQ-006** | Root cause category valid | Major | Enum constraint |
| **DQ-007** | CAPA reference format valid | Minor | Regex check |
| **DQ-008** | No duplicate deviation for same batch/event | Critical | Unique composite key |

---

## 5. Data Governance

### 5.1 Data Ownership Model

| Dataset Category | Data Owner | Data Steward | Technical Owner |
|------------------|------------|--------------|-----------------|
| **Medicines/Product** | Regulatory Affairs | Product Data Manager | IT Data Architect |
| **Batch/Lot** | Manufacturing | Batch Data Coordinator | MES Admin |
| **Deviations** | Quality Assurance | Deviation Coordinator | QMS Admin |
| **CAPA** | Quality Assurance | CAPA Coordinator | QMS Admin |
| **Complaints** | Pharmacovigilance/QA | Complaint Coordinator | PV/QMS Admin |
| **Audits** | Quality Assurance | Audit Coordinator | QMS Admin |
| **Changes** | Regulatory Affairs/QA | Change Coordinator | QMS Admin |
| **Suppliers** | Procurement/QA | Supplier Quality Manager | Procurement Sys Admin |
| **Training** | HR/Training | Training Coordinator | LMS Admin |
| **Environmental** | Facilities/Engineering | EM Coordinator | BMS/EMS Admin |
| **Stability** | R&D/Regulatory | Stability Coordinator | LIMS Admin |
| **Laboratory** | QC Management | Lab Data Coordinator | LIMS Admin |
| **Equipment** | Engineering/Maintenance | Equipment Data Manager | CMMS Admin |
| **Risk Management** | Quality Assurance | Risk Manager | QMS Admin |

---

## 6. Data Exchange & Interoperability

### 6.1 Standard Interfaces

| Interface | Standard | Protocol | Use Case |
|-----------|----------|----------|----------|
| **REST API** | OpenAPI 3.0 | HTTPS/JSON | Real-time queries, integrations |
| **GraphQL** | GraphQL Schema | HTTPS/JSON | Flexible queries, federated data |
| **FHIR** | HL7 FHIR R4 | HTTPS/JSON | Clinical/regulatory exchange |
| **CDISC** | SDTM/ADaM/SEND | XML/CSV | Clinical data submission |
| **eCTD** | ICH eCTD v4.0 | XML/PDF | Regulatory submission |
| **IDMP** | ISO 11615/11616 | XML/JSON | Product identification |
| **EDI** | ASC X12 / EDIFACT | VAN/AS2 | Supply chain transactions |
| **OPC UA** | IEC 62541 | TCP/Binary | Equipment/process data |

---

## 7. Metadata & Cataloging

### 7.1 Dataset Metadata (Data Catalog Entry)

```json
{
  "dataset_id": "DEV-2024-Q2",
  "name": "Deviation Records Q2 2024",
  "description": "All deviation records for Q2 2024 including investigations and CAPA linkages",
  "category": "DEV",
  "owner": "Quality Assurance",
  "steward": "Deviation Coordinator",
  "technical_owner": "QMS Admin",
  "source_systems": ["QMS-MasterControl", "LIMS-LabVantage"],
  "schema_version": "1.2",
  "format": "Parquet",
  "partitioning": "Year=2024/Month=04,05,06",
  "row_count": 1247,
  "size_bytes": 245760000,
  "checksum_sha256": "a1b2c3d4e5f6...",
  "created_date": "2024-07-15",
  "last_updated": "2024-07-15T08:00:00Z",
  "refresh_frequency": "Daily incremental",
  "retention": "1 year post batch expiry",
  "pii_classification": "None",
  "confidentiality": "Confidential",
  "regulatory_relevance": true,
  "tags": ["deviations", "quality-events", "investigations", "capa"],
  "lineage": {
    "source_systems": ["QMS-MasterControl", "LIMS-LabVantage"],
    "transformations": ["deduplication", "enrichment", "standardization"],
    "downstream_consumers": ["BI-Dashboard", "CAPA-System", "Regulatory-Reporting"]
  },
  "quality_metrics": {
    "completeness": 0.999,
    "accuracy": 0.9995,
    "timeliness_hours": 2.5,
    "last_quality_check": "2024-07-28T06:00:00Z"
  },
  "access_control": {
    "read_roles": ["QA", "Production", "Regulatory", "Management"],
    "write_roles": ["QA-Deviation-Coordinator"],
    "admin_roles": ["QMS-Admin"]
  }
}
```

---

## 8. Data Pipeline Architecture

### 8.1 Modern Data Stack

```
Source Systems → Ingestion → Raw Zone → Staging → Curated → Serving
     │              │           │          │          │         │
  QMS, LIMS,    Batch/      Raw         Cleaned,    Business   BI, ML,
  MES, ERP,     Stream      (Bronze)    Validated   Ready      API, 
  LIMS, ERP,    (Kafka,     (Delta/     (Silver)    (Gold)     Reports,
  CMMS, LMS     Debezium)   Parquet)    (Delta/     (Delta/    Dashboards,
                                    Parquet)   Parquet)   ML Models
```

### 8.2 Pipeline Quality Gates

| Stage | Quality Checks | Failure Action |
|-------|----------------|----------------|
| **Ingestion** | Schema validation, row counts, checksums | Quarantine, alert |
| **Raw → Staging** | Schema enforcement, null checks, duplicates | Quarantine, alert |
| **Staging → Curated** | Business rules, referential integrity, SCD logic | Block promotion, alert |
| **Curated → Serving** | Aggregation accuracy, KPI validation, freshness | Block deployment, alert |

---

## Metadata

```json
{
  "document_id": "datasets_repository_standards",
  "category": "datasets",
  "subcategory": "data_standards",
  "source_type": "Compiled_Technical_Standards",
  "authority": "FDA/EMA/ICH/CDISC/HL7/ISO/FAIR",
  "version": "2026.1",
  "format": "Markdown",
  "retrieved": "2026-07-28",
  "confidence": 0.95,
  "tags": ["Data_Standards", "Data_Formats", "JSON", "CSV", "Parquet", "Avro", "Schema_Standards", "Data_Quality", "Data_Governance", "Data_Lineage", "FAIR_Principles", "CDISC", "FHIR", "Data_Pipeline", "Data_Catalog", "Metadata_Management", "Data_Quality"]
}
```