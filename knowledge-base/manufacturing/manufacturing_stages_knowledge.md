# Pharmaceutical Manufacturing Stages - Process Knowledge Base

## Overview
Complete reference for pharmaceutical manufacturing stages from raw material to finished product, with equipment, critical quality attributes, failure modes, and complaint linkages for API and FDF manufacturing.

## Source References
- FDA 21 CFR 210/211 - cGMP Regulations
- ICH Q7 - GMP for APIs
- ICH Q8/Q9/Q10 - Pharmaceutical Development/Quality Risk Management/Quality System
- EU GMP Annex 15 - Qualification and Validation
- ISPE Baseline Guides
- PDA Technical Reports
- Date Retrieved: 2026-07-28
- Confidence: 0.95

---

## 1. API Manufacturing Stages (ICH Q7)

### Stage 1: Starting Materials Procurement & Control
| Aspect | Details |
|--------|---------|
| **Inputs** | Raw materials, reagents, solvents, catalysts, intermediates |
| **Key Controls** | Supplier qualification, incoming testing, COA verification, material quarantine |
| **Critical Quality Attributes** | Identity, purity, assay, water content, residual solvents, particle size |
| **Equipment** | Sampling tools, analytical instruments (HPLC, GC, Karl Fischer, DSC) |
| **Common Failures** | Wrong material, contaminated supply, OOS on identity/purity, missing COA |
| **Complaint Links** | PC-04 (Assay), PC-05 (Impurity), PC-09 (Foreign matter from raw material) |
| **Key SOPs** | Vendor qualification, Incoming inspection, Material release/rejection, Re-test |

### Stage 2: Synthesis / Chemical Processing
| Aspect | Details |
|--------|---------|
| **Unit Operations** | Reaction, crystallization, distillation, extraction, filtration, drying |
| **Critical Process Parameters** | Temperature, pressure, pH, stoichiometry, addition rate, reaction time, agitation |
| **Critical Quality Attributes** | Yield, impurity profile, polymorph form, particle size, residual solvents |
| **Equipment** | Reactors (glass-lined, stainless), crystallizers, distillation columns, filters, dryers |
| **Common Failures** | Incomplete reaction, wrong polymorph, high impurities, low yield, solvent carryover |
| **Complaint Links** | PC-04 (Assay), PC-05 (Impurities), PC-08 (Stability - polymorphic change) |
| **Key SOPs** | Batch record execution, In-process controls, Deviation handling, Yield calculation |

### Stage 3: Isolation & Purification
| Aspect | Details |
|--------|---------|
| **Unit Operations** | Filtration, centrifugation, washing, drying, milling, sieving |
| **Critical Process Parameters** | Filter pore size, wash volumes, drying temp/time, mill speed/screen size |
| **Critical Quality Attributes** | Moisture content, particle size distribution, flowability, bulk/tapped density, residual solvents |
| **Equipment** | Nutsche filters, centrifuges, fluid bed dryers, tray dryers, mills, sifters |
| **Common Failures** | High moisture, incorrect PSD, cross-contamination, filter media migration, over-drying |
| **Complaint Links** | PC-01 (Friability - moisture), PC-05 (Residual solvents), PC-07 (Dissolution - PSD) |
| **Key SOPs** | Drying endpoint determination, Milling controls, Sieving integrity, Cleaning validation |

### Stage 4: Final API Processing & Packaging
| Aspect | Details |
|--------|---------|
| **Operations** | Final milling, blending (if multi-lot), packaging, labeling |
| **Critical Controls** | Homogeneity, container integrity, label accuracy, tamper evidence |
| **Packaging Types** | Fiber drums with PE liners, HDPE containers, FIBCs, glass bottles (small scale) |
| **Key Controls** | Container cleaning, liner qualification, headspace control, inert gas purge |
| **Common Failures** | Label mix-up, container damage, moisture ingress, segregation during transport |
| **Complaint Links** | PK-01 (Container), PK-03 (Label), LG-01 (Moisture during transit) |
| **Key SOPs** | Packaging operation, Label reconciliation, Container qualification, Shipping release |

---

## 2. FDF (Finished Dosage Form) Manufacturing Stages

### Stage 1: Material Receipt & Dispensing
| Aspect | Details |
|--------|---------|
| **Inputs** | API, excipients (fillers, binders, disintegrants, lubricants, glidants, colorants), primary packaging |
| **Key Controls** | Dispensing booth/weigh room, double verification, environment control (temp/RH), dust containment |
| **Critical Quality Attributes** | Correct material, correct quantity, identity verified, no cross-contamination |
| **Equipment** | Analytical balances, dispensing booths, vacuum transfer, containment systems |
| **Common Failures** | Wrong material dispensed, wrong quantity, cross-contamination, environment excursion |
| **Complaint Links** | PC-10 (Wrong API), PC-04 (Assay - wrong excipient ratio), PK-03 (Wrong label on dispensed container) |
| **Key SOPs** | Weighing/dispensing, Double verification, Cleaning between products, Environmental monitoring |

### Stage 2: Granulation (Wet/Dry)
| Aspect | Details |
|--------|---------|
| **Wet Granulation** | Mixing → Binder addition → Wet massing → Wet screening → Drying → Dry screening → Blending |
| **Dry Granulation** | Mixing → Compaction (roller compactor) → Milling/Sieving → Blending |
| **Direct Compression** | Mixing → Blending → Compression (no granulation) |
| **Critical Process Parameters** | Impeller/chopper speed, binder addition rate, end-point (torque/power), inlet/outlet temp, mill speed/screen |
| **Critical Quality Attributes** | Granule size distribution, moisture content (LOD), flowability, compressibility, content uniformity |
| **Equipment** | High-shear mixer (Glenmark, GEA, Diosna), Fluid bed dryer (Glatt, Ventilex), Roller compactor (Alexanderwerk, Fitzpatrick), Mills (Quadro, Fitzpatrick), Blenders (V-blender, Bin blender) |
| **Common Failures** | Over-granulation (hard granules), under-granulation (poor flow), high moisture (sticking), low moisture (poor compression), segregation, content uniformity failure |
| **Complaint Links** | PC-01 (Tablet defects), PC-04 (Content uniformity), PC-07 (Dissolution - granule properties) |
| **Key SOPs** | Granulation end-point determination, Drying endpoint (LOD), Milling controls, Blend uniformity sampling |

### Stage 3: Blending / Final Mix
| Aspect | Details |
|--------|---------|
| **Operations** | Lubricant blending (magnesium stearate), final blend uniformity |
| **Critical Process Parameters** | Blender speed, time, fill level, lubricant blending time (critical!) |
| **Critical Quality Attributes** | Blend uniformity (RSD ≤5%), lubricant distribution, flow properties |
| **Equipment** | V-blenders, Double-cone, Bin blenders (IBC), Continuous blenders (Gericke) |
| **Common Failures** | Over-lubrication (prolonged disintegration, low hardness), under-blending (CU failure), segregation during transfer |
| **Complaint Links** | PC-01 (Lamination - over-lubrication), PC-04 (CU failure), PC-07 (Dissolution - lubricant) |
| **Key SOPs** | Blending validation, Lubricant sensitivity study, Blend sampling plan, Transfer procedures |

### Stage 4: Compression (Tableting)
| Aspect | Details |
|--------|---------|
| **Machine Types** | Single rotary (low volume), Double rotary (high volume), Multi-layer (bi/tri-layer) |
| **Critical Process Parameters** | Compression force (pre/main), turret speed, feed frame settings, punch penetration, turret dwell time |
| **Critical Quality Attributes** | Weight, thickness, hardness, friability, disintegration, dissolution, weight variation, content uniformity |
| **In-Process Controls** | Weight (every 15-30 min), hardness/thickness (every 15-30 min), friability (hourly), disintegration (hourly), weight variation (statistical) |
| **Equipment** | Tablet presses (Korsch, Fette, Manesty, Kilian, Elizabeth), Tooling (EU/D/BBB standards), Force feeders |
| **Common Failures** | Weight variation, capping/lamination, sticking/picking, double imprint, high friability, low hardness, high/low dissolution |
| **Complaint Links** | PC-01 (All physical defects), PC-04 (Weight/CU), PC-07 (Dissolution) |
| **Key SOPs** | Compression setup, Tooling management, IPC frequency, Weight control, Tooling inspection |

### Stage 5: Coating (Film/Sugar/Enteric)
| Aspect | Details |
|--------|---------|
| **Types** | Film (aqueous/organic), Sugar, Enteric (pH-dependent), Functional (modified release) |
| **Critical Process Parameters** | Inlet/exhaust temp, spray rate, atomization pressure, pan speed, gun distance, coating weight gain |
| **Critical Quality Attributes** | Weight gain, uniformity, logo/imprint legibility, color uniformity, dissolution profile (enteric/MR), disintegration |
| **Equipment** | Perforated pan coaters (O'Hara, Dumoulin, Glatt, Freund), Wurster (fluid bed), Spray systems |
| **Common Failures** | Logo bridging/filling, picking/twinning, color variation, coating non-uniformity, dissolution failure (enteric), sticking/twinning |
| **Complaint Links** | PK-04 (Logo illegible), PC-01 (Picking - cosmetic), PC-07 (Dissolution - enteric/MR) |
| **Key SOPs** | Coating suspension preparation, Process parameters, Weight gain calculation, Logo qualification |

### Stage 6: Encapsulation (Hard/Soft Gel)
| Aspect | Details |
|--------|---------|
| **Hard Capsule** | Powder/pellet fill → Two-piece gelatin/HPMC shells → Band sealing (optional) → Polishing |
| **Soft Gelatin** | Gelatin melt → Fill formulation → Rotary die encapsulation → Drying → Inspection |
| **Critical Process Parameters** | Fill weight, capsule orientation, separation/alignment, band seal integrity, drying conditions |
| **Critical Quality Attributes** | Fill weight, weight variation, content uniformity, dissolution, shell integrity, moisture |
| **Equipment** | Capsule fillers (Bosch, MG2, IMA, Zanasi), Softgel machines (Schukat, Technophar), Polishers, Sorters |
| **Common Failures** | Empty capsules, split capsules, dents, weight variation, content uniformity, leakage (softgel), sticking |
| **Complaint Links** | PC-01 (Empty/split/dented), PC-04 (Fill weight/CU), PK-02 (Leakage) |
| **Key SOPs** | Capsule qualification, Fill weight adjustment, Band sealing validation, Shell moisture control |

### Stage 7: Sterile Manufacturing (Aseptic/Lyophilization)
| Aspect | Details |
|--------|---------|
| **Aseptic Processing** | Component prep → Sterilization (autoclave/depyrogenation) → Aseptic assembly → Filling → Stoppering → Crimping |
| **Lyophilization** | Filling → Partial stoppering → Freezing → Primary drying → Secondary drying → Full stoppering → Crimping |
| **Critical Process Parameters** | Fill weight/volume, fill accuracy, stoppering force, vacuum/pressure, shelf temp, cycle times |
| **Critical Quality Attributes** | Sterility, particulate matter, fill volume/weight, reconstitution time, cake appearance, moisture |
| **Equipment** | Washers, depyrogenation tunnels, fill/finish lines (IMA, Bosch, Marchesini), lyophilizers (IMA, GEA, SP), RABS/Isolators |
| **Common Failures** | Sterility failure, particulates (glass, rubber, fibers), fill volume OOS, stoppering defects, cake collapse, moisture OOS |
| **Complaint Links** | PC-02 (Particulates), PC-06 (Sterility), PC-08 (Moisture/cake) |
| **Key SOPs** | Media fills, Environmental monitoring, Filter integrity, Lyophilization cycle, Component prep |

### Stage 8: Primary Packaging
| Aspect | Details |
|--------|---------|
| **Blister Packing** | Forming → Feeding → Sealing → Perforation → Cutting → Inspection |
| **Bottle Packing** | Counting → Filling → Desiccant → Cotton → Capping → Induction seal → Labeling |
| **Sachet/Stick Pack** | Forming → Filling → Sealing → Cutting |
| **Critical Process Parameters** | Seal temp/pressure/dwell, forming temp/pressure, feed accuracy, code printing, inspection sensitivity |
| **Critical Quality Attributes** | Seal integrity, leak test, count accuracy, label placement, code readability, child-resistant function |
| **Equipment** | Blister machines (Uhlmann, IMA, Marchesini, Mediseal), Bottle lines (NJM, Busch, Krones), Cartoners |
| **Common Failures** | Seal failure, empty pockets, wrong count, label skew, code missing/illegible, damaged blister |
| **Complaint Links** | PK-01 (Blister/bottle), PK-02 (Seal/cap), PK-04 (Label), PK-07 (Serialization) |
| **Key SOPs** | Packaging setup, Line clearance, Reconciliation, Seal integrity testing, Code verification |

### Stage 9: Secondary Packaging & Serialization
| Aspect | Details |
|--------|---------|
| **Operations** | Cartoning → Case packing → Palletizing → Stretch wrapping → Labeling |
| **Serialization** | Unit → Bundle → Case → Pallet aggregation; 2D DataMatrix (GS1); Verification; Reporting |
| **Critical Controls** | Aggregation accuracy, code readability, parent-child linkage, tamper evidence, pallet stability |
| **Equipment** | Cartoners (IMA, Marchesini, Korchi), Case packers, Palletizers, Aggregation scanners, Print & apply |
| **Common Failures** | Missing leaflet, wrong carton, aggregation break, unreadable code, damaged case |
| **Complaint Links** | PK-05 (Carton), PK-06 (Leaflet), PK-07 (Serialization), LG-03 (Wrong case count) |
| **Key SOPs** | Serialization setup, Aggregation verification, Reconciliation, Tamper verification |

---

## 3. Cross-Stage Quality Control Points

| QC Point | Stage | Tests | Frequency | Specifications |
|----------|-------|-------|-----------|----------------|
| **Starting Material Release** | API/FDF | Identity, Assay, Impurities, Water, Residual Solvents, Micro | Each lot | Pharmacopeia / In-house |
| **In-Process - Granulation** | FDF | LOD, PSD, Flow, Blend Uniformity | Per batch / Per run | In-house |
| **In-Process - Compression** | FDF | Weight, Hardness, Thickness, Friability, DT, Dissolution | Per IPC schedule | USP <701>, <711>, <1216> |
| **In-Process - Coating** | FDF | Weight gain, Visual, Dissolution (enteric) | Per run | In-house |
| **In-Process - Sterile** | FDF | Fill weight, Sterility (media fill), Particulates | Per batch / Media fill | USP <797>, <788> |
| **Finished Product Release** | Both | Full monograph: ID, Assay, Impurities, Dissolution, CU, Micro, Stability | Each batch | USP/EP/JP / ICH Q6A |
| **Stability** | Both | ICH Q1 conditions: 25/60, 30/65, 40/75, 5/±3 | Per protocol | ICH Q1A-Q1F |
| **Annual Product Review** | Both | Trend analysis, CAPA effectiveness, Change control, Market complaints | Annual | ICH Q10, FDA 211.180 |

---

## 4. Manufacturing Stage → Complaint Category Mapping Matrix

| Manufacturing Stage | Primary Complaint Categories | Key Defect Types |
|---------------------|------------------------------|------------------|
| **API Synthesis** | PC-04, PC-05, PC-08 | Impurities, Assay, Stability |
| **API Isolation** | PC-01, PC-05, PC-07 | PSD, Residual solvents, Dissolution |
| **API Packaging** | PK-01, PK-03, LG-01 | Container, Label, Moisture |
| **Dispensing** | PC-10, PC-04, PK-03 | Wrong material, Wrong qty, Label |
| **Granulation** | PC-01, PC-04, PC-07 | Tablet defects, CU, Dissolution |
| **Blending** | PC-01, PC-04, PC-07 | Lubrication, CU, Dissolution |
| **Compression** | PC-01, PC-04, PC-07 | All physical, Weight/CU, Dissolution |
| **Coating** | PK-04, PC-01, PC-07 | Logo, Picking, Dissolution |
| **Encapsulation** | PC-01, PC-04, PK-02 | Physical, CU, Leakage |
| **Sterile Fill** | PC-02, PC-06, PC-08 | Particulates, Sterility, Moisture |
| **Primary Pack** | PK-01, PK-02, PK-04, PK-07 | Container, Seal, Label, Serial |
| **Secondary Pack** | PK-05, PK-06, PK-07, LG-03 | Carton, Leaflet, Serial, Count |
| **Distribution** | LG-01, LG-02, LG-03 | Temp, Damage, Wrong ship |

---

## 5. Process Validation Lifecycle per Stage

| Stage | Stage 1: Process Design | Stage 2: Process Qualification | Stage 3: Continued Process Verification |
|-------|------------------------|--------------------------------|------------------------------------------|
| **Granulation** | DOE for critical params; PAT (NIR for endpoint) | 3 consecutive batches; IPC ranges; Scale-up factors | CPV: LOD, PSD, Blend CU trends; SPC charts |
| **Blending** | Lubricant sensitivity; Blend time study; Sampling plan | 3 batches; Blend uniformity at multiple locations | CPV: Blend CU trend; Lubricant lot variability |
| **Compression** | Compression force profile; Tooling design; PAT (force) | 3 batches; Weight control; IPC capability (Cpk>1.33) | CPV: Weight/Hardness/Friability trends; Tooling life |
| **Coating** | Spray rate/temp design; Logo qualification; Scale-up | 3 batches; Weight gain uniformity; Dissolution | CPV: Logo legibility; Weight gain; Color consistency |
| **Sterile Fill** | Media fill design; Aseptic process simulation | 3 media fills; Fill accuracy; Stoppering force | CPV: Environmental trends; Filter integrity; Media fill |
| **Packaging** | Seal validation; Code verification; Line speed challenge | 3 runs; Seal integrity; Aggregation accuracy | CPV: Seal test results; Code readability; Reconciliation |

---

## Metadata

```json
{
  "document_id": "manufacturing_stages_knowledge",
  "category": "manufacturing",
  "subcategory": "process_stages",
  "source_type": "Compiled_Regulatory_Technical_Reference",
  "authority": "FDA/ICH/EU_GMP/ISPE/PDA",
  "version": "2026.1",
  "format": "Markdown",
  "retrieved": "2026-07-28",
  "confidence": 0.95,
  "tags": ["Manufacturing_Stages", "API_Production", "FDF_Production", "Granulation", "Compression", "Coating", "Encapsulation", "Sterile_Manufacturing", "Packaging", "Process_Validation", "Quality_Control", "Complaint_Linkage"]
}
```

---

## Usage Notes

1. **Stage-Gate Reviews**: Each stage should have defined entry/exit criteria
2. **Deviation Impact**: Assess downstream impact when deviation occurs at any stage
3. **Change Control**: Any change to critical process parameters requires impact assessment
3. **Technology Transfer**: Stage definitions critical for site-to-site transfer
4. **Continuous Improvement**: CPV data should drive process optimization
5. **Complaint Feedback**: Field complaints must trace back to manufacturing stage for root cause