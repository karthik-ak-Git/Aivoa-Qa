import { configureStore } from '@reduxjs/toolkit';
import formReducer from './formSlice';
import complaintsReducer from './complaintsSlice';
import uiReducer from './uiSlice';

export const store = configureStore({
  reducer: {
    form: formReducer,
    complaints: complaintsReducer,
    ui: uiReducer,
  },
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;