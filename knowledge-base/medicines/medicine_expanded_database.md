# Medicine Expanded Database

## Extended Product Master Data

---

## Source References
- FDA Orange Book
- DailyMed
- OpenFDA
- DrugBank
- Date Retrieved: 2026-07-28
- Confidence: 0.94

---

## Additional Medicines

### 1. Cardiovascular Products

| Product | Generic Name | Strength | Dosage Form | Route | Manufacturer |
|---------|--------------|----------|-------------|-------|--------------|
| **Plavix** | Clopidogrel Bisulfate | 75mg | Tablet | Oral | Sanofi/Bristol-Myers Squibb |
| **Eliquis** | Apixaban | 5mg | Tablet | Oral | Bristol-Myers Squibb/Pfizer |
| **Xarelto** | Rivaroxaban | 20mg | Tablet | Oral | Janssen Pharmaceuticals |
| **Symbicort** | Budesonide/Formoterol | 160/4.5mcg | Inhalation Aerosol | Inhalation | AstraZeneca |
| **Entresto** | Sacubitril/Valsartan | 97/103mg | Tablet | Oral | Novartis |

### 2. Endocrine Products

| Product | Generic Name | Strength | Dosage Form | Route | Manufacturer |
|---------|--------------|----------|-------------|-------|--------------|
| **Januvia** | Sitagliptin | 100mg | Tablet | Oral | Merck |
| **Jardiance** | Empagliflozin | 10mg | Tablet | Oral | Boehringer Ingelheim |
| **Ozempic** | Semaglutide | 1mg | Injection | SC | Novo Nordisk |
| **Trulicity** | Dulaglutide | 1.5mg | Injection | SC | Eli Lilly |
| **Mounjaro** | Tirzepatide | 5mg | Injection | SC | Eli Lilly |

### 3. Oncology Products

| Product | Generic Name | Strength | Dosage Form | Route | Manufacturer |
|---------|--------------|----------|-------------|-------|--------------|
| **Keytruda** | Pembrolizumab | 100mg/4mL | Injection | IV | Merck |
| **Opdivo** | Nivolumab | 100mg/10mL | Injection | IV | Bristol-Myers Squibb |
| **Imbruvica** | Ibrutinib | 140mg | Capsule | Oral | Pharmacyclics/Janssen |
| **Ibrance** | Palbociclib | 125mg | Capsule | Oral | Pfizer |
| **Revlimid** | Lenalidomide | 25mg | Capsule | Oral | Bristol-Myers Squibb |

### 4. Immunology Products

| Product | Generic Name | Strength | Dosage Form | Route | Manufacturer |
|---------|--------------|----------|-------------|-------|--------------|
| **Humira** | Adalimumab | 40mg/0.8mL | Injection | SC | AbbVie |
| **Enbrel** | Etanercept | 50mg/mL | Injection | SC | Amgen/Pfizer |
| **Remicade** | Infliximab | 100mg | Powder for Injection | IV | Janssen |
| **Stelara** | Ustekinumab | 45mg/0.5mL | Injection | SC | Janssen |
| **Cosentyx** | Secukinumab | 150mg/mL | Injection | SC | Novartis |

### 5. CNS Products

| Product | Generic Name | Strength | Dosage Form | Route | Manufacturer |
|---------|--------------|----------|-------------|-------|--------------|
| **Xanax** | Alprazolam | 0.5mg | Tablet | Oral | Pfizer |
| **Lexapro** | Escitalopram | 10mg | Tablet | Oral | Allergan |
| **Gabapentin** | Gabapentin | 300mg | Capsule | Oral | Various |
| **Pregabalin** | Pregabalin | 75mg | Capsule | Oral | Pfizer |
| **Duloxetine** | Duloxetine | 30mg | Capsule | Oral | Eli Lilly |

---

## Common Defect Patterns by Therapeutic Category

### 1. Cardiovascular Products

| Defect Type | Frequency | Severity | Root Cause |
|-------------|-----------|----------|------------|
| **Tablet Capping** | Medium | Major | Compression force too high |
| **Content Uniformity** | Low | Critical | Blending insufficient |
| **Dissolution Failure** | Low | Critical | Granulation variability |
| **Moisture Uptake** | Medium | Major | Packaging insufficient |

### 2. Endocrine Products

| Defect Type | Frequency | Severity | Root Cause |
|-------------|-----------|----------|------------|
| **Peeling/Chipping** | Medium | Major | Tablet hardness too low |
| **Weight Variation** | Low | Critical | Granulation flow |
| **Color Variation** | Low | Major | API degradation |
| **Injection Site Reaction** | Medium | Major | Formulation pH |

### 3. Oncology Products

| Defect Type | Frequency | Severity | Root Cause |
|-------------|-----------|----------|------------|
| **Particulate Matter** | Low | Critical | Contamination |
| **Potency Variation** | Low | Critical | API degradation |
| **Container Closure** | Low | Critical | Seal integrity |
| **Precipitation** | Low | Critical | Formulation stability |

---

## Product Stability Profiles

### Stability Conditions (ICH)

| Condition | Temperature | Humidity | Duration | Testing |
|-----------|-------------|----------|----------|---------|
| **Long-term** | 25°C ± 2°C | 60% ± 5% RH | 12-60 months | Every 6 months |
| **Intermediate** | 30°C ± 2°C | 65% ± 5% RH | 12 months | Every 6 months |
| **Accelerated** | 40°C ± 2°C | 75% ± 5% RH | 6 months | Every 3 months |

### Stability Endpoints

| Test | Method | Acceptance Criteria | Frequency |
|------|--------|---------------------|-----------|
| **Appearance** | Visual | No change from initial | Every time point |
| **Assay** | HPLC | 90-110% of label claim | Every time point |
| **Dissolution** | USP apparatus | ≥ Q+5% | Every time point |
| **Related Substances** | HPLC | Individual ≤ 0.5%, Total ≤ 2.0% | Every time point |
| **Water Content** | Karl Fischer | ≤ specification limit | Every time point |
| **Microbial Limits** | USP <61>/<62> | Meets specifications | Every time point |

---

## Metadata

```json
{
  "document_id": "medicine_expanded_database",
  "category": "medicines",
  "subcategory": "extended_product_data",
  "source_type": "FDA_OpenFDA_DailyMed_DrugBank",
  "authority": "FDA/OpenFDA/DailyMed/DrugBank",
  "version": "2026.1",
  "format": "Markdown",
  "retrieved": "2026-07-28",
  "confidence": 0.94,
  "tags": ["Medicines", "Product_Database", "Cardiovascular", "Endocrine", "Oncology", "Immunology", "CNS", "Stability", "Defect_Patterns", "Therapeutic_Categories"]
}
```