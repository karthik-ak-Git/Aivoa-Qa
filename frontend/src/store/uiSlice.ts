import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface UIState {
  activeTab: 'form' | 'logs';
  chatMessages: Array<{
    id: string;
    role: 'user' | 'assistant' | 'system';
    content: string;
    timestamp: string;
  }>;
  isSending: boolean;
  searchTerm: string;
  statusFilter: string;
  severityFilter: string;
}

const initialState: UIState = {
  activeTab: 'form',
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
    addChatMessage: (state, action: PayloadAction<UIState['chatMessages'][0]>) => {
      state.chatMessages.push(action.payload);
    },
    setChatMessages: (state, action: PayloadAction<UIState['chatMessages']>) => {
      state.chatMessages = action.payload;
    },
    setIsSending: (state, action: PayloadAction<boolean>) => {
      state.isSending = action.payload;
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
  addChatMessage,
  setChatMessages,
  setIsSending,
  setSearchTerm,
  setStatusFilter,
  setSeverityFilter,
} = uiSlice.actions;

export default uiSlice.reducer;