# Pharmaceutical Manufacturing Stages

Last Updated: 2026-07-28
Total Stages: 10

---

## Overview

Pharmaceutical manufacturing transforms raw materials (APIs + excipients) into finished dosage forms (FDFs) through a series of controlled, validated processes. Each stage has defined Critical Process Parameters (CPPs), Critical Quality Attributes (CQAs), and potential failure modes that can lead to product complaints.

---

## Stage 1: Raw Material Receiving & Warehouse

### Description
All incoming raw materials (API, excipients, packaging components) are received, sampled, tested, and released before use.

### Key Activities
- Receipt and quarantine
- Visual inspection of containers
- Sampling by QC
- Identity testing
- Storage under specified conditions

### Equipment
- Receiving dock with truck locks
- Warehouse racking systems
- Temperature-controlled storage rooms
- Sample room with laminar flow hoods

### Common Failures
- Wrong material received
- Damaged containers during receipt
- Temperature excursion during storage
- Cross-contamination from adjacent materials
- Pest infestation in warehouse

### Complaint Linkage
- **Product Complaint**: Foreign matter, contamination, potency issues
- **Root Cause**: Raw material mix-up, degraded material used in production

### Key Controls
- Supplier qualification and auditing
- Incoming inspection (visual + analytical)
- Quarantine/release system (electronic or physical)
- First-expiry-first-out (FEFO) management
- Temperature mapping and monitoring

---

## Stage 2: Dispensing & Weighing

### Description
Raw materials are weighed/dispensed according to the Batch Manufacturing Record (BMR).

### Key Activities
- Dispensing of API and excipients per batch formula
- Segregated dispensing for potent compounds
- Verification by second person or electronic system

### Equipment
- Dispensing booths with dust control
- Analytical balances and platform scales
- Dedicated dispensing rooms/booths
- De-dusting systems

### Common Failures
- Wrong weight dispensed
- Cross-contamination between products
- Improper container labeling
- API exposure to operator
- Powder spillage

### Complaint Linkage
- **Product Complaint**: Potency variation, weight variation
- **Root Cause**: Dispensing error, untrained operator

### Key Controls
- 2-person verification
- Check-weighing systems
- Differential weighing
- Dedicated dispensing equipment for potent compounds

---

## Stage 3: Granulation

### Description
Powder particles are agglomerated to improve flow properties, compression characteristics, and content uniformity.

### Types

#### Wet Granulation
- **Process**: Dry mixing → Binder solution addition → Wet massing → Wet milling → Drying → Dry milling
- **Equipment**: High-shear granulator, fluid bed dryer, oscillating mill, rapid mixer granulator (RMG)
- **CPPs**: Binder concentration, granulation time, impeller speed, drying temperature, drying time

#### Dry Granulation (Roller Compaction)
- **Process**: Blending → Roller compaction → Milling → Screening
- **Equipment**: Roller compactor, oscillating mill, vibrosieve
- **CPPs**: Roller pressure, roller gap, feed screw speed, mill speed

### Common Failures
- Over-granulation (too hard granules)
- Under-granulation (too fine, dusty)
- Non-uniform binder distribution
- Over-drying or under-drying
- Chemical degradation during drying

### Complaint Linkage
- **Product Complaint**: Hardness variation, dissolution failure, weight variation, capping
- **Root Cause**: Incorrect granulation endpoint, drying temperature too high

---

## Stage 4: Blending

### Description
The final blend (granules + extra-granular excipients + lubricant) is blended to ensure content uniformity.

### Equipment
- V-blender, bin blender, double cone blender, ribbon blender
- Intensifier bar for de-agglomeration

### Common Failures
- Segregation (demixing) during discharge
- Inadequate blending time
- Over-blending (can cause de-mixing)
- Lubricant over-blending (affects dissolution)

### Complaint Linkage
- **Product Complaint**: Content uniformity failure, dissolution failure
- **Root Cause**: Inadequate blend validation, blender parameter deviation

---

## Stage 5: Compression (Tablets)

### Description
Blended granules are compressed into tablets using a tablet press.

### Equipment
- Single-punch press (R&D/small scale)
- Rotary tablet press (production) — e.g., Fette, Korsch, Manesty
- Tablet de-duster, metal detector, checkweigher

### CPPs
- Compression force
- Pre-compression force
- Turret speed (dwell time)
- Fill depth
- Punch penetration depth
- Feeder speed

### Common Failures
| Defect | Description | Root Cause |
|---|---|---|
| Capping | Top/bottom separates | Air entrapment, low moisture |
| Lamination | Layers separate | High compression force, air entrapment |
| Sticking/Picking | Material sticks to punch face | Low melting point, high humidity |
| Weight Variation | Inconsistent tablet weight | Poor granule flow, feeder issues |
| Hardness Variation | Varying tablet hardness | Compression force variation |
| Friability | Tablets chip/crumble | Low compression force, poor binding |
| Mottling | Uneven color | Poor dye dispersion |
| Double Impression | Stamp on both sides | Punch alignment issue |

### Complaint Linkage
- **Product Complaint**: Broken tablets, crumbling, weight variation, hardness issues
- **Root Cause**: Compression parameter deviation, worn punches/dies, poor granule quality

---

## Stage 6: Coating (Tablets)

### Description
A coating is applied to tablet cores for appearance, taste masking, protection, or controlled release.

### Types
- **Film Coating**: Polymer-based (HPMC, ethyl cellulose) spray application
- **Sugar Coating**: Multiple layers of sugar-based coating
- **Enteric Coating**: pH-sensitive polymer for delayed release
- **Functional Coating**: Controls API release profile

### Equipment
- Perforated pan coater (e.g., Accela-Cota, Glatt)
- Fluid bed coater
- Coating spray system (air-atomized spray guns)

### CPPs
- Inlet air temperature/volume
- Spray rate
- Atomization air pressure
- Pan speed
- Bed temperature
- Exhaust air temperature

### Common Failures
| Defect | Description |
|---|---|
| Chipping | Coating breaks at tablet edges |
| Peeling | Coating separates from core |
| Bridging | Coating fills in score lines |
| Blistering | Coating bubbles |
| Roughness | Uneven coating surface |
| Color Variation | Non-uniform color |
| Orange Peel | Textured surface |
| Twinning | Two tablets stick together |

### Complaint Linkage
- **Product Complaint**: Coating peeling, discolored tablets, taste issues, dissolution failure
- **Root Cause**: Coating process deviation, coating formulation issue

---

## Stage 7: Encapsulation (Capsules)

### Description
Powder blend, granules, pellets, or liquid are filled into hard gelatin or HPMC capsule shells.

### Equipment
- Capsule filling machines (e.g., Bosch, MG2, Zanasi)
- Capsule polisher
- Weight checking system

### Common Failures
- Weight variation
- Empty capsules
- Tilted capsules (cap/body misaligned)
- Denting/damaged shells
- Capsule separation after filling
- Powder leakage from capsule joint

### Complaint Linkage
- **Product Complaint**: Empty capsules, stuck capsules, leakage
- **Root Cause**: Filler adjustment, shell quality issue

---

## Stage 8: Sterilization (Sterile Products)

### Description
Products intended to be sterile (injectables, eye drops, etc.) undergo sterilization.

### Methods
| Method | Application |
|---|---|
| Steam (Autoclave) | Heat-stable products, equipment |
| Dry Heat | Glassware, anhydrous products |
| Ethylene Oxide (EtO) | Heat-sensitive materials, devices |
| Gamma Irradiation | Pre-filled syringes, devices |
| Aseptic Filtration | Heat-sensitive solutions |
| Aseptic Processing | Products that cannot be terminally sterilized |

### Equipment
- Autoclaves (steam sterilizers)
- Dry heat tunnels/ovens
- EtO chambers
- Gamma irradiators
- Sterilizing filters (0.22 micron)

### Common Failures
- Sterility assurance level (SAL) not achieved
- Bioburden before sterilization too high
- Container closure integrity failure after sterilization
- Endotoxin/pyrogen contamination
- Sterilizer temperature distribution not uniform

### Complaint Linkage
- **Product Complaint**: Infection, fever post-injection, visible mold
- **Root Cause**: Sterilization cycle deviation, container closure integrity failure

---

## Stage 9: Packaging & Labeling

### Description
Finished products are packaged in primary containers (bottles, blisters), secondary packaging (cartons), and labeled.

### Key Activities
- Primary packaging: Filling, sealing, capping, blistering
- Labeling: Label application, lot/expiry date coding
- Secondary packaging: Cartoning, bundling
- Tertiary packaging: Case packing, palletizing

### Equipment
- Bottle filling lines, induction sealers, cappers
- Blister packaging machines
- Labeling machines (pressure-sensitive, wet glue, shrink sleeve)
- Cartoners, case packers, palletizers
- Serialization/aggregation systems
- Checkweighers, metal detectors, vision inspection systems

### Common Failures
| Issue | Description |
|---|---|
| Label Mix-up | Wrong label on product |
| Date Coding Error | Wrong or missing expiry/batch number |
| Short Count | Missing units in package |
| Leaking | Container not properly sealed |
| Missing Insert | No package insert |
| Wrong Product | Wrong product in package |

### Complaint Linkage
- **Product Complaint**: Label errors, missing information, leaking, wrong product
- **Root Cause**: Line clearance failure, label control issue, operator error

---

## Stage 10: Quality Control & Release

### Description
Finished products are tested against specifications before release to the market.

### Key Activities
- Sampling per sampling plan
- Physical testing (hardness, friability, weight variation, disintegration)
- Chemical testing (assay, dissolution, content uniformity, impurities)
- Microbiological testing (sterility, bioburden, endotoxin)
- Stability sample submission
- Review of batch documentation (BPR review)
- Batch release by QA

### Common Failures
- OOS results requiring investigation
- Documentation errors in BPR
- Stability sample omission
- Deviations not properly documented

### Complaint Linkage
- **Product Complaint**: Any quality issue that should have been caught by QC
- **Root Cause**: QC testing failure, sampling error, testing error

---

## Manufacturing-to-Complaint Mapping Summary

| Manufacturing Stage | Most Common Causes of Complaints |
|---|---|
| Raw Materials | Impurities, wrong material, degradation |
| Dispensing | Wrong weight, cross-contamination |
| Granulation | Poor flow, dissolution issues |
| Blending | Content uniformity failure |
| Compression | Broken tablets, weight variation, capping |
| Coating | Peeling, discoloration, taste issues |
| Encapsulation | Empty capsules, leakage |
| Sterilization | Sterility failure, endotoxin |
| Packaging | Label errors, leaking, short count |
| QC/Release | Missed defective batch |

**Sources**: ICH Q8 (Pharmaceutical Development), ISPE Baseline Guide, FDA Process Validation Guidance
