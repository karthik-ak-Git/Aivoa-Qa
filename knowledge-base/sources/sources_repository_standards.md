# Sources Repository Standards

## Comprehensive Standards for Source Reference Management in Pharmaceutical QMS

---

## Source References
- ICH Guidelines (Q1–Q14)
- FDA Guidance Documents
- EU GMP / EudraLex
- WHO Guidelines
- USP-NF / USP Chapters
- ISPE Baseline Guides
- PDA Technical Reports
- PIC/S Guides
- ISO Standards
- Date Retrieved: 2026-07-28
- Confidence: 0.95

---

## 1. Source Categories

### 1.1 Primary Regulatory Sources

| Category | Source | Priority | Update Frequency |
|----------|--------|----------|------------------|
| **FDA Federal Register** | FDA.gov | 1st | Weekly |
| **FDA Guidance** | FDA.gov/Regulatory-Information | 1st | Monthly |
| **OpenFDA API** | OpenFDA.gov | 1st | Real-time/Daily |
| **DailyMed** | DailyMed.nlm.nih.gov | 1st | Weekly |
| **EMA Guidelines** | EMA.europa.eu | 1st | Monthly |
| **ICH Guidelines** | ICH.org | 1st | As published |
| **WHO Guidelines** | WHO.int | 1st | Monthly |
| **USP-NF** | USP.org | 1st | Quarterly |
| **PIC/S Guides** | Picscheme.eu | 2nd | As published |
| **ISO Standards** | ISO.org | 2nd | As published |
| **ISPE Baseline Guides** | ISPE.org | 2nd | As published |
| **PDA Technical Reports** | PDA.org | 3rd | As published |

### 1.2 Secondary Sources

| Category | Source | Priority | Update Frequency |
|----------|--------|----------|------------------|
| **Academic Literature** | PubMed, Google Scholar, ScienceDirect | 3rd | Continuous |
| **Industry Publications** | PharmTech, BioPharm, Drug Discovery & Dev | 3rd | Monthly |
| **Conference Proceedings** | ISPE, PDA, AAPS, RAPS | 4th | Annual/Conference |
| **FDA Warning Letters** | FDA.gov/Warning-Letters | 1st | Weekly |
| **FDA Recall Database** | FDA.gov/Recalls | 1st | Daily |
| **FDA Inspection Database** | FDA.gov/Inspections | 1st | Weekly |

---

## 2. Source Validation Standards

### 2.1 Source Quality Criteria

| Criterion | Requirement | Validation Method |
|-----------|-------------|-------------------|
| **Authority** | Official regulatory/government body | Check issuer |
| **Currency** | Published within 5 years (or current version) | Date check |
| **Relevance** | Directly applicable to QMS topic | Content review |
| **Accuracy** | Consistent with other authoritative sources | Cross-reference |
| **Completeness** | Covers required topic comprehensively | Gap analysis |
| **Accessibility** | Available at stable URL or reference | Link check |
| **Peer Review** | Reviewed by recognized experts | Check review status |

### 2.2 Source Ranking

| Rank | Source Type | Criteria |
|------|-------------|----------|
| **Tier 1** | Official regulations, laws, statutes | Legally binding, government-issued |
| **Tier 2** | Official guidance, standards, compendia | Recognized by regulatory authorities |
| **Tier 3** | Industry standards, technical reports | Recognized by industry bodies |
| **Tier 4** | Peer-reviewed publications | Scientific validation |
| **Tier 5** | Manufacturer documentation | Technical product information |
| **Tier 6** | Industry experience, expert opinion | Practical knowledge |

---

## 3. Citation Standards

### 3.1 Citation Format (APA 7th Edition for Regulations)

```
[Regulatory Body]. (Year). [Title of Document]. [Document Number/Version]. [URL].
[Date Retrieved].

Examples:
ICH. (2000). Q7: Good Manufacturing Practice Guide for Active Pharmaceutical Ingredients. ICH Harmonised Tripartite Guideline. https://www.ich.org/page/quality-guidelines. Retrieved 2026-07-28.

FDA. (2021). 21 CFR Part 11 - Electronic Records; Electronic Signatures. Code of Federal Regulations, Title 21, Part 11. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11. Retrieved 2026-07-28.

European Commission. (2022). EudraLex Volume 4 - Good Manufacturing Practice (GMP) Guidelines. EU GMP Annex 11: Computerised Systems. https://health.ec.europa.eu/medicinal-products/eudralex/eudralex-volume-4_en. Retrieved 2026-07-28.
```

### 3.2 Required Citation Fields

| Field | Description | Example |
|-------|-------------|---------|
| **Author/Issuer** | Issuing body | FDA, EMA, ICH, WHO, USP |
| **Year** | Publication or effective year | 2026 |
| **Title** | Full document title | "21 CFR Part 11 - Electronic Records; Electronic Signatures" |
| **Document Number** | Official identifier | "ICH Q7", "21 CFR Part 11", "Annex 11" |
| **Version** | Current version (if applicable) | "Revision 1", "v4.0" |
| **URL** | Stable reference URL | https://www.fda.gov/... |
| **Date Retrieved** | When accessed | "2026-07-28" |
| **Confidence** | Confidence in accuracy | 0.95 (0-1 scale) |

---

## 4. Source Registry

### 4.1 Core Regulatory Source Registry

| Source ID | Source Name | Issuing Body | Category | URL | Last Verified |
|-----------|-------------|--------------|----------|-----|---------------|
| SRC-FDA-001 | 21 CFR Part 11 | FDA | Regulation | https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11 | 2026-07-28 |
| SRC-FDA-002 | 21 CFR Parts 210/211 | FDA | Regulation | https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C | 2026-07-28 |
| SRC-FDA-003 | FDA Guidance: Computerized Systems in Clinical Investigations | FDA | Guidance | https://www.fda.gov/regulatory-information/search-fda-guidance-documents | 2026-07-28 |
| SRC-ICH-001 | ICH Q7: GMP for APIs | ICH | Guideline | https://www.ich.org/page/quality-guidelines | 2026-07-28 |
| SRC-ICH-002 | ICH Q1-Q14 | ICH | Guideline | https://www.ich.org/page/quality-guidelines | 2026-07-28 |
| SRC-EMA-001 | EudraLex Volume 4 | EU | Regulation | https://health.ec.europa.eu/medicinal-products/eudralex/eudralex-volume-4_en | 2026-07-28 |
| SRC-EMA-002 | EU GMP Annex 11 | EU | Regulation | https://health.ec.europa.eu/medicinal-products/eudralex/eudralex-volume-4_en | 2026-07-28 |
| SRC-WHO-001 | WHO GMP Guidelines | WHO | Guideline | https://www.who.int/teams/regulation-prequalification/regulatory-information/norms-and-standards | 2026-07-28 |
| SRC-USP-001 | USP-NF | USP | Compendium | https://www.usp.org/compounding/general-chapter-usp-nf | 2026-07-28 |
| SRC-PIC-001 | PIC/S GMP Guide | PIC/S | Guide | https://picscheme.eu/en/publications | 2026-07-28 |

---

## 5. Source Monitoring & Maintenance

### 5.1 Source Verification Schedule

| Source Category | Verification Frequency | Responsible | Method |
|-----------------|----------------------|-------------|--------|
| **FDA Regulations** | Annually | Regulatory Affairs | Web check + version comparison |
| **ICH Guidelines** | Annually | Regulatory Affairs | Web check + version comparison |
| **EMA Guidelines** | Annually | Regulatory Affairs | Web check + version comparison |
| **USP Chapters** | Quarterly | Quality Control | Web check + version comparison |
| **Manufacturer Info** | Annually | Supply Chain | Web check + contact verification |
| **Academic Sources** | As needed | R&D/QA | Citation verification |

### 5.2 Source Status Tracking

| Status | Description | Action Required |
|--------|-------------|-----------------|
| **Current** | Latest version, URL active | None |
| **Outdated** | Newer version available | Update reference |
| **Broken Link** | URL returns error | Find alternative source |
| **Deprecated** | Document officially withdrawn | Replace with successor |
| **Superseded** | Replaced by newer document | Update to new version |

---

## 6. Source Integration

### 6.1 Automated Source Integration

| Integration | Method | Frequency | Quality Gate |
|-------------|--------|-----------|--------------|
| **OpenFDA API** | REST API | Daily | Schema validation, deduplication |
| **DailyMed API** | REST API | Weekly | Completeness check |
| **FDA Warning Letters** | Web scraping | Weekly | Manual review |
| **FDA Recalls** | Web scraping | Daily | Deduplication |
| **PubMed** | E-utilities API | Weekly | Relevance filtering |
| **EUROPA** | RSS + scraping | Monthly | Manual review |

---

## Metadata

```json
{
  "document_id": "sources_repository_standards",
  "category": "sources",
  "subcategory": "source_management",
  "source_type": "Compiled_Technical_Standards",
  "authority": "FDA/EMA/ICH/WHO/USP/PIC/S/ISPE/PDA/ISO",
  "version": "2026.1",
  "format": "Markdown",
  "retrieved": "2026-07-28",
  "confidence": 0.95,
  "tags": ["Source_Management", "Citation_Standards", "Regulatory_Sources", "FDA", "EMA", "ICH", "WHO", "USP", "PIC_S", "Source_Validation", "Source_Monitoring", "Reference_Management", "Source_Quality", "Source_Registry"]
}
```