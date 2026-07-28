import { useEffect } from 'react';
import { Header } from './components/Header';
import { ComplaintForm } from './components/ComplaintForm';
import { CopilotSidebar } from './components/CopilotSidebar';
import { SavedComplaintsModal } from './components/SavedComplaintsModal';
import { useAppDispatch, useAppSelector } from './store/hooks';
import { updateField, setFormData, setIsAssessingRisk, setNotification, replaceFormData, clearNotification } from './store/formSlice';
import { setSavedComplaints, addComplaint, updateComplaint, deleteComplaint } from './store/complaintsSlice';
import { setActiveTab } from './store/uiSlice';
import { INITIAL_EMPTY_FORM } from './sampleData';
import { ComplaintFormData } from './types';

export default function App() {
  const dispatch = useAppDispatch();
  const formData = useAppSelector((state) => state.form.formData);
  const isExtracting = useAppSelector((state) => state.form.isExtracting);
  const isBlocked = true;
  const isAssessingRisk = useAppSelector((state) => state.form.isAssessingRisk);
  const notification = useAppSelector((state) => state.form.notification);
  const savedComplaints = useAppSelector((state) => state.complaints.savedComplaints);
  const activeTab = useAppSelector((state) => state.ui.activeTab);

  // Initialize from local storage on mount
  useEffect(() => {
    try {
      const stored = localStorage.getItem('pharma_complaints_v1');
      if (stored) {
        dispatch(setSavedComplaints(JSON.parse(stored)));
      } else {
        const sampleRecord: ComplaintFormData = {
          id: 'CMP-2026-0038',
          status: 'Under QA Investigation',
          complaintSource: 'Email Intake',
          customerName: 'Apex Pharmaceuticals Distribution GmbH',
          productName: 'Amoxicillin Trihydrate 500mg FDF Capsules',
          productStrength: '500mg Alu-Alu Blister',
          batchNumber: 'AMX-2026-094',
          manufacturingDate: '2026-03-10',
          expiryDate: '2028-03-09',
          quantityAffected: '240',
          quantityUnit: 'kg',
          complaintType: 'Discoloration & Blister Seal Defect',
          complaintDate: '2026-07-24',
          detailedDescription: 'Brownish capsule discoloration observed in 15 blister packs. Secondary packaging heat seal compromised allowing humidity ingress.',
          suggestedSeverity: 'Major',
          suggestedNextAction: 'Route to QA Investigation & Issue Replacement',
          riskAssessment: 'Potential moisture ingress or primary packaging seal failure leading to capsule discoloration. Requires immediate retain sample inspection and CAPA review.',
          createdAt: new Date().toISOString(),
        };
        dispatch(setSavedComplaints([sampleRecord]));
        localStorage.setItem('pharma_complaints_v1', JSON.stringify([sampleRecord]));
      }
    } catch (e) {
      console.error('Failed loading localStorage:', e);
    }
  }, [dispatch]);

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

  const handleSaveComplaint = () => {
    const newId = formData.id || `CMP-2026-${Math.floor(1000 + Math.random() * 9000)}`;
    const recordToSave: ComplaintFormData = {
      ...formData,
      id: newId,
      createdAt: new Date().toISOString(),
    };

    const existingIndex = savedComplaints.findIndex((c) => c.id === newId);
    if (existingIndex >= 0) {
      dispatch(updateComplaint(recordToSave));
    } else {
      dispatch(addComplaint(recordToSave));
    }
    localStorage.setItem('pharma_complaints_v1', JSON.stringify(
      existingIndex >= 0
        ? savedComplaints.map((c, i) => i === existingIndex ? recordToSave : c)
        : [recordToSave, ...savedComplaints]
    ));
    dispatch(replaceFormData(recordToSave));
    showNotification(`Complaint ${newId} saved to database.`, 'success');
  };

  const handleAssessRisk = async () => {
    dispatch(setIsAssessingRisk(true));
    try {
      const res = await fetch('/api/assess-risk', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ currentForm: formData }),
      });
      const result = await res.json();
      if (!res.ok || !result.success) {
        throw new Error(result.error || 'Failed to re-assess risk');
      }

      dispatch(setFormData({
        suggestedSeverity: result.data.suggestedSeverity || formData.suggestedSeverity,
        suggestedNextAction: result.data.suggestedNextAction || formData.suggestedNextAction,
        riskAssessment: result.data.riskAssessment || formData.riskAssessment,
      }));
      showNotification('AI Risk Assessment re-evaluated successfully.', 'success');
    } catch (err: any) {
      console.error('Risk assessment error:', err);
      showNotification(`Risk assessment warning: ${err.message}`, 'error');
    } finally {
      dispatch(setIsAssessingRisk(false));
    }
  };

  const handleDeleteComplaint = (id: string) => {
    dispatch(deleteComplaint(id));
    localStorage.setItem('pharma_complaints_v1', JSON.stringify(
      savedComplaints.filter((c) => c.id !== id)
    ));
    showNotification(`Complaint ${id} removed.`, 'info');
  };

  return (
    <div className="min-h-screen bg-[#faf8ff] text-slate-900 font-sans flex flex-col">
      <Header
        savedCount={savedComplaints.length}
        onNewComplaint={() => {
          dispatch(replaceFormData(INITIAL_EMPTY_FORM));
          dispatch(setActiveTab('form'));
        }}
        onOpenSavedModal={() => dispatch(setActiveTab('logs'))}
      />

      {/* Floating toast notification */}
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

      {/* Main Content Layout */}
      <main className="flex-1 max-w-7xl w-full mx-auto p-4 md:p-6">
        {activeTab === 'logs' ? (
          <SavedComplaintsModal
            complaints={savedComplaints}
            onSelectComplaint={(c) => {
              dispatch(replaceFormData(c));
              dispatch(setActiveTab('form'));
            }}
            onDeleteComplaint={handleDeleteComplaint}
            onBackToForm={() => dispatch(setActiveTab('form'))}
          />
        ) : (
          <div className="flex flex-col lg:flex-row gap-6 items-start">
            {/* Left 7 Columns: Form (scrollable) */}
            <div className="w-full lg:w-7/12 lg:max-w-[58%] flex-1 min-w-0">
              <div className="h-[calc(100vh-8rem)] overflow-y-auto pr-2 lg:pr-4">
                <ComplaintForm
                  formData={formData}
                  onChange={handleFieldChange}
                  onReset={handleResetForm}
                  onSave={handleSaveComplaint}
                  onAssessRisk={handleAssessRisk}
                  isExtracting={isExtracting}
                  isAssessingRisk={isAssessingRisk}
                  isBlocked={isBlocked}
                />
              </div>
            </div>

            {/* Right 5 Columns: AI Copilot Sidebar (sticky) */}
            <div className="w-full lg:w-5/12 lg:max-w-[42%] shrink-0">
              <CopilotSidebar
                currentForm={formData}
              />
            </div>
          </div>
        )}
      </main>
    </div>
  );
}