import React from 'react';
import { ShieldCheck, FolderKanban, PlusCircle } from 'lucide-react';
import { useAppDispatch, useAppSelector } from '../store/hooks';
import { setActiveTab } from '../store/uiSlice';
import { setStatus } from '../store/formSlice';

interface HeaderProps {
  savedCount: number;
  onNewComplaint: () => void;
  onOpenSavedModal: () => void;
}

export const Header: React.FC<HeaderProps> = ({
  savedCount,
  onNewComplaint,
  onOpenSavedModal,
}) => {
  const dispatch = useAppDispatch();
  const status = useAppSelector((state) => state.form.formData.status);
  const activeTab = useAppSelector((state) => state.ui.activeTab);

  const getStatusBadgeStyle = (currentStatus: string) => {
    switch (currentStatus) {
      case 'Pending Triage':
        return 'bg-amber-50 text-amber-800 border-amber-200';
      case 'Under QA Investigation':
        return 'bg-blue-50 text-blue-800 border-blue-200';
      case 'CAPA Initiated':
        return 'bg-purple-50 text-purple-800 border-purple-200';
      case 'Closed':
        return 'bg-emerald-50 text-emerald-800 border-emerald-200';
      default:
        return 'bg-amber-50 text-amber-800 border-amber-200';
    }
  };

  const handleStatusChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    dispatch(setStatus(e.target.value as 'Pending Triage' | 'Under QA Investigation' | 'CAPA Initiated' | 'Closed'));
  };

  return (
    <header className="bg-white border-b border-slate-200 px-6 py-4 shadow-2xs sticky top-0 z-20">
      <div className="max-w-7xl mx-auto flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center gap-2">
            <span className="p-1.5 bg-blue-50 text-blue-700 rounded-md">
              <ShieldCheck className="w-5 h-5" />
            </span>
            <h1 className="text-2xl font-bold text-slate-900 tracking-tight">Log Customer Complaint</h1>
          </div>
          <p className="text-xs font-medium text-slate-500 mt-0.5 tracking-wider uppercase">
            API & FDF Quality Assurance Module
          </p>
        </div>

        <div className="flex items-center flex-wrap gap-3 w-full sm:w-auto justify-between sm:justify-end">
          {/* Status Dropdown Pill */}
          <div className="flex items-center gap-1.5">
            <span className="text-xs font-medium text-slate-500">Status:</span>
            <select
              value={status}
              onChange={handleStatusChange}
              className={`text-xs font-semibold px-3 py-1.5 rounded-full border cursor-pointer focus:outline-none transition-colors ${getStatusBadgeStyle(status)}`}
            >
              <option value="Pending Triage">Pending Triage</option>
              <option value="Under QA Investigation">Under QA Investigation</option>
              <option value="CAPA Initiated">CAPA Initiated</option>
              <option value="Closed">Closed</option>
            </select>
          </div>

          <div className="h-5 w-px bg-slate-200 hidden sm:block" />

          {/* Navigation Buttons */}
          <div className="flex items-center gap-2">
            <button
              onClick={onNewComplaint}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium flex items-center gap-1.5 transition-all ${
                activeTab === 'form'
                  ? 'bg-blue-600 text-white shadow-2xs hover:bg-blue-700'
                  : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
              }`}
            >
              <PlusCircle className="w-3.5 h-3.5" />
              New Complaint
            </button>

            <button
              onClick={() => {
                dispatch(setActiveTab('logs'));
                onOpenSavedModal();
              }}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium flex items-center gap-1.5 transition-all ${
                activeTab === 'logs'
                  ? 'bg-blue-600 text-white shadow-2xs hover:bg-blue-700'
                  : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
              }`}
            >
              <FolderKanban className="w-3.5 h-3.5" />
              Complaint Register
              {savedCount > 0 && (
                <span className="ml-1 px-1.5 py-0.2 bg-blue-100 text-blue-800 text-[10px] font-bold rounded-full">
                  {savedCount}
                </span>
              )}
            </button>
          </div>
        </div>
      </div>
    </header>
  );
};