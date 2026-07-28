# Images Repository Structure and Metadata Standards

## Image Repository for Pharmaceutical QMS Knowledge Base

---

## Source References
- FDA Guidance: Photographic Documentation
- EU GMP Annex 11 (Computerised Systems)
- ICH Q10 Documentation Requirements
- ISO 19005 (PDF/A for Archival)
- DICOM Standards (Medical Imaging)
- Date Retrieved: 2026-07-28
- Confidence: 0.95

---

## 1. Directory Structure

```
images/
├── medicines/
│   ├── tablets/
│   ├── capsules/
│   ├── injectables/
│   ├── topical/
│   └── packaging/
├── packaging/
│   ├── primary/
│   ├── secondary/
│   ├── tertiary/
│   ├── labeling/
│   └── defects/
├── equipment/
│   ├── manufacturing/
│   ├── packaging/
│   ├── laboratory/
│   ├── facilities/
│   └── defects/
├── manufacturing/
│   ├── processes/
│   ├── facilities/
│   ├── cleanrooms/
│   └── defects/
├── complaints/
│   ├── product_defects/
│   ├── packaging_defects/
│   ├── labeling_defects/
│   └── logistics_defects/
├── deviations/
│   ├── process_deviations/
│   ├── equipment_deviations/
│   └── documentation_deviations/
├── investigations/
│   ├── root_cause_analysis/
│   ├── laboratory_investigations/
│   └── manufacturing_investigations/
├── regulatory/
│   ├── warning_letters/
│   ├── recalls/
│   ├── inspections/
│   └── 483_observations/
├── training/
│   ├── procedures/
│   ├── equipment/
│   ├── aseptic_technique/
│   └── gowning/
└── reference/
    ├── anatomical/
    ├── chemical_structures/
    ├── process_flow_diagrams/
    └── facility_layouts/
```

---

## 2. Image Metadata Standards (EXIF/XMP)

### 2.1 Required Metadata Fields

| Field | Standard | Format | Example |
|-------|----------|--------|---------|
| **Title** | XMP:dc:title | Text | "Atorvastatin 20mg Tablet - Chipped Edge Defect" |
| **Description** | XMP:dc:description | Text | "Close-up of tablet edge showing chipping defect from compression tooling wear. Batch AT-2024-001." |
| **Keywords/Tags** | XMP:dc:subject | Array | ["tablet", "defect", "chipping", "compression", "atorvastatin", "PC-01"] |
| **Category** | Custom:Category | Controlled Vocabulary | "Complaints/Product Defects/Solid Oral/Physical/Chipping" |
| **Source** | Custom:Source | Text | "Internal QC Lab / FDA Warning Letter WL-2024-045" |
| **Date Created** | EXIF:DateTimeOriginal | ISO 8601 | "2024-03-15T10:30:00Z" |
| **Date Modified** | EXIF:ModifyDate | ISO 8601 | "2024-03-15T14:22:00Z" |
| **Author/Creator** | XMP:dc:creator | Text | "QC Analyst - Jane Smith" |
| **Copyright** | XMP:dc:rights | Text | "Company Confidential - Internal Use Only" |
| **Confidentiality** | Custom:Confidentiality | Controlled | "Confidential / Internal / Public" |
| **GMP Relevance** | Custom:GMPRelevance | Boolean | true |
| **Regulatory Reference** | Custom:RegulatoryRef | Text | "21 CFR 211.100, 211.192; PC-01" |
| **Product** | Custom:Product | Text | "Atorvastatin Calcium 20mg Tablet" |
| **Batch/Lot** | Custom:BatchLot | Text | "AT-2024-001" |
| **Equipment** | Custom:Equipment | Text | "Compression Press #3" |
| **Root Cause** | Custom:RootCause | Text | "Tooling wear - upper punch tip erosion" |
| **Severity** | Custom:Severity | Critical/Major/Minor | "Major" |
| **Status** | Custom:Status | Open/Closed/Archived | "Closed" |
| **CAPA Reference** | Custom:CAPARef | Text | "CAPA-2024-0089" |
| **Resolution** | EXIF:XResolution/EXIF:YResolution | Pixels/inch | 300 dpi |
| **Dimensions** | EXIF:ImageWidth/EXIF:ImageHeight | Pixels | 4000 x 3000 |
| **Color Space** | EXIF:ColorSpace | sRGB/Adobe RGB | sRGB |
| **Compression** | EXIF:Compression | Lossless/Lossy | Lossless (PNG/TIFF) |
| **File Size** | File:FileSize | Bytes | 12,456,789 bytes |
| **Format** | File:FileType | PNG/TIFF/JPEG | PNG |
| **Hash (SHA-256)** | Custom:SHA256 | Hex | "a1b2c3d4e5f6..." |
| **Version** | Custom:Version | Integer | 1 |
| **Review Status** | Custom:ReviewStatus | Pending/Reviewed/Approved | "Approved" |
| **Reviewer** | Custom:Reviewer | Text | "QA Manager - John Doe" |
| **Review Date** | Custom:ReviewDate | ISO 8601 | "2024-07-20T09:15:00Z" |

---

## 2.2 Image Quality Standards

| Category | Minimum Resolution | Color Depth | Format | Compression |
|----------|-------------------|-------------|--------|-------------|
| **Defect Photography** | 300 dpi, 4000x3000 px | 24-bit RGB | PNG/TIFF | Lossless |
| **Equipment Photography** | 300 dpi, 4000x3000 px | 24-bit RGB | PNG/TIFF | Lossless |
| **Facility/Layout** | 300 dpi, 5000x5000 px | 24-bit RGB | PNG/TIFF | Lossless |
| **Microscopy/SEM** | 600 dpi, native resolution | 24-bit RGB | TIFF | Lossless |
| **Document/Label Scans** | 600 dpi, 2400x3200 px | 24-bit RGB | PNG/TIFF | Lossless |
| **Training/Procedure** | 150 dpi, 1920x1080 px | 24-bit RGB | JPEG | High Quality (90%) |
| **Reference/Diagram** | 300 dpi, vector preferred | 24-bit RGB | SVG/PNG | Lossless |

---

## 3. Naming Convention

```
[Category]_[Subcategory]_[Product/Equipment]_[Defect/Feature]_[Batch/ID]_[Date]_[Version].[ext]

Examples:
COMP_tablet_atorvastatin_chipping_AT-2024-001_20240315_v1.png
EQUIP_compression_press3_tooling_wear_20240315_v1.png
PACK_blister_atorvastatin_seal_failure_AT-2024-001_20240315_v1.png
EQUIP_cleanroom_ISO5_particle_count_20240315_v1.png
DEV_compression_weight_variation_DEV-2024-0045_20240315_v1.png
INV_root_cause_fishbone_DEV-2024-0045_20240315_v1.png
REG_WL-2024-045_observation_2_20240315_v1.png
```

---

## 3. Photography Guidelines

### 3.1 Defect Photography Protocol
| Step | Requirement |
|------|-------------|
| **Lighting** | Uniform, diffuse lighting (5500K), no shadows/glare |
| **Background** | Neutral gray (18%) or white, non-reflective |
| **Scale** | Include calibrated scale/ruler in every shot |
| **Angles** | Minimum 3 angles: top, side, 45°; macro for detail |
| **Focus** | Sharp focus on defect area, depth of field adequate |
| **Exposure** | Proper exposure, no blown highlights/blocked shadows |
| **Color Reference** | Include color checker card for color-critical defects |
| **Identification** | Include product ID, batch, date, photographer in frame or metadata |
| **Sequence** | Overall → Close-up → Detail (macro) |
| **Lighting Consistency** | Same lighting setup for all defect photos in series |

### 3.2 Equipment Photography Protocol
| Requirement | Specification |
|-------------|---------------|
| **Overall** | Full equipment in context |
| **Critical Components** | Close-ups of critical components |
| **Nameplates** | Clear photos of nameplates, serial numbers |
| **Control Panels** | HMI screens, control panels |
| **Safety Features** | Guards, interlocks, emergency stops |
| **Maintenance Access** | Access points, lubrication points |
| **Nameplate Data** | Manufacturer, model, serial, year, specs |

### 3.3 Facility/Cleanroom Photography
| Requirement | Specification |
|-------------|---------------|
| **Overall Layout** | Wide-angle showing room layout |
| **Airflow** | Diffusers, returns, pressure gauges |
| **Material Flow** | Entry/exit paths, airlocks |
| **Equipment Placement** | Equipment arrangement |
| **Monitoring Points** | Particle counters, temp/RH probes |
| **Personnel Flow** | Gowning areas, airlocks |
| **Critical Surfaces** | Floors, walls, ceilings, HEPA housings |

---

## 4. Image Lifecycle Management

### 4.1 Workflow
```
Capture → Metadata Entry → Quality Review → Approval → Archive → Distribution
```

### 4.2 Retention Schedule
| Image Category | Retention Period | Archive Format |
|----------------|------------------|----------------|
| **GMP-Critical Defects** | Product lifecycle + 10 years | TIFF (archival) |
| **Regulatory Submissions** | Product lifecycle + 10 years | TIFF |
| **Equipment/Facility** | Equipment lifecycle + 5 years | TIFF |
| **Training/Reference** | Current version + 3 years | JPEG/PNG |
| **Reference/Diagrams** | Current version + 5 years | SVG/PNG |
| **Training Photos** | Current version + 3 years | JPEG |

---

## 5. Access Control & Security

| Role | Permissions |
|------|-------------|
| **QA Manager** | Full access: upload, edit metadata, approve, delete |
| **QA Specialist** | Upload, edit metadata, view |
| **Production Supervisor** | View, upload (own area) |
| **QC Analyst** | Upload (lab), view |
| **Regulatory Affairs** | View, download |
| **Regulatory Affairs** | View, download |
| **External Auditor** | View only (read-only, time-limited) |
| **IT Admin** | System admin, backup, no content access |

---

## 6. Search & Retrieval

### 6.1 Searchable Fields
- All metadata fields
- Full-text OCR for text in images
- Visual similarity search (perceptual hashing)
- Geographic/temporal queries
- Relationship queries (linked deviations, CAPAs, batches)

### 6.2 Standard Reports
- Defect trend by image category
- Equipment condition timeline
- Facility condition assessment
- Training material currency
- Regulatory submission package assembly

---

## Metadata

```json
{
  "document_id": "images_repository_metadata_standards",
  "category": "images",
  "subcategory": "metadata_standards",
  "source_type": "Compiled_Technical_Standards",
  "authority": "FDA/EMA/ICH/ISO/DICOM",
  "version": "2026.1",
  "format": "Markdown",
  "retrieved": "2026-07-28",
  "confidence": 0.95,
  "tags": ["Image_Metadata", "EXIF", "XMP", "Photography_Standards", "Defect_Photography", "Equipment_Photography", "Facility_Photography", "Naming_Convention", "Retention", "Access_Control", "Search_Retrieval", "GMP_Documentation", "Digital_Asset_Management"]
}
```