# Investigation Management Knowledge Base

## Comprehensive Investigation Reference for Pharmaceutical Quality Events

---

## Source References
- FDA 21 CFR 211.192, 211.198, 211.180
- EU GMP Chapter 8, Annex 15
- ICH Q10 Section 4.3 (Quality Events)
- ICH Q9 Quality Risk Management
- FDA Guidance: Investigating Out-of-Specification (OOS) Test Results
- PDA Technical Report 71 - Root Cause Analysis
- ASQ Quality Tools
- Date Retrieved: 2026-07-28
- Confidence: 0.95

---

## 1. Investigation Types & Triggers

### 1.1 Laboratory Investigations
| Trigger | Investigation Type | Regulatory Reference |
|---------|-------------------|---------------------|
| **OOS (Out of Specification)** | Phase 1 (Lab) → Phase 2 (Full Scale) | FDA OOS Guidance, 21 CFR 211.165 |
| **OOT (Out of Trend)** | Trend investigation, pattern analysis | ICH Q10, USP <1010> |
| **OOE (Out of Expectation)** | Unexpected result vs prediction | Internal SOP |
| **Laboratory Error** | Analyst, instrument, method, reagent | 21 CFR 211.160 |
| **Stability Failure** | Out-of-spec at stability timepoint | ICH Q1A, 21 CFR 211.166 |

### 1.2 Manufacturing Investigations
| Trigger | Investigation Type |
|---------|-------------------|
| **Process Deviation** | Parameter excursion, procedural error |
| **Equipment Failure** | Malfunction, calibration drift, breakdown |
| **Material Issue** | Wrong material, quality defect, mix-up |
| **Contamination** | Cross-contamination, microbial, particulate |
| **Packaging Error** | Wrong label, count, seal, code |

### 1.3 Quality Event Investigations
| Trigger | Investigation Type |
|---------|-------------------|
| **Customer Complaint** | Product defect, ADR, packaging defect |
| **Audit Finding** | Internal, vendor, regulatory |
| **Regulatory Action** | 483, Warning Letter, Import Alert |
| **Recall** | Class I, II, III, Market Withdrawal |
| **Near Miss** | Potential quality event intercepted |

---

## 2. OOS Investigation Framework (FDA Guidance)

### Phase 1: Laboratory Investigation (Within 24-48 hours)
| Step | Activity | Documentation |
|------|----------|---------------|
| **1.1** | Verify result accuracy (re-read, re-calculate) | Raw data, chromatograms, calculations |
| **1.2** | Check instrument performance (system suitability) | System suitability records |
| **1.3** | Review analytical method compliance | Method SOP, validation |
| **1.4** | Check reagent/standard integrity | COA, preparation records |
| **1.5** | Assess analyst technique/training | Training records, observation |
| **1.5** | Document all findings | Phase 1 Report |

**Phase 1 Outcome**: Assignable lab error? → Document, retest per SOP. No lab error? → Proceed to Phase 2.

### Phase 2: Full-Scale Investigation (Within 30 days)
| Step | Activity | Documentation |
|------|----------|---------------|
| **2.1** | Review manufacturing records for batch | BMR, BPR, IPC, deviations |
| **2.5** | Review material records | COA, dispensing, storage |
| **2.3** | Review equipment/environmental records | Logs, calibration, environmental monitoring |
| **2.4** | Laboratory retesting (per written protocol) | Retest protocol, results, statistical evaluation |
| **2.5** | Additional testing if warranted | Extended impurity profile, forced degradation |
| **2.6** | Root cause determination | RCA report, CAPA linkage |
| **2.7** | Batch disposition decision | Release, rework, reject with rationale |

### Phase 2 Retesting Requirements
| Requirement | Detail |
|-------------|--------|
| **Protocol** | Pre-approved, statistically sound |
| **Sample** | Original sample (if adequate) + reserve samples |
| **Replicates** | Minimum n=3 (original + 2) for assay; n=6 for content uniformity |
| **Acceptance** | All results within specification |
| **Statistics** | Mean, SD, %RSD, confidence intervals |
| **Invalidation** | Original result invalidated ONLY with documented lab error |

---

## 3. Root Cause Analysis Methodologies

### 3.1 Tool Selection Guide
| Situation | Recommended Tool(s) |
|-----------|---------------------|
| Simple linear cause chain | 5 Whys |
| Multiple potential causes | Fishbone (Ishikawa) |
| Complex system failure | Fault Tree Analysis (FTA) |
| Proactive process risk | FMEA |
| Prioritizing multiple causes | Pareto Analysis |
| Change-related deviation | Change Analysis |
| Safety/barrier failure | Barrier Analysis |
| Human error focus | HFACS / HEART |

### 3.2 5 Whys Template
```
Problem: [Clear problem statement]
Why 1: [Answer] → Why?
Why 2: [Answer] → Why?
Why 3: [Answer] → Why?
Why 4: [Answer] → Why?
Why 5: [Answer] → Root Cause
```

### 3.3 Fishbone (6M) Categories
```
                    Problem
                        |
        +---------------+---------------+---------------+
        |               |               |               |
   Man (People)   Machine        Material      Method
        |               |               |               |
   +----+----+     +----+----+     +----+----+     +----+----+
   |         |     |         |     |         |     |         |
Training  Skill   Calibrat. Wear    Identity Purity   Procedure Doc
Fatigue   Superv. Mainten. Age     Supplier Spec     Change  Valid
```

### 3.4 Human Error Classification (HFACS)
| Level | Category | Examples |
|-------|----------|----------|
| **Level 1** | Unsafe Acts | Slips, lapses, mistakes, violations |
| **Level 2** | Preconditions | Fatigue, stress, poor lighting, inadequate training |
| **Level 3** | Supervisory | Inadequate oversight, failed to correct known problem |
| **Level 4** | Organizational | Culture, resources, policies, scheduling |

---

## 4. Investigation Report Structure

### 4.1 Standard Investigation Report Sections
| Section | Content |
|---------|---------|
| **1. Executive Summary** | Problem, root cause, impact, disposition, CAPA summary |
| **2. Event Description** | What, when, where, who, how detected |
| **3. Immediate Actions** | Containment, quarantine, notifications |
| **4. Investigation Scope** | Batches, products, sites, time period |
| **5. Data Collection** | Documents reviewed, interviews, testing |
| **6. Root Cause Analysis** | Method used, analysis, root cause statement |
| **7. Contributing Factors** | Systemic issues, latent conditions |
| **8. Impact Assessment** | Product quality, patient safety, regulatory, business |
| **9. Batch/Material Disposition** | Release, rework, reject with rationale |
| **10. Corrective Actions** | Specific, measurable, owner, due date |
| **11. Preventive Actions (CAPA)** | Systemic, effectiveness verification |
| **12. Regulatory Assessment** | Field alert, recall, notification requirements |
| **12** | Effectiveness Verification Plan | Metrics, timeline, verification method |
| **14. Closure** | QA approval, date, lessons learned |

### 4.2 Root Cause Statement Formula
> **Root Cause = [Specific Failure] + [Underlying Systemic Gap]**
>
> *Example*: "The tablet weight variation was caused by worn compression tooling (upper punch tip erosion) due to the absence of a predictive maintenance program for compression tooling life monitoring."

---

## 5. Investigation Timelines

| Investigation Type | Target Completion | Regulatory Driver |
|-------------------|-------------------|-------------------|
| **OOS Phase 1** | 24-48 hours | FDA OOS Guidance |
| **OOS Phase 2** | 30 calendar days | FDA OOS Guidance |
| **Complaint Investigation** | 30 calendar days | 21 CFR 211.198 |
| **Deviation Investigation** | Critical: 30d, Major: 60d, Minor: 90d | Internal SOP |
| **Audit Finding Response** | 15-30 business days | FDA/EMA requirement |
| **Regulatory Action Response** | 15 business days | FDA Warning Letter |
| **Recall Investigation** | Immediate initiation | 21 CFR 7.40 |

---

## 6. Common Investigation Pitfalls

| Pitfall | Prevention |
|---------|------------|
| **Shallow RCA** (symptom as cause) | Use structured tools, ask "why" until systemic gap found |
| **Blaming human error** | Focus on system gaps enabling error (training, design, procedure) |
| **Incomplete scope** | Define scope upfront, include all potentially affected batches |
| **Inadequate documentation** | Real-time documentation, evidence retention |
| **Confirmation bias** | Independent reviewer, challenge assumptions |
| **Missing batch impact** | Systematic batch traceability review |
| **Delayed initiation** | Automated alerts, clear escalation paths |
| **No effectiveness check** | Built-in verification with metrics and timeline |

---

## 7. Investigation Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **RCA Depth** | >90% systemic root causes | QA review of closed investigations |
| **Timeliness** | 100% within target | Tracking system |
| **Repeat Investigations** | <10% same root cause/year | Trending analysis |
| **Regulatory Findings** | 0 investigation-related 483s | Inspection history |
| **CAPA Conversion** | >80% Major/Critical → CAPA | CAPA tracking |
| **Batch Impact Accuracy** | 100% correct scope | QA audit of investigations |
| **Documentation Completeness** | 100% sections complete | Template compliance audit |

---

## 8. Cross-Functional Investigation Team Roles

| Role | Responsibilities |
|------|------------------|
| **Investigation Lead (QA)** | Own process, ensure timelines, coordinate team, final report |
| **Subject Matter Expert** | Technical knowledge (process, analytical, equipment) |
| **Production Representative** | Operational context, batch records, operator interviews |
| **Engineering/Maintenance** | Equipment history, calibration, failure modes |
| **Regulatory Affairs** | Reporting obligations, regulatory strategy |
| **Quality Control** | Laboratory perspective, retesting, method review |
| **Statistical Support** | Data analysis, retest protocol design, significance testing |

---

## Metadata

```json
{
  "document_id": "investigation_management_kb",
  "category": "investigations",
  "subcategory": "investigation_management",
  "source_type": "Compiled_Regulatory_Technical_Reference",
  "authority": "FDA/EMA/ICH/PDA/ASQ",
  "version": "2026.1",
  "format": "Markdown",
  "retrieved": "2026-07-28",
  "confidence": 0.95,
  "tags": ["Investigation_Management", "OOS_Investigation", "Root_Cause_Analysis", "FDA_OOS_Guidance", "Phase_1_Phase_2", "Fishbone", "5_Whys", "Human_Error", "Batch_Disposition", "Pharmaceutical_QMS", "ICH_Q10", "21_CFR_211", "EU_GMP"]
}
```