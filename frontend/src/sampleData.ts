import { SampleEmailTemplate, ComplaintFormData } from './types';

export const SAMPLE_EMAIL_TEMPLATES: SampleEmailTemplate[] = [
  {
    id: 'sample-1',
    title: 'Capsule Discoloration & Seal Defect (FDF)',
    subject: 'Urgent Quality Issue: Discolored Amoxicillin 500mg Capsules (Batch #AMX-2026-094)',
    rawText: `From: quality.assurance@apexpharma-dist.com
To: qa.complaints@pharma-global.com
Date: 27 July 2026
Subject: Urgent Quality Issue: Discolored Amoxicillin 500mg Capsules (Batch #AMX-2026-094)

Dear QA Complaints Team,

We are submitting a formal quality notification regarding a shipment received at our distribution center on July 24, 2026. 

Customer: Apex Pharmaceuticals Distribution GmbH
Product Name: Amoxicillin Trihydrate 500mg FDF Capsules
Batch/Lot Number: AMX-2026-094
Manufacturing Date: 2026-03-10
Expiry Date: 2028-03-09
Quantity Affected: 1,200 blister packs (Approx 240 kg equivalent finished product)

Issue Observed:
During secondary packaging inspection, our QA technicians noticed significant capsule discoloration (turning brownish-grey) in 15 inspected blisters. Upon closer examination under optical magnification, the primary Alu-Alu blister heat-seal appears weak and compromised along the edge, allowing moisture ingress.

This defect poses a high risk of active pharmaceutical ingredient degradation and potential loss of potency. We request an immediate investigation, retain sample review, and authorization for return or credit replacement.

Kind regards,
Dr. Helena Vance
Director of Quality Assurance, Apex Pharma Distribution`
  },
  {
    id: 'sample-2',
    title: 'Active Pharmaceutical Ingredient Particle Size OOS (API)',
    subject: 'Quality Complaint: Paracetamol Micropowder API Fine Fraction Excess',
    rawText: `From: purchasing@medisyn-labs.org
To: intake@api-quality.com
Date: 26 July 2026
Subject: Quality Complaint: Paracetamol Micropowder API Fine Fraction Excess (Lot #PCM-API-8812)

Attention QA Director,

During routine incoming physical testing for Lot #PCM-API-8812 received on July 20, 2026, our QC lab identified an Out-of-Specification (OOS) particle size distribution result.

Customer Name: MediSyn Formulations Ltd.
Product Name: Paracetamol Active Pharmaceutical Ingredient (Micropowder EP Grade)
Product Grade: EP / USP Micronized Grade
Batch/Lot Number: PCM-API-8812
Manufacturing Date: 2026-01-18
Expiry Date: 2029-01-17
Quantity Affected: 850 kg (in 34 fiber drums)

Detailed Finding:
Laser diffraction particle size analysis revealed D90 = 42 µm (Specification: D90 <= 25 µm), resulting in severe powder agglomeration during wet granulation tableting trials on Machine #3. This caused tablet weight variation OOS.

We have quarantined all 34 drums. Please provide investigation plan and disposition approval.

Regards,
Markus Thorne
Chief Quality Officer, MediSyn Formulations`
  },
  {
    id: 'sample-3',
    title: 'Injectable Vial Particulate Defect (Sterile FDF)',
    subject: 'Critical Quality Alert: Visible Floating Particles in Ceftriaxone 1g Injectable Vials',
    rawText: `From: hospital.pharmacy@stjude-health.org
To: pv-complaints@pharma-global.com
Date: 27 July 2026
Subject: Critical Quality Alert: Visible Floating Particles in Ceftriaxone 1g Injectable Vials

Urgent Medical Notice:

Customer: St. Jude Central Hospital Pharmacy
Product: Ceftriaxone Sodium for Injection 1g Vials
Grade: Sterile Injectable Grade
Batch Number: CTX-INJ-502
Manufacturing Date: 2026-04-01
Expiry Date: 2028-03-31
Quantity Affected: 450 vials (90 boxes)

Defect Description:
During reconstitution with Sterile Water for Injection in the central IV admixture cleanroom, nursing personnel observed dark, translucent floating particulate matter in 3 consecutive reconstituted vials. Reconstitution was stopped immediately before any patient administration. No patients were exposed or harmed.

We require immediate risk evaluation, health hazard assessment, and urgent dispatch of replacement stock from a different validated lot.

Sincerely,
Sarah Jenkins, PharmD
Director of Hospital Pharmacy`
  }
];

export const INITIAL_EMPTY_FORM: ComplaintFormData = {
  status: 'Pending Triage',
  complaintSource: '',
  customerName: '',
  productName: '',
  productStrength: '',
  batchNumber: '',
  manufacturingDate: '',
  expiryDate: '',
  quantityAffected: '',
  quantityUnit: 'kg',
  complaintType: '',
  complaintDate: '',
  detailedDescription: '',
  suggestedSeverity: '',
  suggestedNextAction: '',
  riskAssessment: '',
};

export const INITIAL_PREFILLED_FORM: ComplaintFormData = {
  id: 'CMP-2026-0041',
  status: 'Pending Triage',
  complaintSource: 'Email Intake (Awaiting AI extraction...)',
  customerName: 'Awaiting AI extraction...',
  productName: 'Awaiting AI extraction...',
  productStrength: 'Awaiting AI extraction...',
  batchNumber: 'Awaiting AI extraction...',
  manufacturingDate: 'Awaiting AI extraction...',
  expiryDate: 'Awaiting AI extraction...',
  quantityAffected: 'Awaiting AI extraction...',
  quantityUnit: 'kg',
  complaintType: 'Awaiting AI extraction...',
  complaintDate: 'Awaiting AI extraction...',
  detailedDescription: 'Awaiting AI extraction...',
  suggestedSeverity: 'Major',
  suggestedNextAction: 'Route to QA Investigation & Issue Replacement',
  riskAssessment: 'Potential moisture ingress or primary packaging seal failure leading to capsule discoloration. Requires immediate retain sample inspection and CAPA review.',
};