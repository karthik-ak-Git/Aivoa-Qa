export interface ComplaintFormData {
  id?: string;
  status: 'Pending Triage' | 'Under QA Investigation' | 'CAPA Initiated' | 'Closed';
  // 1. Origin & Customer Details
  complaintSource: string;
  customerName: string;

  // 2. Product & Batch Identification
  productName: string;
  productStrength: string;
  batchNumber: string;
  manufacturingDate: string;
  expiryDate: string;
  quantityAffected: string;
  quantityUnit: string;

  // 3. Complaint Details
  complaintType: string;
  complaintDate: string;
  detailedDescription: string;

  // 4. Initial Assessment & Priority
  suggestedSeverity: 'Critical' | 'Major' | 'Minor' | '';
  suggestedNextAction: string;
  riskAssessment: string;

  createdAt?: string;
}

export interface ChatMessage {
  id: string;
  role: 'user' | 'assistant' | 'system';
  content: string;
  timestamp: string;
}

export interface SampleEmailTemplate {
  id: string;
  title: string;
  subject: string;
  rawText: string;
}