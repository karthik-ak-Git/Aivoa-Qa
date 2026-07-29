import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { ComplaintFormData } from '../types';

interface FormState {
  formData: ComplaintFormData;
  isAssessingRisk: boolean;
  notification: { type: 'success' | 'info' | 'error'; message: string } | null;
  highlightedFields: string[];
}

const initialState: FormState = {
  formData: {
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
  },
  isAssessingRisk: false,
  notification: null,
  highlightedFields: [],
};

const formSlice = createSlice({
  name: 'form',
  initialState,
  reducers: {
    setFormData: (state, action: PayloadAction<Partial<ComplaintFormData>>) => {
      state.formData = { ...state.formData, ...action.payload };
    },
    replaceFormData: (state, action: PayloadAction<ComplaintFormData>) => {
      const changed: string[] = [];
      for (const key of Object.keys(action.payload) as (keyof ComplaintFormData)[]) {
        if (action.payload[key] !== state.formData[key]) {
          changed.push(key);
        }
      }
      state.formData = action.payload;
      state.highlightedFields = changed;
    },
    updateField: (state, action: PayloadAction<{ field: keyof ComplaintFormData; value: string }>) => {
      (state.formData as any)[action.payload.field] = action.payload.value;
    },
    setStatus: (state, action: PayloadAction<'Pending Triage' | 'Under QA Investigation' | 'CAPA Initiated' | 'Closed'>) => {
      state.formData.status = action.payload;
    },
    setIsAssessingRisk: (state, action: PayloadAction<boolean>) => {
      state.isAssessingRisk = action.payload;
    },
    setNotification: (state, action: PayloadAction<{ type: 'success' | 'info' | 'error'; message: string } | null>) => {
      state.notification = action.payload;
    },
    clearNotification: (state) => {
      state.notification = null;
    },
    clearHighlightedFields: (state) => {
      state.highlightedFields = [];
    },
    resetForm: (state, action: PayloadAction<ComplaintFormData>) => {
      state.formData = action.payload;
    },
  },
});

export const {
  setFormData,
  replaceFormData,
  updateField,
  setStatus,
  setIsAssessingRisk,
  setNotification,
  clearNotification,
  clearHighlightedFields,
  resetForm,
} = formSlice.actions;

export default formSlice.reducer;