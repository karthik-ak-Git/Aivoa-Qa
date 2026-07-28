# SOP Examples for Pharmaceutical QMS

## Comprehensive Standard Operating Procedure Templates

---

## Source References
- FDA 21 CFR 211 Subpart F (Production and Process Controls)
- EU GMP Chapter 4 (Documentation)
- ICH Q10 - Pharmaceutical Quality System
- PDA Technical Report 56 - CAPA
- ISPE GAMP 5
- Date Retrieved: 2026-07-28
- Confidence: 0.95

---

## 1. SOP Template Structure (Master Template)

### SOP Header
```markdown
# SOP-XXXX: [SOP Title]

**Document Control:**
- Document Number: SOP-XXXX
- Version: 1.0
- Effective Date: YYYY-MM-DD
- Review Date: YYYY-MM-DD
- Status: ☐ Draft ☐ Under Review ☐ Approved ☐ Obsolete

**Approval Signatures:**
| Role | Name | Signature | Date |
|------|------|-----------|------|
| Author | | | |
| Reviewer (QA) | | | |
| Approver (Dept Head) | | | |
| QA Final Approval | | | |

**Revision History:**
| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| 1.0 | YYYY-MM-DD | Name | Initial release |

**Distribution List:**
- Department/Role: ___________
- Controlled Copy #: ___________

---

## 1. Purpose
[Clear, concise statement of what this SOP covers and why it exists]

## 2. Scope
[Where this SOP applies: departments, products, processes, locations, exclusions]

## 3. Responsibilities
| Role | Responsibility |
|------|----------------|
| [Role] | [Specific duties] |

## 4. Definitions & Abbreviations
| Term | Definition |
|------|------------|

## 5. References
- Regulatory: 21 CFR XXX, ICH QX, EU GMP Annex X
- Internal: SOP-XXXX, Form-XXXX, Policy-XXXX

## 6. Procedure
### 6.1 [Phase 1 Title]
[Step-by-step numbered instructions with decision points]

### 6.2 [Phase 2 Title]
[Step-by-step numbered instructions]

## 7. Documentation & Records
| Record | Retention | Location | Responsible |
|--------|-----------|----------|-------------|

## 8. Training Requirements
| Role | Training Method | Frequency | Assessment |
|------|----------------|-----------|------------|

## 9. Change Control
[Reference to Change Control SOP]

## 10. Deviation Handling
[Reference to Deviation Management SOP]

## 11. Appendices
- Appendix A: [Title]
- Appendix B: [Title]

## 12. Forms & Attachments
- Form-XXXX: [Title]
```

---

## 2. Critical SOP Examples

### SOP-QA-001: Deviation Management

```markdown
# SOP-QA-001: Deviation Management

**Document Control:**
- Document Number: SOP-QA-001
- Version: 3.2
- Effective Date: 2026-01-15
- Status: Approved

---

## 1. Purpose
To define a standardized process for identification, documentation, investigation, classification, and closure of deviations from approved procedures, specifications, or established standards in GMP operations.

## 2. Scope
Applies to all GMP operations at [Site Name]: Manufacturing, Packaging, Quality Control, Warehousing, Engineering, and Contract Operations.
**Exclusions:** Non-GMP administrative processes (refer to SOP-ADM-001).

## 3. Responsibilities

| Role | Responsibility |
|------|----------------|
| **Deviation Originator** | Identify, report immediately, complete Deviation Report Form (Form-QA-001) within 24 hours |
| **Department Supervisor** | Initial assessment, containment, assign investigation owner |
| **QA Investigator** | Lead investigation, root cause analysis, CAPA development |
| **Quality Unit (QU)** | Review/approve classification, investigation, CAPA, closure |
| **Department Head** | Resource allocation, CAPA implementation oversight |
| **QA Manager** | Final approval, trending, regulatory reporting assessment |

## 4. Definitions

| Term | Definition |
|------|------------|
| **Deviation** | Any departure from approved documents (SOPs, BPRs, specs, protocols) or standards |
| **Critical Deviation** | May impact product quality, patient safety, data integrity, or regulatory compliance |
| **Major Deviation** | Significant impact on quality systems, GMP compliance, or process consistency |
| **Minor Deviation** | Low impact, administrative, no direct product quality effect |
| **Planned Deviation** | Pre-approved temporary change with documented justification |
| **Unplanned Deviation** | Unexpected departure requiring immediate action |
| **CAPA** | Corrective and Preventive Action |

## 5. Procedure

### 5.1 Deviation Identification & Reporting (0-24 hours)

**5.1.1** Any personnel identifying a deviation shall:
1. **STOP** - Take immediate action to prevent further impact (quarantine, segregate, stop line)
2. **NOTIFY** - Verbally inform immediate supervisor and QA within 1 hour
3. **DOCUMENT** - Complete Form-QA-001 (Deviation Report) within 24 hours of discovery
4. **QUARANTINE** - Affected material/product per SOP-QA-002 (Material Quarantine)

**5.1.2** Form-QA-001 Minimum Required Fields:
- Date/time of discovery and occurrence
- Product, batch/lot number, equipment, area
- Description of deviation (what, when, where, how discovered)
- Immediate containment actions taken
- Potential impact assessment (product quality, patient safety, regulatory)
- Reporter name, department, contact

### 5.2 Initial Assessment & Classification (24-48 hours)

**5.2.1** QA Investigator and Department Supervisor perform joint assessment:
- Review Form-QA-001 for completeness
- Assess impact on: Product quality, Patient safety, Data integrity, Regulatory compliance, Batch disposition
- Assign preliminary classification:

| Classification | Criteria | Examples |
|----------------|----------|----------|
| **Critical** | Direct patient safety risk; Data integrity breach; Regulatory reporting required; Product recall potential | OOS with safety impact; Sterility failure; Data deletion; Cross-contamination |
| **Major** | Significant quality system impact; GMP non-compliance; Potential batch rejection | Process parameter OOS; Equipment qualification lapse; SOP not followed affecting quality |
| **Minor** | Low/no product impact; Administrative; Documentation error corrected immediately | Typo in batch record corrected per GDP; Late entry per SOP; Cosmetic label defect |

**5.2.2** For Critical/Major: Initiate CAPA per SOP-QA-003 (CAPA Management)
**5.2.3** For Planned Deviations: Complete Form-QA-001A (Planned Deviation Request) **before** execution

### 5.3 Investigation & Root Cause Analysis (5-30 business days)

**5.3.1** Investigation Team Composition:
- Lead: QA Investigator (assigned by QA Manager)
- Members: Subject Matter Experts (Production, QC, Engineering, Validation as needed)
- Timeline: Critical (15 days), Major (30 days), Minor (45 days)

**5.3.2** Investigation Requirements:
1. **Timeline Reconstruction** - Chronological sequence of events
2. **Data Collection** - Batch records, logbooks, electronic data, interviews, photos
3. **Root Cause Analysis** - Apply appropriate tool:
   - 5 Whys (simple, linear)
   - Fishbone/Ishikawa (multiple factors)
   - Fault Tree Analysis (complex systems)
   - FMEA (process design)
   - Change Analysis (post-change deviations)
4. **Impact Assessment** - Product, other batches, systems, regulatory
5. **Root Cause Statement** - Specific, verifiable, actionable

**5.3.3** Root Cause Documentation (Form-QA-001B):
- Root Cause Category: [Man/Method/Machine/Material/Environment/Measurement/Management]
- Root Cause Description: [Specific, evidence-based]
- Contributing Factors: [List]
- Why Root Cause Not Detected Earlier: [Gap analysis]

### 5.4 CAPA Development & Implementation

**5.4.1** Corrective Actions (fix the specific problem):
- Specific to root cause
- Implemented and verified before closure
- Effectiveness check defined

**5.4.2** Preventive Actions (prevent recurrence):
- Systemic, sustainable
- May include: Procedure revision, System enhancement, Training, Automation, Design change
- Effectiveness check with metrics

**5.4.3** CAPA Tracking: All CAPAs entered in CAPA Tracking System (SOP-QA-003)

### 5.5 Deviation Closure

**5.5.1** Closure Package Requirements:
- Completed investigation report (Form-QA-001B)
- Implemented CAPAs with verification evidence
- Batch disposition (if applicable) per SOP-QA-004
- Regulatory reporting assessment (Field Alert, Recall)
- QA Manager approval signature

**5.5.2** Closure Timelines:
- Critical: 30 business days from initiation
- Major: 60 business days
- Minor: 90 business days
- Extensions require QA Manager written justification

### 5.6 Trending & Reporting

**5.6.1** Monthly Deviation Metrics Report:
- Total deviations by classification, department, product
- Open vs. closed, aging analysis
- Repeat deviations (>2 same root cause in 12 months)
- CAPA effectiveness metrics

**5.6.2** Quarterly Management Review Presentation

---

## 6. Records
| Record | Retention | Location |
|--------|-----------|----------|
| Form-QA-001 (Deviation Report) | 1 year post expiry | QA Archive / eQMS |
| Form-QA-001B (Investigation Report) | 1 year post expiry | QA Archive / eQMS |
| CAPA Records | 1 year post expiry | CAPA System / eQMS |
| Trending Reports | 3 years | QA Archive |

---

## 7. Key Performance Indicators
| KPI | Target |
|-----|--------|
| Deviation reporting within 24h | ≥98% |
| Investigation closure on time | ≥95% |
| CAPA effectiveness verification | 100% |
| Repeat deviation rate | <2% per year |
| Critical deviation rate | <5% of total |

---

## 8. References
- 21 CFR 211.100, 211.192, 211.180
- EU GMP Chapter 8
- ICH Q10 Section 4.3
- SOP-QA-002: Material Quarantine
- SOP-QA-003: CAPA Management
- SOP-QA-004: Batch Disposition
- Form-QA-001, Form-QA-001A, Form-QA-001B
```

---

### SOP-QA-002: Material Quarantine & Release

```markdown
# SOP-QA-002: Material Quarantine, Hold, Release & Rejection

**Document Control:** SOP-QA-002 | Version 2.1 | Effective: 2026-02-01 | Approved

---

## 1. Purpose
Define the system for quarantine, hold, release, and rejection of all materials (raw, packaging, intermediates, bulk, finished) to ensure only approved materials enter production and distribution.

## 2. Scope
All materials at [Site]: Starting materials, Packaging materials, Intermediates, Bulk products, Finished products, Returned goods, Stability samples.

## 3. Status Definitions

| Status | Label Color | Definition | Authority |
|--------|-------------|------------|-----------|
| **QUARANTINE** | **YELLOW** | Received, awaiting testing/review | Warehouse/QA |
| **HOLD** | **ORANGE** | Under investigation, deviation, OOS | QA Only |
| **RELEASED** | **GREEN** | Meets all specs, approved for use/distribution | QA Only |
| **REJECTED** | **RED** | Failed specs, expired, damaged, counterfeit | QA Only |
| **RETURNED** | **BLUE** | Customer returns, field returns | QA Only |

## 2. Procedure

### 2.1 Receipt & Initial Quarantine
1. Warehouse receives material → Verify PO, COA, shipping docs
2. Apply YELLOW "QUARANTINE" label (material name, lot, qty, receipt date, PO#)
3. Store in designated QUARANTINE area (segregated, controlled)
4. Notify QA via LIMS/eQMS → QA creates sampling plan

### 2.2 Sampling & Testing
- QA issues Sampling Order (Form-QA-002) per Sampling Plan (SOP-QC-001)
- QC samples per SOP-QC-002 → Tests per specification
- Results entered in LIMS → Auto-comparison to spec

### 2.3 Disposition Decision Matrix

| Test Result | Action | Authority | Label |
|-------------|--------|-----------|-------|
| All tests PASS | RELEASE | QA Manager | GREEN "RELEASED" |
| One or more FAIL | REJECT → Investigate | QA Manager | RED "REJECTED" |
| OOS → Investigation | HOLD → Investigate | QA Manager | ORANGE "HOLD" |
| Deviation pending | HOLD | QA Manager | ORANGE "HOLD" |
| Expired retest date | REJECT or Retest | QA Manager | RED or Retest |

### 2.3 Release Process
1. QA reviews: COA, test results, COA comparison, supplier qualification, transport records
2. QA verifies: All specs met, no open deviations, supplier approved, transport OK
3. QA Manager signs Release Certificate (Form-QA-003)
4. System status → RELEASED → GREEN label applied
5. Material moved to RELEASED storage area

### 2.4 Rejection Process
1. QA issues Rejection Notice (Form-QA-004)
2. RED "REJECTED" label applied
3. Material moved to REJECTED area (locked, segregated)
4. Disposition options: Return to supplier, Destroy, Reprocess (if approved), Downgrade
4. Disposition documented, witnessed, recorded

### 2.5 Hold Management
- HOLD only by QA (Deviation, OOS, Investigation, Regulatory)
- Monthly Hold Review (Form-QA-005)
- Maximum Hold: 90 days without QA Manager extension

---

## 3. Label Specifications
| Status | Color | Text | Minimum Size | Placement |
|--------|-------|------|--------------|-----------|
| QUARANTINE | Yellow | QUARANTINE - DO NOT USE | 100x150mm | 2 opposing sides |
| HOLD | Orange | HOLD - QA ONLY | 100x150mm | 2 opposing sides |
| RELEASED | Green | RELEASED - [Date] [Initials] | 100x150mm | 2 opposing sides |
| REJECTED | Red | REJECTED - DO NOT USE | 100x150mm | 2 opposing sides |

## 4. Records
| Record | Retention | Location |
|--------|-----------|----------|
| Quarantine Log | 1 yr post expiry | LIMS/eQMS |
| Release/Rejection Certificates | 1 yr post expiry | QA Archive |
| Hold Review Records | 3 years | QA Archive |
| Sampling Orders | 1 yr post expiry | QC Archive |

---

## 4. References
- 21 CFR 211.80-211.94
- EU GMP Chapter 5
- ICH Q7 Section 7
- SOP-QA-001: Deviation Management
- SOP-QC-001: Sampling Plans
- Form-QA-002, 003, 004, 005
```

---

### SOP-QA-003: CAPA Management

```markdown
# SOP-QA-003: Corrective and Preventive Action (CAPA) Management

**Document Control:** SOP-QA-003 | Version 4.0 | Effective: 2026-03-01 | Approved

---

## 1. Purpose
Establish a systematic, risk-based approach for initiating, investigating, implementing, verifying, and closing Corrective and Preventive Actions (CAPAs) to eliminate root causes of nonconformities and prevent recurrence.

## 2. Scope
All GMP quality events: Deviations, OOS/OOT, Complaints, Audit findings, Regulatory actions, Trends, Near-misses.

## 2. CAPA Classification & Timelines

| CAPA Source | Classification | Initiation Timeline | Closure Target |
|-------------|----------------|---------------------|----------------|
| Critical Deviation | Mandatory | 5 business days | 60 business days |
| Major Deviation | Mandatory | 10 business days | 90 business days |
| Critical OOS | Mandatory | 5 business days | 60 business days |
| Critical Complaint | Mandatory | 5 business days | 60 business days |
| Audit Finding (Critical) | Mandatory | 10 business days | 90 business days |
| Audit Finding (Major) | Recommended | 30 business days | 120 business days |
| Trend Signal | Risk-based | 30 business days | 120 business days |
| Preventive Opportunity | Optional | N/A | 180 business days |

## 3. CAPA Process Flow

### 3.1 CAPA Initiation (Form-QA-006)
**Trigger Sources:** Deviation, OOS, Complaint, Audit, Trend, Regulatory, Preventive
**Required Fields:**
- Source document/reference
- Problem statement (specific, measurable)
- Risk assessment (Severity × Probability × Detectability)
- Proposed team lead
- Preliminary timeline

### 3.2 Risk Assessment (RPN)
| Factor | Scale (1-10) |
|--------|--------------|
| Severity (Patient Impact) | 1=Negligible → 10=Life-threatening |
| Probability (Occurrence) | 1=Rare → 10=Certain |
| Detectability (Current Controls) | 1=Certain detection → 10=Undetectable |
| **RPN = S × P × D** | **Threshold: ≥100 = Mandatory CAPA** |

### 3.3 Investigation & Root Cause (Form-QA-007)
**Team:** Cross-functional per expertise
**Tools:** 5 Whys, Fishbone, FTA, FMEA, Change Analysis
**Deliverable:** Root Cause Report with:
- Verified root cause(s)
- Contributing factors
- Why not detected earlier
- Impact assessment (product, batches, patients, regulatory)

### 3.4 Action Plan Development (Form-QA-008)
| Action Type | Description | Owner | Due Date | Verification Method | Effectiveness Metric |
|-------------|-------------|-------|----------|---------------------|---------------------|
| Corrective (CA) | Fix specific problem | Name/Dept | Date | How verified | Target value |
| Preventive (PA) | Prevent recurrence | Name/Dept | Date | How verified | Target value |

**Requirements:**
- CA: Specific to root cause, immediate containment if needed
- PA: Systemic, sustainable, addresses similar risks elsewhere
- Both: SMART (Specific, Measurable, Achievable, Relevant, Time-bound)

### 3.4 Implementation & Verification
1. **Implementation** - Owner executes per plan, documents evidence
2. **Interim Check** - 30/60/90 day progress review
3. **Effectiveness Verification** (Form-QA-009):
   - CA: Problem resolved? (e.g., zero recurrences in 6 months)
   - PA: Systemic change working? (e.g., metric trend improvement)
4. **Verification Evidence:** Audit results, metrics, data trends, test results

### 3.5 CAPA Closure (Form-QA-010)
**Closure Package:**
- Completed action items with evidence
- Effectiveness verification results
- Metrics demonstrating sustained improvement
- Residual risk assessment
- QA Manager approval
- Lessons learned documented

**Closure Criteria:**
- All actions completed and verified
- Effectiveness confirmed with data
- No recurrence in defined period
- QA Manager approval

---

## 4. CAPA Tracking & Metrics

### 4.1 Required Tracking Fields (CAPA System)
| Field | Description |
|-------|-------------|
| CAPA ID | Unique identifier (CAPA-YYYY-NNNN) |
| Source | Deviation/OOS/Complaint/Audit/Trend |
| Classification | Critical/Major/Minor/Preventive |
| Status | Open/In Progress/Verification/Closed/Cancelled |
| Risk Level | Critical/High/Medium/Low (RPN) |
| Owner | Name, Department |
| Due Date | Original committed date |
| Actual Closure | Date closed |
| Effectiveness | Verified/Not Verified/Partial |

### 4.2 Key Metrics (Monthly Dashboard)
| Metric | Target |
|--------|--------|
| CAPA Closure On-Time | ≥95% |
| Overdue CAPAs | 0 Critical, <5% Major |
| Effectiveness Verification Rate | 100% |
| Recurrence Rate (same root cause) | <2% |
| Average Time to Closure | Critical: <60d, Major: <90d |
| Preventive vs Corrective Ratio | >30% Preventive |

---

## 4. Records
| Record | Retention | Location |
|--------|-----------|----------|
| CAPA Initiation Form | 1 yr post closure | CAPA System |
| Root Cause Report | 1 yr post closure | CAPA System |
| Action Plan | 1 yr post closure | CAPA System |
| Verification Evidence | 1 yr post closure | CAPA System |
| Closure Approval | 1 yr post closure | CAPA System |

---

## 5. References
- 21 CFR 211.100, 211.180, 211.192
- EU GMP Chapter 8
- ICH Q10 Section 4.4
- ICH Q9 Risk Management
- PDA TR56
- SOP-QA-001: Deviation Management
- Form-QA-006, 007, 008, 009, 010
```

---

## 4. SOP Writing Best Practices

### 4.1 Writing Principles
| Principle | Application |
|-----------|-------------|
| **Imperative Mood** | "Weigh 500g" not "The operator should weigh 500g" |
| **One Action Per Step** | Each numbered step = one action |
| **Specific Values** | "Heat to 80±2°C" not "Heat to appropriate temperature" |
| **Decision Points Clear** | "IF weight >502g THEN reject" |
| **References Traceable** | "Per USP <711>" not "Per pharmacopeia" |
| **Roles Not Names** | "QC Analyst" not "John Smith" |

### 4.2 SOP Review Checklist
| Check | Pass/Fail |
|-------|-----------|
| Purpose clear and scoped? | ☐ |
| Responsibilities defined (RACI)? | ☐ |
| Procedure steps sequential, unambiguous? | ☐ |
| Decision points have clear criteria? | ☐ |
| Forms referenced by number/title? | ☐ |
| Records listed with retention? | ☐ |
| Training requirements specified? | ☐ |
| Change control referenced? | ☐ |
| Deviation handling referenced? | ☐ |
| Regulatory citations accurate? | ☐ |
| Cross-references valid? | ☐ |
| Version control complete? | ☐ |

---

## Metadata

```json
{
  "document_id": "sop_examples_pharmaceutical_qms",
  "category": "SOP_examples",
  "subcategory": "sop_templates",
  "source_type": "Compiled_Regulatory_Templates",
  "authority": "FDA/ICH/EU_GMP/PDA/ISPE",
  "version": "2026.1",
  "format": "Markdown",
  "retrieved": "2026-07-28",
  "confidence": 0.95,
  "tags": ["SOP_Templates", "Deviation_Management", "CAPA", "Material_Quarantine", "Batch_Disposition", "Change_Control", "Training", "Document_Control", "GMP_Compliance", "QMS_SOPs"]
}
```