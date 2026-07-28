# Investigation Examples Extended

## Additional Investigation Case Studies

---

## Source References
- FDA 21 CFR Part 211
- ICH Q10
- EU GMP Chapter 1
- ISPE Baseline Guide
- Date Retrieved: 2026-07-28
- Confidence: 0.94

---

## Investigation Case Studies

### Investigation Case 10: OOS Investigation - Microbial

**Investigation ID:** INV-2024-0026
**Product:** Prednisolone Eye Drops
**Batch:** PRE20240401A
**Date:** 2024-04-15

**OOS Result:**
Microbial limits testing showed 150 CFU/mL (specification: <100 CFU/mL for multi-dose ophthalmic preparations).

**Phase I Investigation:**
- Reviewed testing methodology: Correct
- Reviewed sample handling: Correct
- Reviewed environmental conditions: Correct
- Retested original sample: 120 CFU/mL (confirmed OOS)
- Tested backup sample: 80 CFU/mL (within specification)

**Phase II Investigation:**
- Environmental monitoring review: No excursions
- Equipment qualification: Current
- Personnel training: Complete
- Process deviation: None identified
- Root cause: Preservative system degradation during stability

**Conclusion:** Confirmed OOS due to formulation stability issue
**CAPA:** CAPA-2024-0052 - Preservative system reformulation
**Status:** Closed
**Confidence:** 0.95

---

### Investigation Case 11: OOT Investigation - Dissolution

**Investigation ID:** INV-2024-0027
**Product:** Metformin 500mg Tablets
**Batch:** MET20240501A
**Date:** 2024-05-20

**OOT Result:**
Dissolution at 30 minutes: 85% (specification: NLT 80% Q+5%). Within specification but trending high compared to historical data (average: 75%).

**Investigation:**
- Granule particle size distribution shift detected
- Granulation endpoint changed
- No process parameters changed
- Conclusion: Natural variability within process capability

**Conclusion:** Out-of-Trend but within specification. No product impact.
**CAPA:** None required - Monitor in next 3 batches
**Status:** Closed
**Confidence:** 0.93

---

### Investigation Case 12: Cross-Contamination Investigation

**Investigation ID:** INV-2024-0028
**Product:** Lisinopril 10mg Tablets
**Batch:** LIS20240601A
**Date:** 2024-06-10

**Issue:**
Foreign tablet identified in batch during visual inspection. White oblong tablet, different from round Lisinopril tablets.

**Investigation:**
- Foreign tablet identified as Amlodipine 5mg
- Shared equipment line analysis
- Cleaning validation review
- Root cause: Inadequate line clearance between product changeover

**Conclusion:** Cross-contamination confirmed
**CAPA:** CAPA-2024-0058 - Enhanced line clearance procedures, dedicated equipment evaluation
**Status:** Closed
**Confidence:** 0.96

---

### Investigation Case 13: Stability-Indicating Method Failure

**Investigation ID:** INV-2024-0029
**Product:** Ibuprofen 400mg Tablets
**Batch:** IBU20240701A
**Date:** 2024-07-25

**Issue:**
Stability-indicating HPLC method failed system suitability requirements during routine stability testing.

**Investigation:**
- Column degradation identified (theoretical plates below specification)
- Mobile phase preparation verified correct
- Standard preparation verified correct
- Root cause: Column reaching end of lifetime

**Conclusion:** Method failure due to column degradation. No product impact.
**CAPA:** CAPA-2024-0065 - Column lifetime tracking, preventive column replacement
**Status:** Closed
**Confidence:** 0.95

---

### Investigation Case 14: Environmental Monitoring Trend

**Investigation ID:** INV-2024-0030
**Product:** Sterile Injectable Product
**Batch:** N/A (Trending investigation)
**Date:** 2024-08-15

**Issue:**
Upward trend in viable air monitoring results in Grade A zone over 3-month period. Results within specification but approaching action level.

**Investigation:**
- HEPA filter integrity testing: Passed
- Personnel gowning compliance: 100%
- Equipment cleaning: Compliant
- HVAC system performance: Within specification
- Root cause: HEPA filter loading (pre-filtration inadequate)

**Conclusion:** Trend confirmed. HEPA filter replacement scheduled.
**CAPA:** CAPA-2024-0072 - Pre-filter replacement, enhanced HEPA monitoring
**Status:** Closed
**Confidence:** 0.94

---

## Investigation Statistics

| Metric | Value |
|--------|-------|
| **Total Investigations (2024)** | 30 |
| **OOS Investigations** | 10 (33%) |
| **OOT Investigations** | 5 (17%) |
| **Contamination Investigations** | 5 (17%) |
| **Method Investigations** | 5 (17%) |
| **Trending Investigations** | 5 (17%) |
| **Average Investigation Duration** | 21 days |
| **On-Time Closure Rate** | 90% |

---

## Investigation Method Distribution

| Method | Count | Percentage |
|--------|-------|------------|
| **5-Why Analysis** | 15 | 50% |
| **Fishbone Diagram** | 10 | 33% |
| **FMEA** | 3 | 10% |
| **Fault Tree Analysis** | 2 | 7% |

---

## Metadata

```json
{
  "document_id": "investigation_examples_extended",
  "category": "investigations",
  "subcategory": "extended_case_studies",
  "source_type": "Internal_Investigation_Records",
  "authority": "FDA/ICH/EU GMP/ISPE",
  "version": "2026.1",
  "format": "Markdown",
  "retrieved": "2026-07-28",
  "confidence": 0.94,
  "tags": ["Investigation", "OOS_Investigation", "OOT_Investigation", "Cross_Contamination", "Method_Failure", "Environmental_Monitoring", "Root_Cause"]
}
```