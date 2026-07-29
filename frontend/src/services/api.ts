import { ComplaintFormData } from '../types';

const API_BASE = import.meta.env.VITE_API_BASE || 'http://127.0.0.1:8000';

// ── Backend complaint shape (what the API expects/returns) ──

interface BackendComplaint {
  id: string;
  complaint_number: string;
  title: string;
  description: string;
  status: string;
  priority: string;
  source: string;
  category: string | null;
  subcategory: string | null;
  product_name: string | null;
  product_code: string | null;
  batch_number: string | null;
  manufacture_date: string | null;
  expiry_date: string | null;
  reporter_name: string | null;
  reporter_email: string | null;
  reporter_type: string | null;
  ai_category: string | null;
  ai_confidence: number | null;
  ai_suggested_root_cause: string | null;
  ai_suggested_capa: string | null;
  tags: string[] | null;
  created_at: string;
  updated_at: string;
}

interface BackendListResponse {
  complaints: BackendComplaint[];
  total: number;
  page: number;
  page_size: number;
}

// ── Field mapping: frontend ↔ backend ──

const STATUS_MAP_BACKEND_TO_FRONTEND: Record<string, ComplaintFormData['status']> = {
  open: 'Pending Triage',
  in_progress: 'Under QA Investigation',
  under_review: 'Under QA Investigation',
  resolved: 'Closed',
  closed: 'Closed',
  rejected: 'Pending Triage',
};

const STATUS_MAP_FRONTEND_TO_BACKEND: Record<string, string> = {
  'Pending Triage': 'open',
  'Under QA Investigation': 'in_progress',
  'CAPA Initiated': 'in_progress',
  'Closed': 'closed',
};

function frontendToBackend(form: ComplaintFormData): Record<string, unknown> {
  return {
    title: form.complaintType || form.productName || 'Untitled Complaint',
    description: form.detailedDescription || '',
    status: STATUS_MAP_FRONTEND_TO_BACKEND[form.status] || 'open',
    priority: form.suggestedSeverity === 'Critical' ? 'critical'
      : form.suggestedSeverity === 'Major' ? 'high'
      : form.suggestedSeverity === 'Minor' ? 'low'
      : 'medium',
    source: form.complaintSource || 'web',
    product_name: form.productName || null,
    batch_number: form.batchNumber || null,
    manufacture_date: form.manufacturingDate || null,
    expiry_date: form.expiryDate || null,
    reporter_name: form.customerName || null,
    category: form.complaintType || null,
    tags: form.suggestedNextAction ? [form.suggestedNextAction] : null,
  };
}

function backendToFrontend(b: BackendComplaint): ComplaintFormData {
  const status = STATUS_MAP_BACKEND_TO_FRONTEND[b.status] || 'Pending Triage';
  const severityMap: Record<string, ComplaintFormData['suggestedSeverity']> = {
    critical: 'Critical', high: 'Major', medium: '', low: 'Minor',
  };

  return {
    id: b.complaint_number || b.id,
    status,
    complaintSource: b.source || '',
    customerName: b.reporter_name || '',
    productName: b.product_name || '',
    productStrength: b.subcategory || '',
    batchNumber: b.batch_number || '',
    manufacturingDate: b.manufacture_date || '',
    expiryDate: b.expiry_date || '',
    quantityAffected: '',
    quantityUnit: 'kg',
    complaintType: b.category || b.title || '',
    complaintDate: b.created_at ? b.created_at.slice(0, 10) : '',
    detailedDescription: b.description || '',
    suggestedSeverity: severityMap[b.priority] || '',
    suggestedNextAction: b.tags?.[0] || '',
    riskAssessment: b.ai_suggested_root_cause || '',
    createdAt: b.created_at,
  };
}

// ── API functions ──

async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { 'Content-Type': 'application/json', ...options?.headers },
    ...options,
  });
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body.detail || `API error: ${res.status}`);
  }
  if (res.status === 204) return undefined as T;
  return res.json();
}

export async function fetchComplaints(): Promise<ComplaintFormData[]> {
  const data = await request<BackendListResponse>('/api/complaints?page_size=100');
  return (data.complaints || []).map(backendToFrontend);
}

export async function createComplaint(form: ComplaintFormData): Promise<ComplaintFormData> {
  const payload = frontendToBackend(form);
  const created = await request<BackendComplaint>('/api/complaints', {
    method: 'POST',
    body: JSON.stringify(payload),
  });
  return backendToFrontend(created);
}

export async function updateComplaint(
  complaintId: string,
  form: Partial<ComplaintFormData>,
): Promise<ComplaintFormData> {
  const payload: Record<string, unknown> = {};
  if (form.status !== undefined) payload.status = STATUS_MAP_FRONTEND_TO_BACKEND[form.status] || 'open';
  if (form.suggestedSeverity !== undefined) {
    payload.priority = form.suggestedSeverity === 'Critical' ? 'critical'
      : form.suggestedSeverity === 'Major' ? 'high'
      : form.suggestedSeverity === 'Minor' ? 'low'
      : 'medium';
  }
  if (form.detailedDescription !== undefined) payload.description = form.detailedDescription;
  if (form.productName !== undefined) payload.product_name = form.productName;
  if (form.batchNumber !== undefined) payload.batch_number = form.batchNumber;
  if (form.complaintType !== undefined) payload.category = form.complaintType;
  if (form.customerName !== undefined) payload.reporter_name = form.customerName;

  const updated = await request<BackendComplaint>(`/api/complaints/${complaintId}`, {
    method: 'PATCH',
    body: JSON.stringify(payload),
  });
  return backendToFrontend(updated);
}

export async function deleteComplaint(complaintId: string): Promise<void> {
  await request<void>(`/api/complaints/${complaintId}`, { method: 'DELETE' });
}
