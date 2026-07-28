import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { ComplaintFormData } from '../types';

interface ComplaintsState {
  savedComplaints: ComplaintFormData[];
}

const initialState: ComplaintsState = {
  savedComplaints: [],
};

const complaintsSlice = createSlice({
  name: 'complaints',
  initialState,
  reducers: {
    setSavedComplaints: (state, action: PayloadAction<ComplaintFormData[]>) => {
      state.savedComplaints = action.payload;
    },
    addComplaint: (state, action: PayloadAction<ComplaintFormData>) => {
      state.savedComplaints = [action.payload, ...state.savedComplaints];
    },
    updateComplaint: (state, action: PayloadAction<ComplaintFormData>) => {
      const index = state.savedComplaints.findIndex(c => c.id === action.payload.id);
      if (index >= 0) {
        state.savedComplaints[index] = action.payload;
      }
    },
    deleteComplaint: (state, action: PayloadAction<string>) => {
      state.savedComplaints = state.savedComplaints.filter(c => c.id !== action.payload);
    },
  },
});

export const {
  setSavedComplaints,
  addComplaint,
  updateComplaint,
  deleteComplaint,
} = complaintsSlice.actions;

export default complaintsSlice.reducer;