const API_BASE = import.meta.env.VITE_API_BASE || 'http://127.0.0.1:8000';

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

// ── Copilot AI endpoints ──

export interface CopilotResult {
  form_data: Record<string, unknown>;
  confidence: number;
  agent_used: string;
  sources_used: string[];
}

export async function copilotWrite(query: string, currentForm?: Record<string, unknown>): Promise<CopilotResult> {
  return request<CopilotResult>('/api/copilot/write', {
    method: 'POST',
    body: JSON.stringify({ query, current_form: currentForm || null }),
  });
}

export async function copilotEdit(instruction: string, currentForm: Record<string, unknown>): Promise<CopilotResult> {
  return request<CopilotResult>('/api/copilot/edit', {
    method: 'POST',
    body: JSON.stringify({ instruction, current_form: currentForm }),
  });
}

export async function copilotExtractText(text: string, filename?: string): Promise<CopilotResult> {
  return request<CopilotResult>('/api/copilot/extract-text', {
    method: 'POST',
    body: JSON.stringify({ text, filename: filename || 'pasted_text' }),
  });
}

export async function copilotExtractFile(file: File): Promise<CopilotResult> {
  const formData = new FormData();
  formData.append('file', file);
  const res = await fetch(`${API_BASE}/api/copilot/extract`, {
    method: 'POST',
    body: formData,
  });
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body.detail || `API error: ${res.status}`);
  }
  return res.json();
}
