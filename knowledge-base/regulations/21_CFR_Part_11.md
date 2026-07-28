# 21 CFR Part 11: Electronic Records; Electronic Signatures

## Overview
- **Full Title**: Electronic Records; Electronic Signatures
- **CFR Reference**: 21 CFR Part 11
- **Effective Date**: August 20, 1997
- **Authority**: 21 U.S.C. 321-393; 42 U.S.C. 262
- **Status**: Final Rule
- **Scope**: Criteria for FDA considering electronic records/signatures trustworthy, reliable, equivalent to paper

## Source References
- **Primary**: https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11
- **FDA Guidance**: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/part-11-electronic-records-electronic-signatures-scope-and-application
- **Cornell LII**: https://www.law.cornell.edu/cfr/text/21/part-11
- **GovInfo PDF**: https://www.govinfo.gov/content/pkg/CFR-2025-title21-vol1/pdf/CFR-2025-title21-vol1-part11.pdf
- **Date Retrieved**: 2026-07-28
- **Confidence**: High (Official CFR)

## Structure

### Subpart A: General Provisions (§§ 11.1 - 11.3)

#### § 11.1 Scope
- (a) Criteria for electronic records/signatures to be trustworthy, reliable, equivalent to paper
- (b) Applies to records in electronic form created, modified, maintained, archived, retrieved, transmitted under any records requirement in Agency regulations
- (c) Records required by predicate rules (e.g., 21 CFR 211, 820, 58) if maintained electronically

#### § 11.2 Implementation
- (a) Part 11 effective August 20, 1997
- (b) Persons may use electronic records/signatures after effective date if compliant
- (c) Part 11 does not require electronic records/signatures

#### § 11.3 Definitions
| Term | Definition |
|------|------------|
| **Act** | Federal Food, Drug, and Cosmetic Act |
| **Agency** | Food and Drug Administration |
| **Biometrics** | Method verifying identity based on physical characteristics |
| **Closed system** | Environment where system access controlled by persons responsible for content |
| **Digital signature** | Electronic signature based on cryptographic methods |
| **Electronic record** | Any combination of text, graphics, data, audio, pictorial in digital form |
| **Electronic signature** | Computer data compilation of symbols executed/adopted as legally binding equivalent of handwritten signature |
| **Handwritten signature** | Scripted name/legal mark written by hand |
| **Open system** | Environment where system access not controlled by persons responsible for content |
| **Predicate rule** | Requirement in statute/regulation requiring record maintenance/submission |

### Subpart B: Electronic Records (§§ 11.10 - 11.70)

#### § 11.10 Controls for Closed Systems
| Requirement | Description |
|-------------|-------------|
| (a) Validation | Validate systems to ensure accuracy, reliability, consistent performance, ability to discern invalid/altered records |
| (b) Record generation | Ability to generate accurate, complete copies in human readable & electronic form |
| (c) Record protection | Protect records for accurate, ready retrieval throughout retention period |
| (d) System access | Limit access to authorized individuals |
| (e) Audit trails | Secure, computer-generated, time-stamped audit trails for record creation/modification/deletion |
| (f) Operational checks | Authority checks, device checks, education/training checks |
| (g) Authority checks | Only authorized individuals can use system, electronically sign records, access operations, alter records |
| (h) Device checks | Input/output device checks for data accuracy |
| (i) Training | Documented training for system operators |
| (j) SOPs | Written policies for system administration, security, accountability |
| (k) Accountability | Written policies for deterrence/detection of record falsification |
| (l) Controls | Controls over systems documentation including distribution, access, use |

#### § 11.30 Controls for Open Systems
- All §11.10 controls PLUS:
- Document encryption
- Digital signature standards
- Additional measures to ensure record authenticity, integrity, confidentiality

#### § 11.50 Signature Manifestations
- (a) Signed electronic records contain:
  - Printed name of signer
  - Date/time of execution
  - Meaning of signature (review, approval, responsibility, authorship)
- (b) Manifestations subject to same controls as electronic records

#### § 11.70 Signature/Record Linking
- Electronic signatures linked to records to prevent excision, copying, transfer
- Linking by electronic means

### Subpart C: Electronic Signatures (§§ 11.100 - 11.300)

#### § 11.100 General Requirements
- (a) Each electronic signature unique to one individual
- (b) Identity verified before signature established
- (b) Certification to FDA that electronic signatures intended as legally binding equivalent of handwritten signatures (submitted per § 11.100(c))

#### § 11.200 Electronic Signature Components and Controls
| Requirement | Description |
|-------------|-------------|
| (a)(1) | Two distinct identification components (e.g., ID code + password) |
| (a)(2) | Single sign-on: ID code + password executed at each signing |
| (a)(3) | Biometric: ID code + biometric executed at each signing |
| (b) | Only genuine owner can use electronic signature |
| (c) | Signature controls maintained |

#### § 11.300 Controls for Identification Codes/Passwords
| Control | Description |
|---------|-------------|
| (a) | Unique ID codes, periodically changed |
| (b) | Password protection, not shared |
| (c) | Loss management (reporting, deauthorization, replacement) |
| (d) | Device tokens/bio-metrics protected from compromise |

## FDA Enforcement Discretion (2003 Guidance)

### Narrow Interpretation of Scope
- FDA exercises enforcement discretion for certain Part 11 requirements
- Focus on predicate rule requirements for validation (not additional Part 11 validation)
- Enforcement discretion on:
  - § 11.10(a) Validation of computerized systems
  - § 11.10(k) SOPs for system administration
  - § 11.10(l) Controls over systems documentation
  - Corresponding § 11.30 requirements for open systems

### Requirements Still Enforced
- Closed system controls (§ 11.10(b)-(j))
- Open system controls (§ 11.30)
- Electronic signature requirements (§§ 11.50, 11.70, 11.100, 11.200, 11.300)

## Common 483 Observations

| Category | Typical Findings |
|----------|------------------|
| **Audit Trail** | Disabled, incomplete, not reviewable, no time stamps |
| **Access Control** | Shared passwords, generic accounts, excessive privileges |
| **Validation** | Inadequate IQ/OQ/PQ, no validation for Part 11 compliance |
| **Signature** | Missing manifestations, no linking, non-unique signatures |
| **Training** | No documented training for system users |
| **SOPs** | Missing or inadequate system administration SOPs |
| **Data Integrity** | Deleted records, modified audit trails, backdated entries |

## Compliance Checklist

### System Validation
- [ ] Computerized system validation per GAMP 5 / FDA guidance
- [ ] Risk-based validation approach (GAMP 5 categories)
- [ ] Validation documentation (URS, FS, DS, IQ, OQ, PQ)
- [ ] Traceability matrix linking requirements to tests

### Access Control
- [ ] Unique user IDs for all personnel
- [ ] Role-based access (least privilege)
- [ ] Password complexity, expiration, lockout policies
- [ ] Automatic logoff after inactivity
- [ ] Periodic access reviews

### Audit Trail
- [ ] Enabled and cannot be disabled by users
- [ ] Captures: who, what, when, old/new values
- [ ] Retained for record retention period
- [ ] Read-only, tamper-evident
- [ ] Regular review by quality unit

### Electronic Signatures
- [ ] Two-component signatures (ID + password) or biometric
- [ ] Signature manifestation includes name, date/time, meaning
- [ ] Signatures linked to records, non-transferable
- [ ] Certification to FDA for legally binding equivalence

### Data Integrity (ALCOA+)
- [ ] Attributable - who performed action
- [ ] Legible - readable throughout lifecycle
- [ ] Contemporaneous - recorded at time of activity
- [ ] Original - first capture or certified copy
- [ ] Accurate - error-free, complete
- [ ] Complete - all data including repeats/reanalyses
- [ ] Consistent - logical sequence, date/time stamped
- [ ] Enduring - durable media
- [ ] Available - accessible for review

### SOPs and Training
- [ ] System administration SOPs
- [ ] Security management SOPs
- [ ] Data backup/recovery SOPs
- [ ] Change control SOPs
- [ ] User training documented and current

### Vendor Management
- [ ] Vendor audit/assessment for SaaS/cloud systems
- [ ] Quality agreements with vendors
- [ ] Vendor validation documentation review
- [ ] Right to audit contractual clause

## Relationship to Other Regulations

| Regulation | Relationship |
|------------|--------------|
| **21 CFR 211** | cGMP for finished pharmaceuticals - Part 11 applies to electronic batch records |
| **21 CFR 820** | Quality System Regulation (medical devices) - Part 11 applies to eQMS |
| **21 CFR 58** | GLP - Part 11 applies to electronic lab records |
| **EU Annex 11** | EU equivalent - Computerised Systems in GMP |
| **GAMP 5** | Industry framework for validation approach |

## Tags
`#21_CFR_Part_11` `#Electronic_Records` `#Electronic_Signatures` `#FDA_Compliance` `#Data_Integrity` `#ALCOA` `#Computer_System_Validation` `#GAMP5` `#eQMS` `#Regulatory_Compliance`

## Metadata
```json
{
  "document_id": "21_CFR_Part_11",
  "category": "regulations",
  "subcategory": "FDA_Regulations",
  "source_type": "Code_of_Federal_Regulations",
  "authority": "FDA",
  "cfr_title": 21,
  "cfr_part": 11,
  "effective_date": "1997-08-20",
  "last_updated": "2025-04-01",
  "format": "Markdown",
  "retrieved": "2026-07-28",
  "confidence": 0.98,
  "tags": ["21_CFR_Part_11", "Electronic_Records", "Electronic_Signatures", "FDA_Compliance", "Data_Integrity", "ALCOA", "Computer_System_Validation", "GAMP5", "eQMS", "Regulatory_Compliance"]
}
```