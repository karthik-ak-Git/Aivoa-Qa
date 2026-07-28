import React, { useRef, useEffect } from 'react';
import { Send, Sparkles, Bot, MessageSquare } from 'lucide-react';
import { useAppDispatch, useAppSelector } from '../store/hooks';
import { setSidebarTab, addChatMessage, setIsSending, setRawText, setSelectedSample } from '../store/uiSlice';
import { SAMPLE_EMAIL_TEMPLATES } from '../sampleData';

interface CopilotSidebarProps {
  currentForm: any;
  onExtractText: (rawText: string) => Promise<void>;
  isExtracting: boolean;
}

export const CopilotSidebar: React.FC<CopilotSidebarProps> = ({
  currentForm,
  onExtractText,
  isExtracting,
}) => {
  const dispatch = useAppDispatch();
  const sidebarTab = useAppSelector((state) => state.ui.sidebarTab);
  const chatMessages = useAppSelector((state) => state.ui.chatMessages);
  const isSending = useAppSelector((state) => state.ui.isSending);
  const rawText = useAppSelector((state) => state.ui.rawText);
  const selectedSample = useAppSelector((state) => state.ui.selectedSample);
  const [inputMessage, setInputMessage] = React.useState('');
  const chatEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [chatMessages]);

  const handleSendMessage = async (textToSend?: string) => {
    const query = textToSend || inputMessage;
    if (!query.trim() || isSending) return;

    const userMsg = {
      id: `msg-${Date.now()}`,
      role: 'user' as const,
      content: query.trim(),
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    };

    dispatch(addChatMessage(userMsg));
    setInputMessage('');
    dispatch(setIsSending(true));

    try {
      const res = await fetch('/api/chat-copilot', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: query,
          currentForm,
          history: chatMessages,
        }),
      });

      const data = await res.json();
      if (!res.ok || !data.success) {
        throw new Error(data.error || 'Failed to fetch AI response');
      }

      const assistantMsg = {
        id: `msg-${Date.now() + 1}`,
        role: 'assistant' as const,
        content: data.text,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      };

      dispatch(addChatMessage(assistantMsg));
    } catch (err: any) {
      console.error('Chat error:', err);
      dispatch(addChatMessage({
        id: `msg-err-${Date.now()}`,
        role: 'assistant',
        content: `Sorry, I encountered an issue: ${err.message}. Please check GEMINI_API_KEY settings or try again.`,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      }));
    } finally {
      dispatch(setIsSending(false));
    }
  };

  const handleSampleSelect = (sample: any) => {
    dispatch(setSelectedSample(sample.id));
    dispatch(setRawText(sample.rawText));
  };

  const handleRunExtract = async () => {
    if (!rawText.trim()) return;
    await onExtractText(rawText);
    dispatch(setSidebarTab('chat'));
    dispatch(addChatMessage({
      id: `extract-note-${Date.now()}`,
      role: 'assistant',
      content: `I've extracted the fields into the form! Feel free to ask me for a summary, root cause hypothesis, or to draft a formal customer acknowledgement letter.`,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    }));
  };

  return (
    <div className="bg-white rounded-xl border border-slate-200/80 shadow-2xs flex flex-col h-[calc(100vh-8rem)] sticky top-20">
      {/* Sidebar Top Nav Tabs */}
      <div className="p-3 border-b border-slate-100 flex items-center justify-between bg-slate-50/50 rounded-t-xl">
        <div className="flex items-center gap-1 bg-slate-200/60 p-1 rounded-lg w-full">
          <button
            onClick={() => dispatch(setSidebarTab('chat'))}
            className={`flex-1 py-1.5 px-3 text-xs font-semibold rounded-md flex items-center justify-center gap-1.5 transition-all ${
              sidebarTab === 'chat'
                ? 'bg-white text-blue-700 shadow-2xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            <MessageSquare className="w-3.5 h-3.5" />
            AI QA Copilot
          </button>
          <button
            onClick={() => dispatch(setSidebarTab('extractor'))}
            className={`flex-1 py-1.5 px-3 text-xs font-semibold rounded-md flex items-center justify-center gap-1.5 transition-all ${
              sidebarTab === 'extractor'
                ? 'bg-white text-blue-700 shadow-2xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            <Sparkles className="w-3.5 h-3.5" />
            Auto-Extract Email
          </button>
        </div>
      </div>

      {/* Tab 1: AI Chat View */}
      {sidebarTab === 'chat' && (
        <div className="flex-1 flex flex-col min-h-0">
          {/* Quick Prompts Bar */}
          <div className="p-3 bg-slate-50/30 border-b border-slate-100 flex items-center gap-1.5 overflow-x-auto text-[11px]">
            <span className="text-slate-400 font-medium shrink-0">Prompts:</span>
            <button
              onClick={() => handleSendMessage('Draft a formal customer acknowledgement email for this complaint.')}
              className="shrink-0 px-2.5 py-1 bg-white border border-slate-200 hover:border-blue-300 text-slate-700 hover:text-blue-700 rounded-full transition-all"
            >
              ✉️ Customer Email
            </button>
            <button
              onClick={() => handleSendMessage('What are potential ICH Q9 root causes for this complaint type?')}
              className="shrink-0 px-2.5 py-1 bg-white border border-slate-200 hover:border-blue-300 text-slate-700 hover:text-blue-700 rounded-full transition-all"
            >
              🔍 Root Cause Analysis
            </button>
            <button
              onClick={() => handleSendMessage('Does this issue require a 15-day FDA Field Alert or EU Defect report?')}
              className="shrink-0 px-2.5 py-1 bg-white border border-slate-200 hover:border-blue-300 text-slate-700 hover:text-blue-700 rounded-full transition-all"
            >
              ⚖️ Regulatory Triggers
            </button>
          </div>

          {/* Messages Area */}
          <div className="flex-1 overflow-y-auto p-4 space-y-4">
            {chatMessages.map((msg) => (
              <div
                key={msg.id}
                className={`flex gap-3 text-xs md:text-sm ${
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
            {isSending && (
              <div className="flex items-center gap-2 text-xs text-slate-400 italic">
                <Bot className="w-4 h-4 animate-spin text-blue-500" />
                Copilot is thinking...
              </div>
            )}
            <div ref={chatEndRef} />
          </div>

          {/* Input Box matching prompt screenshot */}
          <div className="p-3 border-t border-slate-200/80 bg-white rounded-b-xl space-y-2">
            <form
              onSubmit={(e) => {
                e.preventDefault();
                handleSendMessage();
              }}
              className="flex items-center gap-2"
            >
              <input
                type="text"
                value={inputMessage}
                onChange={(e) => setInputMessage(e.target.value)}
                placeholder="Ask me anything about this complaint..."
                className="flex-1 text-xs md:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500"
              />
              <button
                type="submit"
                disabled={!inputMessage.trim() || isSending}
                className="p-2.5 bg-blue-600 hover:bg-blue-700 active:bg-blue-800 text-white rounded-lg transition-all disabled:opacity-40 disabled:hover:bg-blue-600"
              >
                <Send className="w-4 h-4" />
              </button>
            </form>
            <p className="text-[11px] text-slate-400 text-center font-normal">
              AI responses may contain errors. Please verify information.
            </p>
          </div>
        </div>
      )}

      {/* Tab 2: Auto-Extractor View */}
      {sidebarTab === 'extractor' && (
        <div className="flex-1 flex flex-col min-h-0 p-4 space-y-4 overflow-y-auto">
          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1.5">
              1-Click Sample Intake Emails
            </label>
            <div className="space-y-2">
              {SAMPLE_EMAIL_TEMPLATES.map((sample) => (
                <button
                  key={sample.id}
                  onClick={() => handleSampleSelect(sample)}
                  className={`w-full text-left p-2.5 rounded-lg border text-xs transition-all ${
                    selectedSample === sample.id
                      ? 'border-blue-500 bg-blue-50/50 text-blue-900 font-medium'
                      : 'border-slate-200 hover:border-slate-300 bg-slate-50/30 text-slate-700'
                  }`}
                >
                  <div className="font-semibold">{sample.title}</div>
                  <div className="text-[11px] text-slate-500 truncate">{sample.subject}</div>
                </button>
              ))}
            </div>
          </div>

          <div className="flex-1 flex flex-col">
            <label className="block text-xs font-semibold text-slate-700 mb-1.5">
              Raw Complaint Text / Email Body
            </label>
            <textarea
              value={rawText}
              onChange={(e) => dispatch(setRawText(e.target.value))}
              placeholder="Paste raw email, customer notice, or quality incident report here..."
              className="flex-1 w-full min-h-[160px] text-xs p-3 bg-slate-50 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 resize-none font-mono"
            />
          </div>

          <button
            onClick={handleRunExtract}
            disabled={!rawText.trim() || isExtracting}
            className="w-full py-2.5 bg-blue-600 hover:bg-blue-700 active:bg-blue-800 text-white rounded-lg text-xs font-semibold flex items-center justify-center gap-2 shadow-2xs transition-all disabled:opacity-50"
          >
            <Sparkles className="w-4 h-4" />
            <span>{isExtracting ? 'Extracting Fields...' : 'Auto-Extract to Form'}</span>
          </button>
        </div>
      )}
    </div>
  );
};