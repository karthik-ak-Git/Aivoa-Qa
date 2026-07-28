import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface UIState {
  activeTab: 'form' | 'logs';
  sidebarTab: 'chat' | 'extractor';
  chatMessages: Array<{
    id: string;
    role: 'user' | 'assistant' | 'system';
    content: string;
    timestamp: string;
  }>;
  isSending: boolean;
  rawText: string;
  selectedSample: string;
  searchTerm: string;
  statusFilter: string;
  severityFilter: string;
}

const initialState: UIState = {
  activeTab: 'form',
  sidebarTab: 'chat',
  chatMessages: [
    {
      id: 'welcome-1',
      role: 'assistant',
      content: `Hello! I am your AI Quality Assurance Copilot for API & FDF complaints.
Ask me anything about regulatory compliance, root cause analysis (ICH Q9), or draft customer responses based on the current form details.`,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    },
  ],
  isSending: false,
  rawText: '',
  selectedSample: '',
  searchTerm: '',
  statusFilter: 'ALL',
  severityFilter: 'ALL',
};

const uiSlice = createSlice({
  name: 'ui',
  initialState,
  reducers: {
    setActiveTab: (state, action: PayloadAction<'form' | 'logs'>) => {
      state.activeTab = action.payload;
    },
    setSidebarTab: (state, action: PayloadAction<'chat' | 'extractor'>) => {
      state.sidebarTab = action.payload;
    },
    addChatMessage: (state, action: PayloadAction<UIState['chatMessages'][0]>) => {
      state.chatMessages.push(action.payload);
    },
    setChatMessages: (state, action: PayloadAction<UIState['chatMessages']>) => {
      state.chatMessages = action.payload;
    },
    setIsSending: (state, action: PayloadAction<boolean>) => {
      state.isSending = action.payload;
    },
    setRawText: (state, action: PayloadAction<string>) => {
      state.rawText = action.payload;
    },
    setSelectedSample: (state, action: PayloadAction<string>) => {
      state.selectedSample = action.payload;
    },
    setSearchTerm: (state, action: PayloadAction<string>) => {
      state.searchTerm = action.payload;
    },
    setStatusFilter: (state, action: PayloadAction<string>) => {
      state.statusFilter = action.payload;
    },
    setSeverityFilter: (state, action: PayloadAction<string>) => {
      state.severityFilter = action.payload;
    },
  },
});

export const {
  setActiveTab,
  setSidebarTab,
  addChatMessage,
  setChatMessages,
  setIsSending,
  setRawText,
  setSelectedSample,
  setSearchTerm,
  setStatusFilter,
  setSeverityFilter,
} = uiSlice.actions;

export default uiSlice.reducer;