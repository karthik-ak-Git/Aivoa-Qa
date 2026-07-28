# Deviation Examples Extended

## Additional Deviation Case Studies

---

## Source References
- FDA 21 CFR Part 211
- ICH Q10
- EU GMP Chapter 1
- Date Retrieved: 2026-07-28
- Confidence: 0.94

---

## Deviation Case Studies

### Deviation Case 10: Environmental Excursion

**Deviation ID:** DEV-2024-0046
**Product:** Sterile Injectable Product
**Batch:** STL20240401A
**Date:** 2024-04-10

**Description:**
Cleanroom temperature excursion detected during aseptic filling operation. Temperature exceeded 22°C limit for 15 minutes (recorded 23.5°C).

**Immediate Actions:**
1. Halted filling operation
2. Notified QA and Environmental Monitoring team
3. Isolated affected batch
4. Documented excursion in batch record

**Investigation:**
- AHU cooling coil malfunction detected
- Maintenance team dispatched immediately
- Temperature returned to within specification after 15 minutes
- No product exposure during excursion (filling not started)

**Root Cause:** Equipment failure (AHU cooling coil)
**Classification:** Major
**CAPA:** CAPA-2024-0051 - Enhanced HVAC monitoring, redundant cooling system
**Status:** Closed
**Confidence:** 0.94

---

### Deviation Case 11: Batch Record Error

**Deviation ID:** DEV-2024-0047
**Product:** Omeprazole 20mg Capsules
**Batch:** OME20240501A
**Date:** 2024-05-15

**Description:**
Operator transposed digits in batch record during weight check documentation. Recorded 250.3g instead of 253.0g.

**Immediate Actions:**
1. Documented correction in batch record per SOP
2. Verified actual weight from balance printout
3. Notified QA for deviation assessment
4. No product impact (correct weight used for calculation)

**Investigation:**
- Human error during manual transcription
- Balance printout available for verification
- No calculation impact (weight not used in critical calculation)

**Root Cause:** Human error (Man)
**Classification:** Minor
**CAPA:** CAPA-2024-0057 - Enhanced batch record training, electronic batch record evaluation
**Status:** Closed
**Confidence:** 0.96

---

### Deviation Case 12: Raw Material Rejection

**Deviation ID:** DEV-2024-0048
**Product:** Ibuprofen 400mg Tablets
**Batch:** IBU20240601A
**Date:** 2024-06-20

**Description:**
Incoming raw material (Ibuprofen API) failed identification testing. FTIR spectrum did not match reference standard.

**Immediate Actions:**
1. Quarantined rejected lot
2. Notified supplier
3. Placed order hold on supplier
4. Initiated deviation investigation

**Investigation:**
- API confirmed as Ibuprofen USP grade
- Supplier shipped correct product
- Root cause: Reference standard expired and not replaced
- New reference standard obtained, re-testing confirmed identity

**Root Cause:** Reference standard management (Measurement)
**Classification:** Major
**CAPA:** CAPA-2024-0063 - Reference standard tracking system, automated expiry alerts
**Status:** Closed
**Confidence:** 0.95

---

### Deviation Case 13: In-Process Control Failure

**Deviation ID:** DEV-2024-0049
**Product:** Metformin 500mg Tablets
**Batch:** MET20240701A
**Date:** 2024-07-15

**Description:**
Tablet weight variation exceeded specification during compression. Individual tablet weights ranged from 485mg to 540mg (specification: 500mg ± 5%).

**Immediate Actions:**
1. Stopped compression operation
2. Segregated affected tablets
3. Notified QA and Production management
4. Initiated investigation

**Investigation:**
- Granule flowability issues detected
- Granule moisture content at lower specification limit
- Compression force inconsistent due to granule density variation

**Root Cause:** Granulation process variability (Method, Material)
**Classification:** Major
**CAPA:** CAPA-2024-0070 - Granulation process optimization, real-time weight monitoring
**Status:** Closed
**Confidence:** 0.94

---

### Deviation Case 14: Packaging Material Defect

**Deviation ID:** DEV-2024-0050
**Product:** Atorvastatin 10mg Tablets
**Batch:** ATV20240801A
**Date:** 2024-08-25

**Description:**
Blister foil showed pinholes during visual inspection. Affected blisters exhibited loss of moisture barrier protection.

**Immediate Actions:**
1. Segregated affected blister rolls
2. Halted packaging operation
3. Notified QA and Packaging Engineering
4. Initiated investigation

**Investigation:**
- Pinholes confirmed on 3% of blister rolls
- Root cause: Foil supplier manufacturing defect
- Supplier investigation ongoing

**Root Cause:** Supplier material defect (Material)
**Classification:** Major
**CAPA:** CAPA-2024-0077 - Enhanced incoming inspection, supplier quality agreement update
**Status:** Closed
**Confidence:** 0.95

---

## Deviation Statistics Summary

| Metric | Value |
|--------|-------|
| **Total Deviations (2024)** | 50 |
| **Critical Deviations** | 5 (10%) |
| **Major Deviations** | 25 (50%) |
| **Minor Deviations** | 20 (40%) |
| **Average Closure Time** | 28 days |
| **On-Time Closure Rate** | 94% |
| **Recurrence Rate** | 4% |

---

## Root Cause Distribution

| Category | Count | Percentage |
|----------|-------|------------|
| **Man** | 12 | 24% |
| **Machine** | 8 | 16% |
| **Material** | 10 | 20% |
| **Method** | 10 | 20% |
| **Environment** | 4 | 8% |
| **Measurement** | 4 | 8% |
| **Management** | 2 | 4% |

---

## Metadata

```json
{
  "document_id": "deviation_examples_extended",
  "category": "deviations",
  "subcategory": "extended_case_studies",
  "source_type": "Internal_Deviation_Records",
  "authority": "FDA/ICH/EU GMP",
  "version": "2026.1",
  "format": "Markdown",
  "retrieved": "2026-07-28",
  "confidence": 0.94,
  "tags": ["Deviation", "Case_Studies", "Environmental_Excursion", "Batch_Record_Error", "Raw_Material", "In_Process_Control", "Packaging_Defect", "Root_Cause"]
}
```