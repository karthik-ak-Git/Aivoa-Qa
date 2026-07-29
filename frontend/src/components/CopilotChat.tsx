import { useRef, useState } from 'react';
import { Send, Loader2, Bot, Plus } from 'lucide-react';
import { useAppDispatch, useAppSelector } from '../store/hooks';
import { addChatMessage, setIsSending } from '../store/uiSlice';
import { replaceFormData, setNotification } from '../store/formSlice';
import type { ComplaintFormData } from '../types';
import * as api from '../services/api';

function formatSummary(data: Partial<ComplaintFormData>): string {
  const lines: string[] = [];
  const label = data.customerName ? `for **${data.customerName}**` : '';
  const product = data.productName ? `**${data.productName}**` : '';
  if (product) lines.push(`- Product: ${product} ${label}`);
  if (data.complaintType) lines.push(`- Type: ${data.complaintType}`);
  if (data.suggestedSeverity) lines.push(`- Severity: **${data.suggestedSeverity}**`);
  if (data.detailedDescription) {
    const shortened = data.detailedDescription.length > 80
      ? data.detailedDescription.slice(0, 80) + '…'
      : data.detailedDescription;
    lines.push(`- Description: ${shortened}`);
  }
  return lines.length > 0 ? lines.join('\n') : 'Form updated.';
}

export const CopilotChat: React.FC = () => {
  const dispatch = useAppDispatch();
  const chatMessages = useAppSelector((state) => state.ui.chatMessages);
  const isSending = useAppSelector((state) => state.ui.isSending);
  const formData = useAppSelector((state) => state.form.formData);
  const [input, setInput] = useState('');
  const fileInputRef = useRef<HTMLInputElement>(null);

  const sendMessage = async (text: string) => {
    if (!text.trim() || isSending) return;
    const trimmed = text.trim();

    dispatch(addChatMessage({
      id: `user-${Date.now()}`,
      role: 'user',
      content: trimmed,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    }));
    setInput('');
    dispatch(setIsSending(true));

    try {
      const result = await api.copilotWrite(trimmed, formData as unknown as Record<string, unknown>);
      dispatch(replaceFormData(result.form_data as any));
      dispatch(addChatMessage({
        id: `assistant-${Date.now()}`,
        role: 'assistant',
        content: `✅ Complaint updated (${(result.confidence * 100).toFixed(0)}% confidence)\n\n${formatSummary(result.form_data)}\n\n_Agent: ${result.agent_used}_`,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      }));
    } catch (err: any) {
      dispatch(addChatMessage({
        id: `error-${Date.now()}`,
        role: 'system',
        content: `Error: ${err.message}`,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      }));
    } finally {
      dispatch(setIsSending(false));
    }
  };

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    dispatch(addChatMessage({
      id: `user-${Date.now()}`,
      role: 'user',
      content: `📎 Uploaded: ${file.name}`,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    }));
    dispatch(setIsSending(true));

    try {
      const text = await file.text();
      const result = await api.copilotExtractText(text, file.name);
      dispatch(replaceFormData(result.form_data as any));
      dispatch(setNotification({ type: 'success', message: `Extracted from ${file.name}` }));
      dispatch(addChatMessage({
        id: `assistant-${Date.now()}`,
        role: 'assistant',
        content: `📄 Data extracted from **${file.name}** (${(result.confidence * 100).toFixed(0)}% confidence)\n\n${formatSummary(result.form_data)}\n\n_Agent: ${result['agent_used']}_`,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      }));
    } catch (err: any) {
      dispatch(setNotification({ type: 'error', message: `Failed to extract: ${err.message}` }));
    } finally {
      dispatch(setIsSending(false));
      if (fileInputRef.current) fileInputRef.current.value = '';
    }
  };

  return (
    <div className="h-full flex flex-col bg-white rounded-xl border border-slate-200/80 shadow-2xs">
      <div className="flex items-center gap-2 px-5 py-3.5 border-b border-slate-100">
        <div className="p-1.5 bg-blue-50 text-blue-600 rounded-lg">
          <Bot className="w-4 h-4" />
        </div>
        <div>
          <h3 className="text-sm font-semibold text-slate-800">AI Copilot</h3>
          <p className="text-[11px] text-slate-400">Write & edit complaints</p>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto p-4 space-y-3">
        {chatMessages.map((msg) => (
          <div key={msg.id} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
            <div
              className={`max-w-[85%] rounded-xl px-3.5 py-2.5 text-xs leading-relaxed whitespace-pre-wrap ${
                msg.role === 'user'
                  ? 'bg-blue-600 text-white'
                  : msg.role === 'system'
                  ? 'bg-red-50 text-red-700 border border-red-100'
                  : 'bg-slate-50 text-slate-700 border border-slate-100'
              }`}
            >
              {msg.content}
            </div>
          </div>
        ))}
        {isSending && (
          <div className="flex justify-start">
            <div className="bg-slate-50 border border-slate-100 rounded-xl px-3.5 py-2.5 flex items-center gap-2 text-xs text-slate-400">
              <Loader2 className="w-3.5 h-3.5 animate-spin" />
              Thinking...
            </div>
          </div>
        )}
      </div>

      <div className="border-t border-slate-100 p-3 space-y-2">
        <div className="flex gap-2">
          <input
            type="file"
            accept=".txt,.csv,.eml,.msg,.pdf"
            ref={fileInputRef}
            onChange={handleFileUpload}
            className="hidden"
          />
          <button
            type="button"
            onClick={() => fileInputRef.current?.click()}
            disabled={isSending}
            className="p-2 text-slate-400 hover:text-blue-600 hover:bg-blue-50 rounded-lg transition-all disabled:opacity-40"
            title="Upload document for extraction"
          >
            <Plus className="w-4 h-4" />
          </button>
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && sendMessage(input)}
            placeholder="Describe a complaint or edit instruction..."
            className="flex-1 text-xs px-3 py-2.5 bg-slate-50 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500"
          />
          <button
            type="button"
            onClick={() => sendMessage(input)}
            disabled={isSending || !input.trim()}
            className="p-2.5 bg-blue-600 hover:bg-blue-700 disabled:opacity-40 text-white rounded-lg transition-all"
          >
            <Send className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  );
};
