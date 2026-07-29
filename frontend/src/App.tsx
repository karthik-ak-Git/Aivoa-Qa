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
import * as api from './services/api';

export default function App() {
  const dispatch = useAppDispatch();
  const formData = useAppSelector((state) => state.form.formData);
  const isExtracting = useAppSelector((state) => state.form.isExtracting);
  const isBlocked = isExtracting;
  const isAssessingRisk = useAppSelector((state) => state.form.isAssessingRisk);
  const notification = useAppSelector((state) => state.form.notification);
  const savedComplaints = useAppSelector((state) => state.complaints.savedComplaints);
  const activeTab = useAppSelector((state) => state.ui.activeTab);

  // Load complaints from backend on mount
  useEffect(() => {
    api.fetchComplaints()
      .then((complaints) => {
        if (complaints.length > 0) {
          dispatch(setSavedComplaints(complaints));
        } else {
          // Seed with sample data on first load
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
          api.createComplaint(sampleRecord).then((created) => {
            dispatch(setSavedComplaints([created]));
          }).catch(() => {
            dispatch(setSavedComplaints([sampleRecord]));
          });
        }
      })
      .catch(() => {
        // Backend offline — fall back to localStorage
        try {
          const stored = localStorage.getItem('pharma_complaints_v1');
          if (stored) dispatch(setSavedComplaints(JSON.parse(stored)));
        } catch { /* ignore */ }
      });
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

  const handleSaveComplaint = async () => {
    try {
      const existingId = savedComplaints.find(
        (c) => c.productName === formData.productName && c.batchNumber === formData.batchNumber && c.id,
      )?.id;

      let saved: ComplaintFormData;
      if (existingId) {
        saved = await api.updateComplaint(existingId, formData);
        dispatch(updateComplaint(saved));
      } else {
        saved = await api.createComplaint(formData);
        dispatch(addComplaint(saved));
      }
      dispatch(replaceFormData(saved));
      showNotification(`Complaint ${saved.id} saved to database.`, 'success');
    } catch (err: any) {
      console.error('Save failed:', err);
      showNotification(`Save failed: ${err.message}`, 'error');
    }
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

  const handleDeleteComplaint = async (id: string) => {
    try {
      await api.deleteComplaint(id);
      dispatch(deleteComplaint(id));
      showNotification(`Complaint ${id} removed.`, 'info');
    } catch (err: any) {
      console.error('Delete failed:', err);
      showNotification(`Delete failed: ${err.message}`, 'error');
    }
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