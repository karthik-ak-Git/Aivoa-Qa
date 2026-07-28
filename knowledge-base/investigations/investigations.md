# Pharmaceutical Investigations

Last Updated: 2026-07-28

---

## 1. Overview

An investigation is a formal, systematic process to determine the root cause of a deviation, OOS result, complaint, or other quality event, and to assess the impact on product quality and patient safety.

### Types of Investigations

| Type | Trigger | Regulatory Requirement |
|---|---|---|
| Complaint Investigation | Product complaint from customer | 21 CFR 211.198 |
| OOS Investigation | Out-of-specification test result | 21 CFR 211.192, FDA OOS Guidance |
| Deviation Investigation | Departure from approved procedure | 21 CFR 211.100 |
| Adverse Event Investigation | Patient safety event | 21 CFR 314.80 |
| Recall Investigation | Product recall | 21 CFR 7 |
| Environmental Investigation | Clean room excursion | EU GMP Annex 1 |
| Stability Failure Investigation | Stability result out of specification | ICH Q1A |

---

## 2. Investigation Levels

### Phase I (Lab Investigation) — For OOS Results
**Objective**: Determine if the OOS is due to lab error.

**Activities**:
- Review calculations
- Review analyst technique
- Check instrument performance
- Review standards and reagents
- Review chromatograms/raw data
- Re-test (if lab error identified)
- If no lab error found → proceed to Phase II

### Phase II (Full-Scale Investigation)
**Objective**: Determine manufacturing root cause and product impact.

**Activities**:
- Review batch records (BPR)
- Review equipment logs
- Review environmental conditions
- Interview operators
- Review raw materials
- Review in-process controls
- Additional testing (retain samples, stability samples)
- Root cause analysis

---

## 3. Complaint Investigation Procedure

### Regulatory Requirement: 21 CFR 211.198

Each complaint must be reviewed and investigated. The written record must include:

1. Name and strength of drug product
2. Lot number
3. Name of complainant
4. Nature of complaint
5. Reply to complainant
6. Findings of investigation

### Investigation Flow

```
Complaint Received
    ↓
Initial Triage (within 24 hours)
    ↓
Severity/Risk Assessment
    ↓
Assign Investigator
    ↓
Gather Information:
- Product details
- Batch/lot number
- Complaint description
- Patient/customer information
- Photographs/retained sample
- Manufacturing batch record
    ↓
Root Cause Analysis
    ↓
Impact Assessment:
- Other batches affected?
- Patient safety
- Regulatory reporting required?
    ↓
Actions:
- Corrective actions
- Preventive actions (CAPA)
- Regulatory submission
- Recall if needed
- Customer response
    ↓
Effectiveness Check
    ↓
Closure
```

### Investigation Timeline

| Severity | Initial Assessment | Investigation Complete |
|---|---|---|
| Critical | 24 hours | 30 days |
| Major | 48 hours | 45 days |
| Moderate | 5 business days | 60 days |
| Minor | 10 business days | 90 days |

---

## 4. Root Cause Analysis Methods

### 5 Whys
Simple iterative questioning technique.

**Complaint Example**: Patient found whole tablet in stool
1. Why? → Tablet didn't dissolve
2. Why? → Dissolution failure
3. Why? → Cross-linking of gelatin capsule shell
4. Why? → Exposure to high humidity
5. Why? → Packaging moisture barrier insufficient

### Fishbone (Ishikawa) Diagram
Categories for pharmaceutical investigations:
- **Man**: Training, qualification, fatigue
- **Machine**: Calibration, maintenance, design
- **Material**: API, excipient, packaging
- **Method**: Process, parameters, SOP
- **Measurement**: Test, equipment, sampling
- **Environment**: Temperature, humidity, pressure

### Fault Tree Analysis (FTA)
Top-down approach using logic gates (AND/OR).

### Failure Mode and Effects Analysis (FMEA)
RPN = Severity × Occurrence × Detection

### Change Analysis
Examine what changed before the failure occurred.
- Material lot change
- Supplier change
- Equipment change
- Parameter change
- Operator change
- Environmental change

---

## 5. Investigation Report Template

```
TITLE: Investigation Report #[ID]

1. GENERAL INFORMATION
   Product Name:
   Batch/Lot Number:
   Complaint/Deviation ID:
   Date of Event:
   Date Investigation Initiated:
   Investigator:
   QA Oversight:

2. DESCRIPTION OF EVENT
   [Detailed description of what occurred]

3. IMMEDIATE ACTIONS TAKEN
   [Quarantine, containment, customer notification, etc.]

4. INVESTIGATION FINDINGS
   4.1 Batch Record Review:
   4.2 Equipment Review:
   4.3 Material Review:
   4.4 Personnel Review:
   4.5 Environmental Review:
   4.6 Previous Similar Events:

5. ROOT CAUSE ANALYSIS
   Method Used:
   Root Cause(s) Identified:
   Contributing Factors:

6. PRODUCT IMPACT ASSESSMENT
   [Does the event affect product quality, safety, efficacy?]
   [Are other batches affected?]
   [Is regulatory reporting required?]

7. CORRECTIVE AND PREVENTIVE ACTIONS
   Immediate Correction:
   Corrective Action:
   Preventive Action:
   CAPA Reference #:

8. REGULATORY REPORTING
   [21 CFR 314.80, 21 CFR 7 recall, etc.]

9. CONCLUSION
   [Summary of findings and final outcome]

10. ATTACHMENTS
    [Batch records, photos, test results, etc.]

11. APPROVALS
    Investigator: ________________ Date: ______
    QA Review: __________________ Date: ______
    Site QA Head: _______________ Date: ______
```

---

## 6. Regulatory Reporting Requirements

### Adverse Events (21 CFR 314.80)
| Event Type | Report Type | Timeline |
|---|---|---|
| Serious + Unexpected | 15-Day Alert Report | 15 days |
| Serious + Expected | Periodic Report | Quarterly (3 years) then annually |
| Non-Serious | Periodic Report | Annual |
| Follow-up to 15-Day | Follow-up Report | 15 days |

### Recalls (21 CFR 7)
| Class | Definition | Examples |
|---|---|---|
| Class I | Reasonable probability of serious adverse health consequences | Contaminated sterile product |
| Class II | May cause temporary or medically reversible health consequences | Subpotent drug |
| Class III | Not likely to cause adverse health consequences | Minor labeling violation |

### Medical Device Reports (21 CFR 803)
- Applicable for combination products
- 30-day, 5-day, and 10-day reporting

---

## 7. Investigation Documentation Best Practices

### DOs
- Document contemporaneously (at time of investigation)
- Include all raw data and evidence
- Use objective language (facts, not opinions)
- Document negative findings (what was ruled out)
- Include photographs of defects
- Reference all source documents
- Complete all sections

### DON'Ts
- Do not delay documentation
- Do not speculate without evidence
- Do not blame individuals (focus on system/process)
- Do not close investigation before root cause is confirmed
- Do not leave gaps in chronology
- Do not use vague language ("possibly", "maybe")

---

## 8. Common Investigation Pitfalls

| Pitfall | Impact | How to Avoid |
|---|---|---|
| Superficial RCA | Issue recurs | Use structured tools (5 Whys, Fishbone) |
| Confirmation bias | Wrong root cause | Consider multiple hypotheses |
| Blaming operator | System issues missed | Look for system/process root causes |
| Premature closure | Root cause missed | Verify root cause with data |
| Inadequate scope | Similar products/lines not checked | Extend investigation to other products |
| Missing effectiveness check | CAPA fails to prevent recurrence | Define measurable effectiveness criteria |

**Sources**: 21 CFR 211.198, FDA OOS Guidance (2006), ICH Q9, ICH Q10, ISPE, PDA
