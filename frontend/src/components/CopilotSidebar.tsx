import React, { useRef, useEffect, useState } from 'react';
import { Send, Bot, MessageSquare, Paperclip, FileText, Loader2, CheckCircle, Zap, ScanLine, Brain } from 'lucide-react';
import { useAppDispatch, useAppSelector } from '../store/hooks';
import { addChatMessage, setIsSending } from '../store/uiSlice';

interface CopilotSidebarProps {
  currentForm: any;
}

export const CopilotSidebar: React.FC<CopilotSidebarProps> = ({
  currentForm,
}) => {
  const dispatch = useAppDispatch();
  const chatMessages = useAppSelector((state) => state.ui.chatMessages);
  const isSending = useAppSelector((state) => state.ui.isSending);
  const [inputMessage, setInputMessage] = React.useState('');
  const chatEndRef = useRef<HTMLDivElement>(null);
  
  // Upload animation states
  const [uploadState, setUploadState] = useState<'idle' | 'uploading' | 'ocr_processing' | 'form_filling' | 'complete'>('idle');
  const [uploadedFile, setUploadedFile] = useState<{ name: string; type: string; progress: number } | null>(null);
  const [ocrProgress, setOcrProgress] = useState(0);
  
  // Chat thinking state
  const [thinkingStage, setThinkingStage] = useState<'idle' | 'loading_knowledge' | 'thinking' | 'form_filling' | 'complete'>('idle');

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [chatMessages]);

  const simulateUploadAnimation = async (file: File) => {
    setUploadedFile({ name: file.name, type: file.type || 'document', progress: 0 });
    setUploadState('uploading');
    
    // Simulate upload progress
    for (let i = 0; i <= 100; i += 10) {
      await new Promise(r => setTimeout(r, 50));
      setUploadedFile(prev => prev ? { ...prev, progress: i } : null);
    }
    
    // OCR processing animation
    setUploadState('ocr_processing');
    setOcrProgress(0);
    const ocrStages = [
      { progress: 15, label: 'Initializing OCR engine...' },
      { progress: 30, label: 'Detecting document layout...' },
      { progress: 50, label: 'Extracting text regions...' },
      { progress: 70, label: 'Recognizing characters...' },
      { progress: 85, label: 'Structuring data fields...' },
      { progress: 100, label: 'OCR complete!' },
    ];
    
    for (const stage of ocrStages) {
      await new Promise(r => setTimeout(r, 400));
      setOcrProgress(stage.progress);
    }
    
    // Form filling animation
    setUploadState('form_filling');
    await new Promise(r => setTimeout(r, 500));
    
    setUploadState('complete');
    await new Promise(r => setTimeout(r, 1000));
    
    // Reset and add completion message
    dispatch(addChatMessage({
      id: `msg-${Date.now()}`,
      role: 'assistant',
      content: `✅ Document "${file.name}" processed successfully! All fields have been extracted and populated in the complaint form.`,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    }));
    
    setUploadState('idle');
    setUploadedFile(null);
    setOcrProgress(0);
  };

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        // Add user message with file info
        dispatch(addChatMessage({
          id: `msg-${Date.now()}`,
          role: 'user',
          content: `📎 Uploaded document: ${file.name} (${(file.size / 1024).toFixed(1)} KB)`,
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        }));
        // Start animation
        simulateUploadAnimation(file);
      };
      reader.readAsText(file);
    }
    // Reset input
    e.target.value = '';
  };

  const simulateChatAnimation = async (query: string) => {
    // Use currentForm for context-aware response
    const formContext = currentForm ? ` (Product: ${currentForm.productName || 'N/A'}, Batch: ${currentForm.batchNumber || 'N/A'})` : '';
    const userMsg = {
      id: `msg-${Date.now()}`,
      role: 'user' as const,
      content: query.trim(),
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    };

    dispatch(addChatMessage(userMsg));
    setInputMessage('');
    dispatch(setIsSending(true));
    
    // Stage 1: Loading knowledge
    setThinkingStage('loading_knowledge');
    await new Promise(r => setTimeout(r, 800));
    
    // Stage 2: Thinking
    setThinkingStage('thinking');
    await new Promise(r => setTimeout(r, 1200));
    
    // Stage 3: Form filling
    setThinkingStage('form_filling');
    await new Promise(r => setTimeout(r, 800));
    
    // Stage 4: Complete
    setThinkingStage('complete');
    
    dispatch(addChatMessage({
      id: `msg-${Date.now() + 1}`,
      role: 'assistant',
      content: `Based on your question about "${query.trim().slice(0, 50)}..."${formContext}, I've analyzed the complaint details and populated the relevant fields in the form. The risk assessment has been updated with ICH Q9 guidance.`,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    }));
    
    await new Promise(r => setTimeout(r, 500));
    setThinkingStage('idle');
    dispatch(setIsSending(false));
  };

  const handleSendMessage = async (textToSend?: string) => {
    const query = textToSend || inputMessage;
    if (!query.trim() || isSending) return;
    
    // Check if it's a file attachment message
    if (query.startsWith('[Attached file:')) {
      return; // Already handled in handleFileUpload
    }
    
    await simulateChatAnimation(query);
  };

  return (
    <div className="bg-white rounded-xl border border-slate-200/80 shadow-2xs flex flex-col h-[calc(100vh-8rem)] sticky top-20">
      {/* Sidebar Top Header */}
      <div className="p-3 border-b border-slate-100 flex items-center justify-between bg-slate-50/50 rounded-t-xl">
        <div className="flex items-center gap-1.5 text-blue-700 font-semibold text-xs md:text-sm">
          <MessageSquare className="w-3.5 h-3.5" />
          AI QA Copilot
        </div>
      </div>

      {/* AI Chat View */}
      <div className="flex-1 flex flex-col min-h-0">
        {/* Messages Area */}
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

          {/* Thinking Animation Overlay */}
          {thinkingStage !== 'idle' && (
            <div className="flex items-center gap-3 text-xs md:text-sm justify-start animate-slide-up">
              <div className="w-7 h-7 rounded-full bg-gradient-to-br from-blue-500 to-purple-500 text-white flex items-center justify-center shrink-0 text-xs font-bold mt-0.5 animate-pulse">
                <Brain className="w-4 h-4" />
              </div>
              <div className="max-w-[85%] rounded-xl p-3.5 space-y-2 bg-gradient-to-r from-blue-50 to-purple-50 border border-blue-100/50 rounded-bl-2xs">
                <div className="flex items-center gap-2 text-blue-700 font-medium">
                  <Loader2 className="w-4 h-4 animate-spin" />
                  <span>{thinkingStage === 'loading_knowledge' && 'Loading knowledge base...'}</span>
                  <span>{thinkingStage === 'thinking' && 'Analyzing with ICH Q9 framework...'}</span>
                  <span>{thinkingStage === 'form_filling' && 'Populating form fields...'}</span>
                  <span>{thinkingStage === 'complete' && 'Ready!'}
                    <CheckCircle className="w-3.5 h-3.5 ml-1 text-green-500" />
                  </span>
                </div>
                {/* Animated dots */}
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

          {/* Upload Animation */}
          {uploadState !== 'idle' && uploadedFile && (
            <div className="flex items-start gap-3 text-xs md:text-sm justify-start animate-slide-up">
              <div className="w-7 h-7 rounded-full bg-gradient-to-br from-amber-500 to-orange-500 text-white flex items-center justify-center shrink-0 text-xs font-bold mt-0.5">
                <FileText className="w-4 h-4" />
              </div>
              <div className="max-w-[85%] rounded-xl p-3.5 space-y-2 bg-gradient-to-r from-amber-50 to-orange-50 border border-amber-100/50 rounded-bl-2xs">
                {/* File info */}
                <div className="flex items-center gap-2 text-amber-800">
                  <FileText className="w-4 h-4" />
                  <div className="flex-1 min-w-0">
                    <p className="font-medium truncate">{uploadedFile.name}</p>
                    <p className="text-[10px] text-amber-600">{uploadedFile.type}</p>
                  </div>
                </div>
                
                {/* Progress bar */}
                <div className="w-full h-2 bg-amber-100 rounded-full overflow-hidden">
                  <div
                    className="h-full bg-gradient-to-r from-amber-500 to-orange-500 rounded-full transition-all duration-300"
                    style={{ width: `${uploadedFile.progress}%` }}
                  />
                </div>
                <p className="text-[10px] text-amber-600 text-right">{uploadedFile.progress}%</p>
                
                {/* OCR stages */}
                {uploadState === 'ocr_processing' && (
                  <div className="space-y-1.5 pt-1 border-t border-amber-200/50">
                    <p className="text-[10px] font-medium text-amber-700 flex items-center gap-1">
                      <ScanLine className="w-3 h-3 animate-pulse" />
                      OCR Processing
                    </p>
                    <div className="w-full h-1.5 bg-amber-100 rounded-full overflow-hidden">
                      <div
                        className="h-full bg-gradient-to-r from-blue-500 to-purple-500 rounded-full transition-all duration-500"
                        style={{ width: `${ocrProgress}%` }}
                      />
                    </div>
                    <p className="text-[9px] text-amber-500 text-right font-mono">{ocrProgress}%</p>
                  </div>
                )}
                
                {/* Form filling */}
                {uploadState === 'form_filling' && (
                  <div className="space-y-1.5 pt-1 border-t border-amber-200/50">
                    <p className="text-[10px] font-medium text-amber-700 flex items-center gap-1">
                      <Zap className="w-3 h-3 animate-pulse" />
                      Populating form fields...
                    </p>
                    <div className="flex gap-1">
                      {['Product', 'Batch', 'Risk', 'Action'].map((field, i) => (
                        <div
                          key={field}
                          className="flex-1 h-4 bg-amber-100 rounded animate-pulse"
                          style={{ animationDelay: `${i * 200}ms` }}
                        />
                      ))}
                    </div>
                  </div>
                )}
                
                {uploadState === 'complete' && (
                  <div className="flex items-center gap-2 text-green-700 pt-2">
                    <CheckCircle className="w-4 h-4" />
                    <span className="font-medium">Document processed & form populated!</span>
                  </div>
                )}
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

        {/* Input Box */}
        <div className="p-3 border-t border-slate-200/80 bg-white rounded-b-xl space-y-2">
          <form
            onSubmit={(e) => {
              e.preventDefault();
              handleSendMessage();
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
              {/* Tooltip */}
              <span className="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 px-2 py-1 bg-slate-800 text-white text-[10px] rounded whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none">
                Attach document (PDF, TXT, DOC)
              </span>
            </label>
            <input
              type="text"
              value={inputMessage}
              onChange={(e) => setInputMessage(e.target.value)}
              placeholder={thinkingStage !== 'idle' ? 'Processing...' : 'Ask me anything about this complaint...'}
              disabled={thinkingStage !== 'idle' || uploadState !== 'idle'}
              className="flex-1 text-xs md:text-sm px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
            />
            <button
              type="submit"
              disabled={!inputMessage.trim() || isSending || thinkingStage !== 'idle' || uploadState !== 'idle'}
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
    </div>
  );
};