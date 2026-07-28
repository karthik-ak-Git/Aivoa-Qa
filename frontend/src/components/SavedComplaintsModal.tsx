import React from 'react';
import { ComplaintFormData } from '../types';
import { Search, Download, Trash2, ExternalLink, ArrowLeft } from 'lucide-react';
import { useAppDispatch, useAppSelector } from '../store/hooks';
import { setSearchTerm, setStatusFilter, setSeverityFilter } from '../store/uiSlice';

interface SavedComplaintsModalProps {
  complaints: ComplaintFormData[];
  onSelectComplaint: (complaint: ComplaintFormData) => void;
  onDeleteComplaint: (id: string) => void;
  onBackToForm: () => void;
}

export const SavedComplaintsModal: React.FC<SavedComplaintsModalProps> = ({
  complaints,
  onSelectComplaint,
  onDeleteComplaint,
  onBackToForm,
}) => {
  const dispatch = useAppDispatch();
  const searchTerm = useAppSelector((state) => state.ui.searchTerm);
  const statusFilter = useAppSelector((state) => state.ui.statusFilter);
  const severityFilter = useAppSelector((state) => state.ui.severityFilter);

  const filtered = complaints.filter((c) => {
    const matchesSearch =
      (c.customerName || '').toLowerCase().includes(searchTerm.toLowerCase()) ||
      (c.productName || '').toLowerCase().includes(searchTerm.toLowerCase()) ||
      (c.batchNumber || '').toLowerCase().includes(searchTerm.toLowerCase()) ||
      (c.complaintType || '').toLowerCase().includes(searchTerm.toLowerCase());

    const matchesStatus = statusFilter === 'ALL' || c.status === statusFilter;
    const matchesSeverity = severityFilter === 'ALL' || c.suggestedSeverity === severityFilter;

    return matchesSearch && matchesStatus && matchesSeverity;
  });

  const exportJSON = () => {
    const blob = new Blob([JSON.stringify(complaints, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `pharma_complaints_register_${new Date().toISOString().split('T')[0]}.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const getSeverityBadge = (severity: string) => {
    switch (severity) {
      case 'Critical':
        return 'bg-red-50 text-red-700 border-red-200';
      case 'Major':
        return 'bg-amber-50 text-amber-700 border-amber-200';
      case 'Minor':
        return 'bg-blue-50 text-blue-700 border-blue-200';
      default:
        return 'bg-slate-50 text-slate-600 border-slate-200';
    }
  };

  return (
    <div className="bg-white rounded-xl border border-slate-200/80 shadow-2xs p-6 md:p-8 space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-100 pb-5">
        <div className="flex items-center gap-3">
          <button
            onClick={onBackToForm}
            className="p-2 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-lg text-xs font-medium transition-all"
          >
            <ArrowLeft className="w-4 h-4" />
          </button>
          <div>
            <h2 className="text-xl font-bold text-slate-900 tracking-tight">Quality Complaint Register</h2>
            <p className="text-xs text-slate-500 mt-0.5">
              Historical QA Triage & Investigation Log ({filtered.length} records)
            </p>
          </div>
        </div>

        <button
          onClick={exportJSON}
          className="px-3.5 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-lg text-xs font-medium flex items-center gap-1.5 transition-all self-start sm:self-auto"
        >
          <Download className="w-3.5 h-3.5" />
          Export JSON
        </button>
      </div>

      {/* Filters Bar */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
        <div className="relative">
          <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            value={searchTerm}
            onChange={(e) => dispatch(setSearchTerm(e.target.value))}
            placeholder="Search customer, batch, product..."
            className="w-full text-xs pl-9 pr-3 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500/20"
          />
        </div>

        <div className="flex items-center gap-2">
          <span className="text-xs font-medium text-slate-500 shrink-0">Status:</span>
          <select
            value={statusFilter}
            onChange={(e) => dispatch(setStatusFilter(e.target.value))}
            className="w-full text-xs px-2.5 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500/20"
          >
            <option value="ALL">All Statuses</option>
            <option value="Pending Triage">Pending Triage</option>
            <option value="Under QA Investigation">Under QA Investigation</option>
            <option value="CAPA Initiated">CAPA Initiated</option>
            <option value="Closed">Closed</option>
          </select>
        </div>

        <div className="flex items-center gap-2">
          <span className="text-xs font-medium text-slate-500 shrink-0">Severity:</span>
          <select
            value={severityFilter}
            onChange={(e) => dispatch(setSeverityFilter(e.target.value))}
            className="w-full text-xs px-2.5 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500/20"
          >
            <option value="ALL">All Severities</option>
            <option value="Critical">Critical</option>
            <option value="Major">Major</option>
            <option value="Minor">Minor</option>
          </select>
        </div>
      </div>

      {/* Table */}
      <div className="overflow-x-auto border border-slate-200 rounded-lg">
        <table className="w-full text-left border-collapse text-xs">
          <thead>
            <tr className="bg-slate-50 border-b border-slate-200 text-slate-600 font-semibold uppercase tracking-wider">
              <th className="p-3">Ref / Customer</th>
              <th className="p-3">Product / Batch</th>
              <th className="p-3">Type</th>
              <th className="p-3">Severity</th>
              <th className="p-3">Status</th>
              <th className="p-3 text-right">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100">
            {filtered.length === 0 ? (
              <tr>
                <td colSpan={6} className="p-8 text-center text-slate-400 italic">
                  No complaints found matching criteria. Log a new complaint or reset filters.
                </td>
              </tr>
            ) : (
              filtered.map((c) => (
                <tr key={c.id} className="hover:bg-slate-50/80 transition-colors">
                  <td className="p-3 font-medium text-slate-900">
                    <div className="font-semibold text-blue-700">{c.id || 'CMP-NEW'}</div>
                    <div className="text-slate-500">{c.customerName || 'N/A'}</div>
                  </td>
                  <td className="p-3">
                    <div className="font-medium text-slate-800">{c.productName || 'N/A'}</div>
                    <div className="text-slate-500 tabular-nums font-mono text-[11px]">
                      Batch: {c.batchNumber || 'N/A'}
                    </div>
                  </td>
                  <td className="p-3 text-slate-700">{c.complaintType || 'N/A'}</td>
                  <td className="p-3">
                    <span
                      className={`px-2 py-0.5 rounded-full border text-[11px] font-semibold ${getSeverityBadge(
                        c.suggestedSeverity
                      )}`}
                    >
                      {c.suggestedSeverity || 'Unassessed'}
                    </span>
                  </td>
                  <td className="p-3">
                    <span className="px-2 py-0.5 rounded-full bg-slate-100 text-slate-700 text-[11px] font-medium border border-slate-200">
                      {c.status}
                    </span>
                  </td>
                  <td className="p-3 text-right">
                    <div className="flex items-center justify-end gap-2">
                      <button
                        onClick={() => {
                          onSelectComplaint(c);
                          onBackToForm();
                        }}
                        className="p-1.5 hover:bg-blue-50 text-blue-600 rounded transition-colors"
                        title="Load into Form"
                      >
                        <ExternalLink className="w-4 h-4" />
                      </button>
                      <button
                        onClick={() => c.id && onDeleteComplaint(c.id)}
                        className="p-1.5 hover:bg-red-50 text-red-500 rounded transition-colors"
                        title="Delete record"
                      >
                        <Trash2 className="w-4 h-4" />
                      </button>
                    </div>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};