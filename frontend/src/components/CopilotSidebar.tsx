import React, { useRef, useEffect, useState } from 'react';
import { Send, Bot, MessageSquare, Paperclip, Loader2, CheckCircle, Brain, FileText } from 'lucide-react';
import { useAppDispatch, useAppSelector } from '../store/hooks';
import { addChatMessage, setIsSending } from '../store/uiSlice';
import { replaceFormData } from '../store/formSlice';
import { ComplaintFormData } from '../types';

const API_BASE = import.meta.env.VITE_API_BASE || 'http://127.0.0.1:8000';

interface CopilotSidebarProps {
  currentForm: ComplaintFormData;
}

export const CopilotSidebar: React.FC<CopilotSidebarProps> = ({ currentForm }) => {
  const dispatch = useAppDispatch();
  const chatMessages = useAppSelector((state) => state.ui.chatMessages);
  const isSending = useAppSelector((state) => state.ui.isSending);
  const [inputMessage, setInputMessage] = useState('');
  const chatEndRef = useRef<HTMLDivElement>(null);
  const [thinkingStage, setThinkingStage] = useState<'idle' | 'retrieving' | 'generating' | 'complete'>('idle');
  const [backendStatus, setBackendStatus] = useState<'unknown' | 'connected' | 'error'>('unknown');
  const [pendingForm, setPendingForm] = useState<ComplaintFormData | null>(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [chatMessages]);

  useEffect(() => {
    fetch(`${API_BASE}/health`, { signal: AbortSignal.timeout(3000) })
      .then(r => r.json())
      .then(d => setBackendStatus(d.status === 'ok' ? 'connected' : 'error'))
      .catch(() => setBackendStatus('error'));
  }, []);

  const detectMode = (query: string): 'edit' | 'write' => {
    const lower = query.toLowerCase();
    const editPatterns = [
      /\b(edit|change|update|modify|set|make|revise|fix|correct|replace)\b/,
      /\b(severity|status|product|batch|date|description|customer|source|type|quantity)\b/,
      /\b(to |the |this |that )\b/,
    ];
    const hasFormContext = currentForm.productName || currentForm.batchNumber || currentForm.detailedDescription;
    if (hasFormContext && editPatterns.some(p => p.test(lower))) {
      return 'edit';
    }
    return 'write';
  };

  const sendMessage = async (query: string) => {
    if (!query.trim() || isSending) return;

    dispatch(addChatMessage({
      id: `msg-${Date.now()}`,
      role: 'user',
      content: query.trim(),
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    }));
    setInputMessage('');
    dispatch(setIsSending(true));
    setThinkingStage('retrieving');

    try {
      const mode = detectMode(query.trim());
      setThinkingStage('generating');

      let endpoint: string;
      let body: any;

      if (mode === 'edit') {
        endpoint = `${API_BASE}/api/copilot/edit`;
        body = JSON.stringify({
          instruction: query.trim(),
          current_form: currentForm,
        });
      } else {
        endpoint = `${API_BASE}/api/copilot/write`;
        body = JSON.stringify({
          query: query.trim(),
          current_form: currentForm,
        });
      }

      const res = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body,
      });

      setThinkingStage('complete');

      if (!res.ok) {
        const errData = await res.json().catch(() => ({}));
        throw new Error(errData.detail || `Server error: ${res.status}`);
      }

      const result = await res.json();
      const formData: ComplaintFormData = {
        id: currentForm.id || '',
        createdAt: currentForm.createdAt || new Date().toISOString(),
        status: result.form_data.status || 'Pending Triage',
        complaintSource: result.form_data.complaintSource || '',
        customerName: result.form_data.customerName || '',
        productName: result.form_data.productName || '',
        productStrength: result.form_data.productStrength || '',
        batchNumber: result.form_data.batchNumber || '',
        manufacturingDate: result.form_data.manufacturingDate || '',
        expiryDate: result.form_data.expiryDate || '',
        quantityAffected: result.form_data.quantityAffected || '',
        quantityUnit: result.form_data.quantityUnit || 'kg',
        complaintType: result.form_data.complaintType || '',
        complaintDate: result.form_data.complaintDate || '',
        detailedDescription: result.form_data.detailedDescription || '',
        suggestedSeverity: result.form_data.suggestedSeverity || 'Major',
        suggestedNextAction: result.form_data.suggestedNextAction || '',
        riskAssessment: result.form_data.riskAssessment || '',
      };

      setPendingForm(formData);

      const summary = [
        `**Agent:** ${result.agent_used}  |  **Confidence:** ${(result.confidence * 100).toFixed(0)}%`,
        '',
        `**Product:** ${formData.productName || 'N/A'}`,
        `**Severity:** ${formData.suggestedSeverity}`,
        `**Type:** ${formData.complaintType}`,
        formData.batchNumber ? `**Batch:** ${formData.batchNumber}` : '',
        '',
        formData.detailedDescription ? `**Description:** ${formData.detailedDescription.slice(0, 300)}${formData.detailedDescription.length > 300 ? '...' : ''}` : '',
        '',
        formData.riskAssessment ? `**Risk:** ${formData.riskAssessment.slice(0, 200)}${formData.riskAssessment.length > 200 ? '...' : ''}` : '',
      ].filter(Boolean).join('\n');

      dispatch(addChatMessage({
        id: `msg-${Date.now() + 1}`,
        role: 'assistant',
        content: summary,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      }));

    } catch (err: any) {
      setThinkingStage('complete');
      dispatch(addChatMessage({
        id: `msg-${Date.now() + 1}`,
        role: 'assistant',
        content: `Error: ${err.message}. Make sure the backend is running at ${API_BASE}.`,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      }));
    } finally {
      setThinkingStage('idle');
      dispatch(setIsSending(false));
    }
  };

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    dispatch(addChatMessage({
      id: `msg-${Date.now()}`,
      role: 'user',
      content: `[Uploaded: ${file.name}]`,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    }));
    dispatch(setIsSending(true));
    setThinkingStage('retrieving');

    try {
      setThinkingStage('generating');
      const formDataUpload = new FormData();
      formDataUpload.append('file', file);

      const res = await fetch(`${API_BASE}/api/copilot/extract`, {
        method: 'POST',
        body: formDataUpload,
      });

      setThinkingStage('complete');

      if (!res.ok) {
        const errData = await res.json().catch(() => ({}));
        throw new Error(errData.detail || `Server error: ${res.status}`);
      }

      const result = await res.json();
      const fd: ComplaintFormData = {
        id: currentForm.id || '',
        createdAt: currentForm.createdAt || new Date().toISOString(),
        status: result.form_data.status || 'Pending Triage',
        complaintSource: result.form_data.complaintSource || '',
        customerName: result.form_data.customerName || '',
        productName: result.form_data.productName || '',
        productStrength: result.form_data.productStrength || '',
        batchNumber: result.form_data.batchNumber || '',
        manufacturingDate: result.form_data.manufacturingDate || '',
        expiryDate: result.form_data.expiryDate || '',
        quantityAffected: result.form_data.quantityAffected || '',
        quantityUnit: result.form_data.quantityUnit || 'kg',
        complaintType: result.form_data.complaintType || '',
        complaintDate: result.form_data.complaintDate || '',
        detailedDescription: result.form_data.detailedDescription || '',
        suggestedSeverity: result.form_data.suggestedSeverity || 'Major',
        suggestedNextAction: result.form_data.suggestedNextAction || '',
        riskAssessment: result.form_data.riskAssessment || '',
      };

      setPendingForm(fd);

      const summary = [
        `**OCR Agent:** Extracted from \`${file.name}\`  |  **Confidence:** ${(result.confidence * 100).toFixed(0)}%`,
        '',
        `**Product:** ${fd.productName || 'N/A'}`,
        `**Severity:** ${fd.suggestedSeverity}`,
        `**Type:** ${fd.complaintType}`,
        fd.batchNumber ? `**Batch:** ${fd.batchNumber}` : '',
        '',
        fd.detailedDescription ? `**Description:** ${fd.detailedDescription.slice(0, 300)}${fd.detailedDescription.length > 300 ? '...' : ''}` : '',
      ].filter(Boolean).join('\n');

      dispatch(addChatMessage({
        id: `msg-${Date.now() + 1}`,
        role: 'assistant',
        content: summary,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      }));

    } catch (err: any) {
      setThinkingStage('complete');
      dispatch(addChatMessage({
        id: `msg-${Date.now() + 1}`,
        role: 'assistant',
        content: `Error extracting document: ${err.message}`,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      }));
    } finally {
      setThinkingStage('idle');
      dispatch(setIsSending(false));
    }
    e.target.value = '';
  };

  const handleApplyForm = () => {
    if (!pendingForm) return;
    dispatch(replaceFormData(pendingForm));
    setPendingForm(null);
    dispatch(addChatMessage({
      id: `msg-${Date.now()}`,
      role: 'system',
      content: 'Form updated with AI-generated data.',
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    }));
  };

  return (
    <div className="bg-white rounded-xl border border-slate-200/80 shadow-2xs flex flex-col h-[calc(100vh-8rem)] sticky top-20">
      <div className="p-3 border-b border-slate-100 flex items-center justify-between bg-slate-50/50 rounded-t-xl">
        <div className="flex items-center gap-1.5 text-blue-700 font-semibold text-xs md:text-sm">
          <MessageSquare className="w-3.5 h-3.5" />
          AI QA Copilot
        </div>
        <div className="flex items-center gap-2">
          {pendingForm && (
            <button
              onClick={handleApplyForm}
              className="text-[10px] px-2.5 py-1 bg-green-600 hover:bg-green-700 text-white rounded-full font-medium transition-colors flex items-center gap-1"
            >
              <FileText className="w-3 h-3" />
              Apply to Form
            </button>
          )}
          <span className={`text-[10px] px-2 py-0.5 rounded-full font-medium ${
            backendStatus === 'connected'
              ? 'bg-green-100 text-green-700'
              : backendStatus === 'error'
              ? 'bg-red-100 text-red-700'
              : 'bg-slate-100 text-slate-500'
          }`}>
            {backendStatus === 'connected' ? '● Online' : backendStatus === 'error' ? '● Offline' : '● Checking...'}
          </span>
        </div>
      </div>

      <div className="flex-1 flex flex-col min-h-0">
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {chatMessages.map((msg) => (
            <div
              key={msg.id}
              className={`flex gap-3 text-xs md:text-sm animate-fade-in ${
                msg.role === 'user' ? 'justify-end' : 'justify-start'
              }`}
            >
              {msg.role === 'assistant' && (
                <div className="w-7 h-7 rounded-full bg-blue-100 text-blue-700 flex items-center justify-center shrink-0 text-xs font-bold mt-0.5">
                  <Bot className="w-4 h-4" />
                </div>
              )}
              <div
                className={`max-w-[85%] rounded-xl p-3.5 space-y-1 ${
                  msg.role === 'user'
                    ? 'bg-blue-600 text-white rounded-br-2xs'
                    : msg.role === 'system'
                    ? 'bg-green-50 border border-green-200 text-green-800 rounded-bl-2xs text-center text-xs'
                    : 'bg-slate-100/80 border border-slate-200/60 text-slate-800 rounded-bl-2xs'
                }`}
              >
                <p className="whitespace-pre-wrap leading-relaxed">{msg.content}</p>
                <span
                  className={`text-[10px] block text-right font-mono ${
                    msg.role === 'user' ? 'text-blue-200' : 'text-slate-400'
                  }`}
                >
                  {msg.timestamp}
                </span>
              </div>
            </div>
          ))}

          {thinkingStage !== 'idle' && (
            <div className="flex items-center gap-3 text-xs md:text-sm justify-start animate-slide-up">
              <div className="w-7 h-7 rounded-full bg-gradient-to-br from-blue-500 to-purple-500 text-white flex items-center justify-center shrink-0 text-xs font-bold mt-0.5 animate-pulse">
                <Brain className="w-4 h-4" />
              </div>
              <div className="max-w-[85%] rounded-xl p-3.5 space-y-2 bg-gradient-to-r from-blue-50 to-purple-50 border border-blue-100/50 rounded-bl-2xs">
                <div className="flex items-center gap-2 text-blue-700 font-medium">
                  <Loader2 className="w-4 h-4 animate-spin" />
                  <span>{thinkingStage === 'retrieving' && 'Searching knowledge base...'}</span>
                  <span>{thinkingStage === 'generating' && 'Generating with gemma2-9b-it...'}</span>
                  <span>{thinkingStage === 'complete' && 'Done!'}
                    <CheckCircle className="w-3.5 h-3.5 ml-1 text-green-500" />
                  </span>
                </div>
                <div className="flex gap-1 ml-6">
                  {[0, 1, 2].map((i) => (
                    <div
                      key={i}
                      className="w-1.5 h-1.5 rounded-full bg-blue-400/60 animate-bounce"
                      style={{ animationDelay: `${i * 150}ms` }}
                    />
                  ))}
                </div>
              </div>
            </div>
          )}

          {isSending && thinkingStage === 'idle' && (
            <div className="flex items-center gap-2 text-xs text-slate-400 italic">
              <Bot className="w-4 h-4 animate-spin text-blue-500" />
              Copilot is thinking...
            </div>
          )}
          <div ref={chatEndRef} />
        </div>

        <div className="p-3 border-t border-slate-200/80 bg-white rounded-b-xl space-y-2">
          <form
            onSubmit={(e) => {
              e.preventDefault();
              sendMessage(inputMessage);
            }}
            className="flex items-center gap-2"
          >
            <label className="p-2.5 bg-slate-50 border border-slate-200 rounded-lg hover:bg-slate-100 transition-colors cursor-pointer relative group" title="Attach file">
              <input
                type="file"
                accept=".pdf,.txt,.doc,.docx,.eml,.msg"
                className="hidden"
                onChange={handleFileUpload}
              />
              <Paperclip className="w-4 h-4 text-slate-500 hover:text-slate-700 group-hover:text-blue-600 transition-colors" />
              <span className="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 px-2 py-1 bg-slate-800 text-white text-[10px] rounded whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none">
                Upload document for OCR extraction
              </span>
            </label>
            <input
              type="text"
              value={inputMessage}
              onChange={(e) => setInputMessage(e.target.value)}
              placeholder={backendStatus === 'error' ? 'Backend offline...' : 'Describe complaint or edit existing...'}
              disabled={isSending || backendStatus === 'error'}
              className="flex-1 text-xs md:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
            />
            <button
              type="submit"
              disabled={!inputMessage.trim() || isSending || backendStatus === 'error'}
              className="p-2.5 bg-blue-600 hover:bg-blue-700 active:bg-blue-800 text-white rounded-lg transition-all disabled:opacity-40 disabled:hover:bg-blue-600"
            >
              <Send className="w-4 h-4" />
            </button>
          </form>
          <p className="text-[11px] text-slate-400 text-center font-normal">
            AI may contain errors. Verify critical info before applying.
          </p>
        </div>
      </div>
    </div>
  );
};
