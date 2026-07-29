import React, { useEffect } from 'react';
import { Calendar, Shield, RotateCcw, Save } from 'lucide-react';
import { ComplaintFormData } from '../types';

interface ComplaintFormProps {
  formData: ComplaintFormData;
  onChange: (field: keyof ComplaintFormData, value: string) => void;
  onReset: () => void;
  onSave: () => void;
  highlightedFields: string[];
  onClearHighlights: () => void;
}

const hl = (field: string, highlightedFields: string[]) =>
  highlightedFields.includes(field) ? 'animate-highlight ring-2 ring-blue-400/40 border-blue-400' : '';

export const ComplaintForm: React.FC<ComplaintFormProps> = ({
  formData,
  onChange,
  onReset,
  onSave,
  highlightedFields,
  onClearHighlights,
}) => {
  useEffect(() => {
    if (highlightedFields.length > 0) {
      const timer = setTimeout(onClearHighlights, 3000);
      return () => clearTimeout(timer);
    }
  }, [highlightedFields, onClearHighlights]);
  return (
    <div className="bg-white rounded-xl border border-slate-200/80 shadow-2xs p-6 md:p-8 space-y-8 relative">

      <div className="bg-slate-50 border border-slate-200 rounded-lg px-4 py-2.5 text-xs text-slate-500 flex items-center gap-2">
        <Sparkles className="w-3.5 h-3.5 text-blue-500 shrink-0" />
        <span>Form is managed by <strong className="text-slate-700">AI Copilot</strong> — edit fields via the chat panel on the right.</span>
      </div>

      {/* Title & Status Bar matching Image */}
      <div className="flex items-start justify-between border-b border-slate-100 pb-6">
        <div>
          <h2 className="text-2xl font-bold text-slate-900 tracking-tight">Log Customer Complaint</h2>
          <p className="text-sm font-medium text-slate-500 mt-1">API & FDF Quality Assurance Module</p>
        </div>
        <div className="flex items-center gap-3">
          <span className="px-3 py-1 bg-amber-50 text-amber-700 border border-amber-200/80 text-xs font-semibold rounded-full tracking-wide">
            {formData.status || 'Pending Triage'}
          </span>
        </div>
      </div>

      {/* 1. ORIGIN & CUSTOMER DETAILS */}
      <section className="space-y-4">
        <h3 className="text-xs font-bold text-slate-500 uppercase tracking-wider border-b border-slate-100 pb-2">
          1. ORIGIN & CUSTOMER DETAILS
        </h3>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          <div>
            <label className="block text-xs font-medium text-slate-700 mb-1.5">Complaint Source</label>
            <input
              type="text"
              value={formData.complaintSource}
              onChange={(e) => onChange('complaintSource', e.target.value)}
              placeholder="e.g. Email Intake, Phone Call, Portal"
              disabled
              readOnly
              className={`w-full text-xs md:text-sm px-3.5 py-2.5 bg-slate-100 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 cursor-not-allowed select-none ${hl('complaintSource', highlightedFields)}`}
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-700 mb-1.5">Customer Name</label>
            <input
              type="text"
              value={formData.customerName}
              onChange={(e) => onChange('customerName', e.target.value)}
              placeholder="e.g. Apex Pharmaceuticals Distribution GmbH"
              disabled
              readOnly
              className={`w-full text-xs md:text-sm px-3.5 py-2.5 bg-slate-100 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 cursor-not-allowed select-none ${hl('customerName', highlightedFields)}`}
            />
          </div>
        </div>
      </section>

      {/* 2. PRODUCT & BATCH IDENTIFICATION */}
      <section className="space-y-4">
        <h3 className="text-xs font-bold text-slate-500 uppercase tracking-wider border-b border-slate-100 pb-2">
          2. PRODUCT & BATCH IDENTIFICATION
        </h3>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          <div>
            <label className="block text-xs font-medium text-slate-700 mb-1.5">Product Name</label>
            <input
              type="text"
              value={formData.productName}
              onChange={(e) => onChange('productName', e.target.value)}
              placeholder="e.g. Amoxicillin Trihydrate 500mg FDF Capsules"
              disabled
              readOnly
              className={`w-full text-xs md:text-sm px-3.5 py-2.5 bg-slate-100 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 cursor-not-allowed select-none ${hl('productName', highlightedFields)}`}
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-700 mb-1.5">Product Strength/Grade</label>
            <input
              type="text"
              value={formData.productStrength}
              onChange={(e) => onChange('productStrength', e.target.value)}
              placeholder="e.g. 500mg Alu-Alu Blister"
              disabled
              readOnly
              className={`w-full text-xs md:text-sm px-3.5 py-2.5 bg-slate-100 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 cursor-not-allowed select-none ${hl('productStrength', highlightedFields)}`}
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-700 mb-1.5">Batch/Lot Number</label>
            <input
              type="text"
              value={formData.batchNumber}
              onChange={(e) => onChange('batchNumber', e.target.value)}
              placeholder="e.g. AMX-2026-094"
              disabled
              readOnly
              className={`w-full text-xs md:text-sm px-3.5 py-2.5 bg-slate-100 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 cursor-not-allowed select-none tabular-nums ${hl('batchNumber', highlightedFields)}`}
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-700 mb-1.5">Manufacturing Date</label>
            <div className="relative">
              <input
                type="text"
              value={formData.manufacturingDate}
              onChange={(e) => onChange('manufacturingDate', e.target.value)}
              placeholder="e.g. 2026-03-10"
              disabled
              readOnly
              className={`w-full text-xs md:text-sm px-3.5 py-2.5 pr-10 bg-slate-100 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 cursor-not-allowed select-none tabular-nums ${hl('manufacturingDate', highlightedFields)}`}
              />
              <Calendar className="w-4 h-4 text-slate-400 absolute right-3.5 top-1/2 -translate-y-1/2 pointer-events-none" />
            </div>
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-700 mb-1.5">Expiry Date</label>
            <div className="relative">
              <input
                type="text"
              value={formData.expiryDate}
              onChange={(e) => onChange('expiryDate', e.target.value)}
              placeholder="e.g. 2028-03-09"
              disabled
              readOnly
              className={`w-full text-xs md:text-sm px-3.5 py-2.5 pr-10 bg-slate-100 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 cursor-not-allowed select-none tabular-nums ${hl('expiryDate', highlightedFields)}`}
              />
              <Calendar className="w-4 h-4 text-slate-400 absolute right-3.5 top-1/2 -translate-y-1/2 pointer-events-none" />
            </div>
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-700 mb-1.5">Quantity Affected</label>
            <div className="relative flex items-center">
              <input
                type="text"
              value={formData.quantityAffected}
              onChange={(e) => onChange('quantityAffected', e.target.value)}
              placeholder="e.g. 240"
              disabled
              readOnly
              className={`w-full text-xs md:text-sm px-3.5 py-2.5 pr-12 bg-slate-100 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 cursor-not-allowed select-none tabular-nums ${hl('quantityAffected', highlightedFields)}`}
              />
              <span className="absolute right-3.5 text-xs font-medium text-slate-500">
                {formData.quantityUnit || 'kg'}
              </span>
            </div>
          </div>
        </div>
      </section>

      {/* 3. COMPLAINT DETAILS */}
      <section className="space-y-4">
        <h3 className="text-xs font-bold text-slate-500 uppercase tracking-wider border-b border-slate-100 pb-2">
          3. COMPLAINT DETAILS
        </h3>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          <div>
            <label className="block text-xs font-medium text-slate-700 mb-1.5">Complaint Type</label>
            <input
              type="text"
              value={formData.complaintType}
              onChange={(e) => onChange('complaintType', e.target.value)}
              placeholder="e.g. Discoloration & Blister Seal Defect"
              disabled
              readOnly
              className={`w-full text-xs md:text-sm px-3.5 py-2.5 bg-slate-100 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 cursor-not-allowed select-none ${hl('complaintType', highlightedFields)}`}
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-700 mb-1.5">Complaint Date</label>
            <div className="relative">
              <input
                type="text"
              value={formData.complaintDate}
              onChange={(e) => onChange('complaintDate', e.target.value)}
              placeholder="e.g. 2026-07-24"
              disabled
              readOnly
              className={`w-full text-xs md:text-sm px-3.5 py-2.5 pr-10 bg-slate-100 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 cursor-not-allowed select-none tabular-nums ${hl('complaintDate', highlightedFields)}`}
              />
              <Calendar className="w-4 h-4 text-slate-400 absolute right-3.5 top-1/2 -translate-y-1/2 pointer-events-none" />
            </div>
          </div>
        </div>

        <div>
          <label className="block text-xs font-medium text-slate-700 mb-1.5">Detailed Complaint Description</label>
          <textarea
            rows={3}
            value={formData.detailedDescription}
            onChange={(e) => onChange('detailedDescription', e.target.value)}
            placeholder="Describe the complaint in detail..."
            disabled
            readOnly
            className={`w-full text-xs md:text-sm p-3.5 bg-slate-100 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 cursor-not-allowed select-none resize-y ${hl('detailedDescription', highlightedFields)}`}
          />
        </div>
      </section>

      {/* 4. INITIAL ASSESSMENT & PRIORITY (Matching blue card in prompt) */}
      <section className="space-y-4">
        <h3 className="text-xs font-bold text-slate-500 uppercase tracking-wider border-b border-slate-100 pb-2">
          4. INITIAL ASSESSMENT & PRIORITY
        </h3>

        <div className="bg-blue-50/40 border border-blue-100 rounded-xl p-5 space-y-4 relative">
          <div className="flex items-center gap-2 text-blue-700 font-semibold text-xs md:text-sm">
            <Shield className="w-4 h-4 text-blue-600" />
            <span>AI copilot risk assessment</span>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label className="block text-xs font-medium text-slate-700 mb-1">Severity (Suggested)</label>
              <select
                value={formData.suggestedSeverity}
                disabled
                className={`w-full text-xs md:text-sm px-3.5 py-2.5 bg-slate-100 border border-slate-200 rounded-lg text-slate-900 font-medium cursor-not-allowed select-none ${hl('suggestedSeverity', highlightedFields)}`}
              >
                <option value="">Select Severity...</option>
                <option value="Critical">Critical</option>
                <option value="Major">Major</option>
                <option value="Minor">Minor</option>
              </select>
            </div>

            <div>
              <label className="block text-xs font-medium text-slate-700 mb-1">Suggested Next Action</label>
              <input
                type="text"
                value={formData.suggestedNextAction}
                onChange={(e) => onChange('suggestedNextAction', e.target.value)}
                placeholder="e.g. Route to QA Investigation & Issue Replacement"
                disabled
                readOnly
                className={`w-full text-xs md:text-sm px-3.5 py-2.5 bg-slate-100 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 cursor-not-allowed select-none ${hl('suggestedNextAction', highlightedFields)}`}
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-700 mb-1">Initial Risk Assessment</label>
            <textarea
              rows={2}
              value={formData.riskAssessment}
              onChange={(e) => onChange('riskAssessment', e.target.value)}
              placeholder="Potential moisture ingress or primary packaging seal failure leading to capsule discoloration..."
              disabled
              readOnly
              className={`w-full text-xs md:text-sm p-3.5 bg-slate-100 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 cursor-not-allowed select-none resize-y ${hl('riskAssessment', highlightedFields)}`}
            />
          </div>
        </div>
      </section>

      {/* Bottom Action Bar matching exact screenshot styling */}
      <div className="flex items-center justify-between pt-4 border-t border-slate-100">
        <button
          type="button"
          onClick={onReset}
          className="px-4 py-2 bg-white border border-slate-200 hover:bg-slate-50 text-slate-700 rounded-lg text-xs font-medium flex items-center gap-2 transition-all"
        >
          <RotateCcw className="w-3.5 h-3.5 text-slate-500" />
          <span>Reset Form</span>
        </button>

        <button
          type="button"
          onClick={onSave}
          className="px-6 py-2.5 bg-blue-600 hover:bg-blue-700 active:bg-blue-800 text-white rounded-lg text-xs font-semibold flex items-center gap-2 shadow-2xs transition-all"
        >
          <Save className="w-4 h-4" />
          <span>Save Complaint</span>
        </button>
      </div>
    </div>
  );
};
