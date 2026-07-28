# Deviations in Pharmaceutical Manufacturing

Last Updated: 2026-07-28

---

## 1. Definition

A deviation is a departure from an approved instruction, procedure, established standard, or specification.

In pharmaceutical GMP, deviations must be documented, investigated, and resolved according to written procedures.

**Regulatory Basis**: 21 CFR 211.100, ICH Q7 Section 2.3, ICH Q10

---

## 2. Types of Deviations

### By Intent

| Type | Description | Examples |
|---|---|---|
| Planned Deviation | A known, intentional temporary departure from the approved procedure (also called "temporary change" or "concession") | Operating at alternate parameter while equipment is repaired |
| Unplanned Deviation | An unexpected departure from the approved procedure | Operator error, equipment failure, material issue |

### By Severity (Risk-Based)

| Class | Description | Examples | Action Required |
|---|---|---|---|
| Critical | Affects product quality, patient safety, or regulatory compliance | Sterility breach, potency failure | Full investigation, CAPA, possible recall |
| Major | May affect product quality but is unlikely to impact patient safety | Weight variation trending, minor equipment issue | Investigation, CAPA |
| Minor | Unlikely to affect product quality | Documentation error, non-significant parameter deviation | Investigation, corrective action (CAPA may not be needed) |

### By Origin

| Type | Description |
|---|---|
| Process Deviation | Related to manufacturing parameters |
| Equipment Deviation | Equipment malfunction or failure |
| Material Deviation | Raw material, excipient, or packaging component issue |
| Environmental Deviation | Clean room environment out of specification |
| Procedural Deviation | Failure to follow SOP / work instruction |
| Documentation Deviation | Error in records, BPR, or logs |
| Analytical Deviation | Lab / QC test procedure deviation |
| Utility Deviation | HVAC, WFI, compressed air deviation |
| Personnel Deviation | Operator error or procedural violation |
| System Deviation | Computer system, LIMS, MES issue |

---

## 3. Deviation Management Process

### Step 1: Identification & Documentation
- Identify deviation during manufacturing or review
- Document immediately on deviation form or electronic system
- Segregate affected material (quarantine)
- Initial assessment of impact

### Step 2: Classification
- Assign severity (Critical, Major, Minor)
- Determine if immediate action is needed
- Notify Quality Unit

### Step 3: Investigation
- Assemble investigation team
- Gather all relevant data (batch records, logs, charts, samples)
- Perform root cause analysis
- Determine product impact
- Document findings

### Step 4: Impact Assessment
- Product quality impact (release decision)
- Patient safety impact
- Regulatory compliance impact
- Other batches potentially affected
- Other products potentially affected

### Step 5: Corrective Action
- Immediate correction (disposition of affected material)
- Corrective action (address root cause)
- Preventive action (prevent recurrence)

### Step 6: Disposition
- Determine fate of affected product/batch:
  - **Release**: Quality acceptable
  - **Rework**: Corrective processing (if allowed)
  - **Reject**: Dispose or destroy
  - **Return to Supplier**: If raw material issue

### Step 7: Closure
- Complete all actions
- Review effectiveness
- Approve closure by QA

---

## 4. Common Deviation Examples

### Example 1: Temperature Excursion During Manufacturing
| Element | Content |
|---|---|
| Description | Fluid bed dryer inlet temperature reached 62°C (spec: 55±3°C) for 4 minutes due to control valve failure |
| Classification | Major |
| Product Impact | Sample tested: moisture content within spec, impurity profile unchanged. Batch released with investigation. |
| Root Cause | Pneumatic control valve failed due to debris in instrument air line |
| Corrective Action | Valve cleaned, instrument air filter replaced |
| Preventive Action | Preventive maintenance frequency for control valves revised. Instrument air quality monitoring added. |

### Example 2: Hold Time Exceeded
| Element | Content |
|---|---|
| Description | Wet granules held 8 hours instead of maximum 6 hours before drying step |
| Classification | Major |
| Product Impact | Microbial testing performed. Results within spec. Batch released. |
| Root Cause | Operator scheduled for lunch break did not resume process. No handover communication. |
| Corrective Action | Batch hold time monitoring system (timer) implemented in MES |
| Preventive Action | Shift handover SOP revised to include hold time status |

### Example 3: Label Misalignment
| Element | Content |
|---|---|
| Description | Label applied 3mm below specification position on one bottle in visual inspection |
| Classification | Minor |
| Product Impact | Corrected immediately. All bottles from same run re-inspected. No further issues. |
| Root Cause | Label sensor temporarily out of alignment |
| Corrective Action | Sensor re-aligned |
| Preventive Action | Sensor alignment added to preventive maintenance checklist |

---

## 5. Deviation Investigation Methodology

### Data to Collect
- Batch records (BPR/BMR)
- Equipment logs
- Operator statements
- Training records
- Previous similar deviations
- Environmental monitoring data
- In-process control data
- Quality control test results
- Equipment calibration/maintenance records
- Material certificates of analysis (COAs)

### Common Root Causes by Category

| Category | Common Root Causes |
|---|---|
| Human Error | Lack of training, fatigue, unclear procedure, distraction, workload |
| Equipment | Calibration drift, wear and tear, design flaw, maintenance failure |
| Material | Supplier change, batch-to-batch variability, degradation |
| Method | Inadequate SOP, ambiguous instruction, insufficient detail |
| Environment | Temperature excursion, humidity, pressure differential failure |
| Measurement | Test method variability, equipment sensitivity, sampling error |

---

## 6. Deviation Trending

### Metrics to Track
| Metric | Description |
|---|---|
| Deviation Rate | Deviations per batch or per month |
| Top Deviation Types | Most frequent deviations (Pareto analysis) |
| Deviation Closure Time | Average time to close |
| Repeat Deviations | Same deviation occurring again after CAPA |
| Deviation by Area | Manufacturing area with most deviations |
| Deviation by Shift | Shift/team with most deviations |

### Trending Analysis Goals
- Identify systemic issues
- Target CAPA effectiveness
- Improve process robustness
- Support Annual Product Review (APR)
- Identify training gaps

---

## 7. Regulatory References

| Requirement | Description |
|---|---|
| 21 CFR 211.100 | Written procedures for production and process control; deviations must be justified and documented |
| 21 CFR 211.192 | Production record review; unexplained discrepancies must be investigated |
| ICH Q7 Section 2.3 | Deviations from established procedures should be documented and explained |
| ICH Q10 Section 3.2.1 | System for monitoring process performance and product quality |
| ICH Q10 Section 3.2.2 | CAPA system; corrective and preventive actions resulting from deviation investigations |
| EU GMP Chapter 1 | Quality management system; deviation handling |
| EU GMP Chapter 4 | Documentation; deviation documentation requirements |

**Sources**: 21 CFR 211, ICH Q7, ICH Q10, EU GMP, ISPE, PDA
