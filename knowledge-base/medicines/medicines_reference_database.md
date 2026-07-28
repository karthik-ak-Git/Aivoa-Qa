# Medicines Reference Database

## Pharmaceutical Product Information for QMS Integration

---

## Source References
- DailyMed (dailymed.nlm.nih.gov)
- DrugBank (go.drugbank.com)
- RxNorm (nlm.nih.gov/research/umls/rxnorm)
- FDA Orange Book
- EMA Product Information
- WHO INN Lists
- USP-NF Monographs
- Date Retrieved: 2026-07-28
- Confidence: 0.95

---

## 1. Medicine Data Structure (JSON Schema)

```json
{
  "medicine_id": "MED-2026-001234",
  "generic_name": "Atorvastatin Calcium",
  "brand_names": ["Lipitor", "Atorva", "Stator", "Torvast"],
  "api": {
    "name": "Atorvastatin Calcium",
    "cas_number": "134523-03-8",
    "molecular_formula": "C66H68CaF2N4O10",
    "molecular_weight": 1209.42,
    "chemical_structure": "InChI=1S/2C33H34FN2O5.Ca/c2*1-25(2)30-24-28(32(38)39)26(4)21-27(30)31(33(40)41)29(5)22-28;/h2*21-24H,1-5H3,(H,38,39)(H,40,41);/q;;+2/p-2",
    "smiles": "CC(C)C1=CC(=C(C(=C1)C(=O)O)C)C(C)C(=O)NC2=CC=CC=C2C(F)F.CC(C)C1=CC(=C(C(=C1)C(=O)O)C)C(C)C(=O)NC2=CC=CC=C2C(F)F.[Ca+2]"
  },
  "strengths": ["10mg", "20mg", "40mg", "80mg"],
  "dosage_forms": ["Tablet, film-coated"],
  "atc_classification": {
    "code": "C10AA05",
    "level_1": "C - Cardiovascular System",
    "level_2": "C10 - Lipid Modifying Agents",
    "level_3": "C10A - Lipid Modifying Agents, Plain",
    "level_4": "C10AA - HMG CoA Reductase Inhibitors",
    "level_5": "C10AA05 - Atorvastatin"
  },
  "storage_conditions": {
    "temperature": "20-25°C (68-77°F)",
    "excursions": "15-30°C (59-86°F)",
    "humidity": "Protect from moisture",
    "light": "Protect from light",
    "special": "Tight container"
  },
  "route_of_administration": "Oral",
  "manufacturer": {
    "name": "Pfizer Inc.",
    "facility": "Kalamazoo, MI, USA",
    "license_number": "123456"
  },
  "known_defects": [
    {
      "defect_id": "DEF-2023-0045",
      "description": "Tablet chipping at edges during compression",
      "batches_affected": ["ATV20230101", "ATV20230105"],
      "root_cause": "Tooling wear - upper punch tip erosion",
      "status": "Resolved - Tooling replaced"
    },
    {
      "defect_id": "DEF-2024-0012",
      "description": "Dissolution failure at 45 min (Q=75%, result 71%)",
      "batches_affected": ["ATV20240215"],
      "root_cause": "Granulation end-point variability - over-wetting",
      "status": "Under investigation"
    }
  ],
  "common_complaint_types": [
    "PC-01: Tablet physical defect - chipping/cracking",
    "PC-04: Assay/content uniformity - dissolution failure",
    "PK-03: Label - illegible printing",
    "LG-01: Temperature excursion during transit"
  ],
  "packaging_types": [
    "HDPE bottle 30ct with desiccant, child-resistant cap",
    "HDPE bottle 90ct with desiccant, child-resistant cap",
    "Blister PVC/PVDC 10x10, aluminum foil backing"
  ],
  "synonyms": ["Atorvastatin", "Atorvastatina", "Atorvastatine", "Аторвастатин"],
  "chemical_names": [
    "(3R,5R)-7-[2-(4-fluorophenyl)-3-phenyl-4-(phenylcarbamoyl)-5-propan-2-ylpyrrol-1-yl]-3,5-dihydroxyheptanoic acid calcium salt",
    "Calcium (3R,5R)-7-[2-(4-fluorophenyl)-3-phenyl-4-[(phenylamino)carbonyl]-5-(propan-2-yl)pyrrol-1-yl]-3,5-dihydroxyheptanoate"
  ],
  "drug_family": "Statins (HMG-CoA Reductase Inhibitors)",
  "package_insert_url": "https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=...",
  "drug_label_url": "https://www.accessdata.fda.gov/drugsatfda_docs/label/...",
  "retrieved_date": "2026-07-28",
  "confidence": 0.98
}
```

---

## 2. Sample Medicines Database

### 2.1 API Manufactured Products

| Medicine ID | Generic Name | API | Strengths | Dosage Form | ATC Code | Key Manufacturer |
|-------------|--------------|-----|-----------|-------------|----------|------------------|
| MED-001 | Atorvastatin Calcium | Atorvastatin Calcium | 10,20,40,80mg | Tablet | C10AA05 | Pfizer |
| MED-002 | Metformin HCl | Metformin Hydrochloride | 500,850,1000mg | Tablet ER | A10BA02 | Bristol-Myers Squibb |
| MED-003 | Losartan Potassium | Losartan Potassium | 25,50,100mg | Tablet | C09CA01 | Merck |
| MED-004 | Amoxicillin Trihydrate | Amoxicillin Trihydrate | 250,500mg | Capsule | J01CA04 | GSK |
| MED-005 | Omeprazole | Omeprazole Magnesium | 20,40mg | Capsule DR | A02BC01 | AstraZeneca |
| MED-006 | Simvastatin | Simvastatin | 5,10,20,40,80mg | Tablet | C10AA01 | Merck |
| MED-007 | Lisinopril | Lisinopril Dihydrate | 5,10,20,40mg | Tablet | C09AA03 | Merck |
| MED-008 | Amlodipine Besylate | Amlodipine Besylate | 2.5,5,10mg | Tablet | C08CA01 | Pfizer |
| MED-009 | Gabapentin | Gabapentin | 100,300,400,600,800mg | Capsule/Tablet | N03AX12 | Pfizer |
| MED-010 | Sertraline HCl | Sertraline Hydrochloride | 25,50,100mg | Tablet | N06AB06 | Pfizer |

### 2.2 Sterile Injectable Products

| Medicine ID | Generic Name | API | Strengths | Dosage Form | ATC Code | Key Manufacturer |
|-------------|--------------|-----|-----------|-------------|----------|------------------|
| MED-011 | Insulin Glargine | Insulin Glargine | 100U/mL | Injection Sol. | A10AE04 | Sanofi |
| MED-012 | Adalimumab | Adalimumab | 40mg/0.8mL | Injection PFS | L04AB04 | AbbVie |
| MED-013 | Enoxaparin Sodium | Enoxaparin Sodium | 40,60,80,100mg | Injection Syr. | B01AB05 | Sanofi |
| MED-014 | Remdesivir | Remdesivir | 100mg/vial | Injection Lyo. | J05AB16 | Gilead |
| MED-015 | Tocilizumab | Tocilizumab | 80,200,400mg | Injection Conc. | L04AC07 | Roche |

---

## 3. Medicines by Therapeutic Category

### 3.1 Cardiovascular
| ATC | Generic | Brand Examples | Strengths | Forms |
|-----|---------|----------------|-----------|-------|
| C10AA01 | Simvastatin | Zocor | 5-80mg | Tablet |
| C10AA05 | Atorvastatin | Lipitor | 10-80mg | Tablet |
| C09AA03 | Lisinopril | Zestril, Prinivil | 5-40mg | Tablet |
| C09CA01 | Losartan | Cozaar | 25-100mg | Tablet |
| C08CA01 | Amlodipine | Norvasc | 2.5-10mg | Tablet |
| C07AB02 | Metoprolol | Lopressor, Toprol | 25-200mg | Tablet |
| C03CA01 | Furosemide | Lasix | 20-80mg | Tablet/Inj |
| B01AC06 | Aspirin | Bayer, Ecotrin | 81-325mg | Tablet |

### 3.2 Anti-Infectives
| ATC | Generic | Brand Examples | Strengths | Forms |
|-----|---------|----------------|-----------|-------|
| J01CA04 | Amoxicillin | Amoxil, Trimox | 250-500mg | Cap/Susp/Inj |
| J01CR02 | Amox/Clav | Augmentin | 250/125-875/125 | Tab/Susp/Inj |
| J01FA10 | Azithromycin | Zithromax | 250-600mg | Tab/Susp/Inj |
| J01MA02 | Ciprofloxacin | Cipro | 250-750mg | Tab/Inj/Ophth |
| J01XD01 | Metronidazole | Flagyl | 250-500mg | Tab/Inj/Top |
| J05AB01 | Acyclovir | Zovirax | 200-800mg | Tab/Inj/Top |

### 3.3 Central Nervous System
| ATC | Generic | Brand Examples | Strengths | Forms |
|-----|---------|----------------|-----------|-------|
| N06AB06 | Sertraline | Zoloft | 25-100mg | Tablet |
| N06AB10 | Escitalopram | Lexapro | 5-20mg | Tablet |
| N05BA01 | Diazepam | Valium | 2-10mg | Tab/Inj/Rect |
| N03AX12 | Gabapentin | Neurontin | 100-800mg | Cap/Tab/Sol |
| N02AX02 | Tramadol | Ultram | 50-100mg | Tab/Inj/ER |
| N02BE01 | Paracetamol | Tylenol | 325-1000mg | Tab/Cap/Sup/Inj |

---

## 4. Known Defect Patterns by Product Type

### 4.1 Tablet Defects
| Defect Pattern | Typical API Characteristics | Root Cause Categories |
|----------------|----------------------------|----------------------|
| Capping/Lamination | High dose, brittle APIs, poor compressibility | Over-compression, rapid decompression, low binder |
| Sticking/Picking | Hygroscopic, low melting point, polymorphic | Insufficient lubrication, high moisture, tooling wear |
| Weight Variation | Poor flow, segregation, fines | Poor flow, feeder issues, tooling wear |
| Hardness Variation | Variable granule density, moisture | Over/under granulation, compression force drift |
| Friability | Low binder, poor bonding, polymorphic | Under-granulation, low compression, wrong polymorph |

### 4.2 Capsule Defects
| Defect | Typical Cause | Detection |
|--------|---------------|-----------|
| Empty capsules | Dosing disc misalignment, vacuum failure | Weight check, vision |
| Split capsules | Over-filling, brittle shells, high humidity | Visual, leak test |
| Dented capsules | Excessive tamping, handling | Visual |
| Weight variation | Powder flow, dosing disc wear | Weight check |
| Cross-contamination | Inadequate changeover, dust | Visual, assay |

### 4.3 Sterile Product Defects
| Defect | Criticality | Detection |
|--------|-------------|-----------|
| Particulates (glass, rubber, metal) | Critical - Patient safety | 100% visual, AVI |
| Container closure integrity failure | Critical - Sterility | CCIT, dye ingress |
| Fill volume variation | Major - Dose accuracy | Weight check, vision |
| Stoppering defects (loose, tilted) | Major - Sterility | Vision, force monitor |
| Lyophilization cake collapse | Major - Reconstitution | Visual, moisture |
| Moisture content OOS | Major - Stability | Karl Fischer |

---

## 5. Complaint Type Mapping by Product

### 5.1 Solid Oral (Tablets/Capsules)
| Complaint Category | Frequency | Typical Severity |
|-------------------|-----------|-----------------|
| PC-01: Physical defect (chip, crack, split) | High | Major |
| PC-04: Dissolution/Assay OOS | Medium | Critical |
| PC-05: Content uniformity | Low | Critical |
| PC-08: Discoloration/spots | Medium | Major |
| PK-01: Label illegible/missing | Low | Major |
| PK-03: Wrong label on container | Low | Critical |
| LG-01: Temperature excursion | Medium | Major |

### 4.2 Sterile Injectables
| Complaint Category | Frequency | Typical Severity |
|-------------------|-----------|-----------------|
| PC-02: Particulates visible | Medium | Critical |
| PC-06: Sterility concern | Low | Critical |
| PC-07: Pyrogen/endotoxin | Very Low | Critical |
| PK-02: Vial/ampoule breakage | Medium | Major |
| PK-04: Stopper/closure defect | Medium | Critical |
| PK-05: Label - wrong product/strength | Low | Critical |
| LG-01: Cold chain breach | Medium | Critical |

---

## 5. Package Insert & Label Data Sources

### 5.1 Primary Sources
| Source | URL | Coverage |
|--------|-----|----------|
| DailyMed | https://dailymed.nlm.nih.gov | FDA-approved labels (US) |
| FDA Drugs@FDA | https://www.accessdata.fda.gov/scripts/cder/daf/ | Approved products |
| EMA Product Info | https://www.ema.europa.eu/medicines | EU approved |
| Health Canada | https://health-products.canada.ca/dpd-bdpp/ | Canada |
| TGA Australia | https://www.tga.gov.au/ | Australia |
| PMDA Japan | https://www.pmda.go.jp/ | Japan |

### 5.2 Data Fields to Extract
| Category | Fields |
|----------|--------|
| **Identity** | Generic name, Brand names, API, Strength, Dosage form |
| **Regulatory** | NDC, ATC, Approval date, Manufacturer, License |
| **Composition** | Active ingredients, Excipients, Impurities limits |
| **Manufacturing** | Process outline, Critical steps, Controls |
| **Specifications** | Release specs, Shelf-life specs, Analytical methods |
| **Stability** | Conditions, Retest period, Shelf-life, Container |
| **Packaging** | Container/closure, Pack sizes, Labeling |
| **Storage** | Temperature, Humidity, Light, Special |
| **Clinical** | Indications, Dosing, Contraindications, Warnings |
| **Safety** | Adverse reactions, Interactions, Pregnancy category |

---

## Metadata

```json
{
  "document_id": "medicines_reference_database",
  "category": "medicines",
  "subcategory": "product_reference",
  "source_type": "Compiled_Regulatory_Database",
  "authority": "FDA/EMA/WHO/USP/DrugBank/DailyMed/RxNorm",
  "version": "2026.1",
  "format": "Markdown",
  "retrieved": "2026-07-28",
  "confidence": 0.95,
  "tags": ["Medicines_Database", "API_Reference", "Product_Information", "ATC_Classification", "Known_Defects", "Complaint_Mapping", "Package_Insert", "Drug_Labels", "Pharmaceutical_Products"]
}
```