import { useState, useCallback } from 'react';
import { Header } from './components/Header';
import { ComplaintForm } from './components/ComplaintForm';
import { CopilotChat } from './components/CopilotChat';
import { useAppDispatch, useAppSelector } from './store/hooks';
import { updateField, setNotification, replaceFormData, clearNotification, clearHighlightedFields } from './store/formSlice';
import { INITIAL_EMPTY_FORM } from './sampleData';
import { ComplaintFormData } from './types';
import { X } from 'lucide-react';

export default function App() {
  const dispatch = useAppDispatch();
  const formData = useAppSelector((state) => state.form.formData);
  const notification = useAppSelector((state) => state.form.notification);
  const highlightedFields = useAppSelector((state) => state.form.highlightedFields);
  const [showSavePopup, setShowSavePopup] = useState(false);
  const [savedFormData, setSavedFormData] = useState<ComplaintFormData | null>(null);

  const showNotification = (message: string, type: 'success' | 'info' | 'error' = 'info') => {
    dispatch(setNotification({ message, type }));
    setTimeout(() => {
      dispatch(clearNotification());
    }, 4000);
  };

  const handleFieldChange = (field: keyof ComplaintFormData, value: string) => {
    dispatch(updateField({ field, value }));
  };

  const handleResetForm = () => {
    dispatch(replaceFormData(INITIAL_EMPTY_FORM));
    showNotification('Form cleared.', 'info');
  };

  const handleSaveComplaint = useCallback(() => {
    const snapshot = { ...formData };
    snapshot.id = snapshot.id || ('PREVIEW-' + Date.now().toString(36));
    setSavedFormData(snapshot);
    setShowSavePopup(true);
    showNotification('Complaint preview ready.', 'success');
  }, [formData, showNotification]);

  const handleClosePopup = () => {
    setShowSavePopup(false);
    setSavedFormData(null);
  };

  const fieldLabels: Record<string, string> = {
    status: 'Status',
    complaintSource: 'Complaint Source',
    customerName: 'Customer Name',
    productName: 'Product Name',
    productStrength: 'Product Strength',
    batchNumber: 'Batch Number',
    manufacturingDate: 'Manufacturing Date',
    expiryDate: 'Expiry Date',
    quantityAffected: 'Quantity Affected',
    quantityUnit: 'Unit',
    complaintType: 'Complaint Type',
    complaintDate: 'Complaint Date',
    detailedDescription: 'Detailed Description',
    suggestedSeverity: 'Severity',
    suggestedNextAction: 'Suggested Next Action',
    riskAssessment: 'Risk Assessment',
  };

  return (
    <div className="min-h-screen bg-[#faf8ff] text-slate-900 font-sans flex flex-col">
      <Header
        onNewComplaint={() => {
          dispatch(replaceFormData(INITIAL_EMPTY_FORM));
        }}
      />

      {notification && (
        <div className="fixed bottom-5 right-5 z-50 animate-bounce">
          <div
            className={`px-4 py-3 rounded-lg shadow-lg border text-xs font-semibold flex items-center gap-2 ${
              notification.type === 'success'
                ? 'bg-emerald-600 text-white border-emerald-500'
                : notification.type === 'error'
                ? 'bg-red-600 text-white border-red-500'
                : 'bg-slate-800 text-white border-slate-700'
            }`}
          >
            <span>{notification.message}</span>
          </div>
        </div>
      )}

      {/* Save Preview Popup */}
      {showSavePopup && savedFormData && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40 backdrop-blur-sm">
          <div className="bg-white rounded-2xl shadow-2xl border border-slate-200 w-full max-w-2xl max-h-[85vh] overflow-y-auto mx-4">
            <div className="sticky top-0 bg-white border-b border-slate-100 px-6 py-4 flex items-center justify-between rounded-t-2xl z-10">
              <div>
                <h2 className="text-lg font-bold text-slate-900 tracking-tight">Complaint Preview</h2>
                <p className="text-xs text-slate-500 mt-0.5">Review the complaint data before finalizing</p>
              </div>
              <button
                onClick={handleClosePopup}
                className="p-2 hover:bg-slate-100 text-slate-500 rounded-lg transition-all"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            <div className="px-6 py-4 space-y-4">
              {Object.entries(fieldLabels).map(([key, label]) => {
                const value = (savedFormData as any)[key];
                if (!value || (typeof value === 'string' && !value.trim())) return null;
                return (
                  <div key={key} className="border-b border-slate-50 pb-2 last:border-0">
                    <span className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">{label}</span>
                    <p className="text-sm text-slate-800 mt-0.5 font-medium">{value}</p>
                  </div>
                );
              })}
            </div>

            <div className="sticky bottom-0 bg-slate-50 border-t border-slate-100 px-6 py-4 flex justify-end rounded-b-2xl">
              <button
                onClick={handleClosePopup}
                className="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white text-sm font-semibold rounded-lg transition-all shadow-2xs"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}

      <main className="flex-1 max-w-7xl w-full mx-auto p-4 md:p-6">
        <div className="flex gap-4 lg:gap-6">
          <div className="flex-1 min-w-0">
            <div className="h-[calc(100vh-8rem)] overflow-y-auto pr-1 lg:pr-2">
              <ComplaintForm
                formData={formData}
                onChange={handleFieldChange}
                onReset={handleResetForm}
                onSave={handleSaveComplaint}
                highlightedFields={highlightedFields}
                onClearHighlights={() => dispatch(clearHighlightedFields())}
              />
            </div>
          </div>
          <div className="w-80 xl:w-96 shrink-0 hidden lg:block">
            <div className="h-[calc(100vh-8rem)]">
              <CopilotChat />
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
