import React from 'react';
import { Calendar, Shield, RotateCcw, Save, Sparkles } from 'lucide-react';
import { ComplaintFormData } from '../types';

interface ComplaintFormProps {
  formData: ComplaintFormData;
  onChange: (field: keyof ComplaintFormData, value: string) => void;
  onReset: () => void;
  onSave: () => void;
  onAssessRisk: () => void;
  isExtracting: boolean;
  isAssessingRisk: boolean;
  isBlocked: boolean;
}

export const ComplaintForm: React.FC<ComplaintFormProps> = ({
  formData,
  onChange,
  onReset,
  onSave,
  onAssessRisk,
  isExtracting,
  isAssessingRisk,
  isBlocked,
}) => {
  return (
    <div className="bg-white rounded-xl border border-slate-200/80 shadow-2xs p-6 md:p-8 space-y-8 relative">
      {/* Top Banner overlay if extracting */}
      {isExtracting && (
        <div className="absolute inset-0 bg-white/75 backdrop-blur-[1px] z-10 rounded-xl flex flex-col items-center justify-center p-6 text-center animate-fade-in">
          <div className="p-3 bg-blue-50 text-blue-600 rounded-full mb-3 animate-bounce">
            <Sparkles className="w-8 h-8" />
          </div>
          <h3 className="text-lg font-semibold text-slate-800">AI Copilot Extracting Metadata...</h3>
          <p className="text-sm text-slate-500 max-w-md mt-1">
            Analyzing pharmaceutical batch, customer details, quality issue severity, and regulatory risk parameters.
          </p>
        </div>
      )}

      {/* Block overlay: prevent manual entry before AI extraction */}
      {isBlocked && (
        <div className="absolute inset-0 bg-slate-50/80 backdrop-blur-[2px] z-10 rounded-xl flex flex-col items-center justify-center p-6 text-center animate-fade-in">
          <div className="p-3 bg-amber-50 text-amber-600 rounded-full mb-3">
            <Sparkles className="w-8 h-8" />
          </div>
          <h3 className="text-lg font-semibold text-slate-800">Awaiting AI Extraction</h3>
          <p className="text-sm text-slate-500 max-w-md mt-1">
            Upload a document to extract complaint details. All fields are locked until AI analysis is complete.
          </p>
        </div>
      )}

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
              placeholder="Awaiting AI extraction..."
              className="w-full text-xs md:text-sm px-3.5 py-2.5 bg-slate-50/50 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all"
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-700 mb-1.5">Customer Name</label>
            <input
              type="text"
              value={formData.customerName}
              onChange={(e) => onChange('customerName', e.target.value)}
              placeholder="Awaiting AI extraction..."
              className="w-full text-xs md:text-sm px-3.5 py-2.5 bg-slate-50/50 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all"
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
              placeholder="Awaiting AI extraction..."
              className="w-full text-xs md:text-sm px-3.5 py-2.5 bg-slate-50/50 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all"
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-700 mb-1.5">Product Strength/Grade</label>
            <input
              type="text"
              value={formData.productStrength}
              onChange={(e) => onChange('productStrength', e.target.value)}
              placeholder="Awaiting AI extraction..."
              className="w-full text-xs md:text-sm px-3.5 py-2.5 bg-slate-50/50 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all"
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-700 mb-1.5">Batch/Lot Number</label>
            <input
              type="text"
              value={formData.batchNumber}
              onChange={(e) => onChange('batchNumber', e.target.value)}
              placeholder="Awaiting AI extraction..."
              className="w-full text-xs md:text-sm px-3.5 py-2.5 bg-slate-50/50 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all tabular-nums"
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-700 mb-1.5">Manufacturing Date</label>
            <div className="relative">
              <input
                type="text"
                value={formData.manufacturingDate}
                onChange={(e) => onChange('manufacturingDate', e.target.value)}
                placeholder="Awaiting AI extraction..."
                className="w-full text-xs md:text-sm px-3.5 py-2.5 pr-10 bg-slate-50/50 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all tabular-nums"
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
                placeholder="Awaiting AI extraction..."
                className="w-full text-xs md:text-sm px-3.5 py-2.5 pr-10 bg-slate-50/50 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all tabular-nums"
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
                placeholder="Awaiting AI extraction..."
                className="w-full text-xs md:text-sm px-3.5 py-2.5 pr-12 bg-slate-50/50 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all tabular-nums"
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
              placeholder="Awaiting AI extraction..."
              className="w-full text-xs md:text-sm px-3.5 py-2.5 bg-slate-50/50 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all"
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-700 mb-1.5">Complaint Date</label>
            <div className="relative">
              <input
                type="text"
                value={formData.complaintDate}
                onChange={(e) => onChange('complaintDate', e.target.value)}
                placeholder="Awaiting AI extraction..."
                className="w-full text-xs md:text-sm px-3.5 py-2.5 pr-10 bg-slate-50/50 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all tabular-nums"
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
            placeholder="Awaiting AI extraction..."
            className="w-full text-xs md:text-sm p-3.5 bg-slate-50/50 border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all resize-y"
          />
        </div>
      </section>

      {/* 4. INITIAL ASSESSMENT & PRIORITY (Matching blue card in prompt) */}
      <section className="space-y-4">
        <h3 className="text-xs font-bold text-slate-500 uppercase tracking-wider border-b border-slate-100 pb-2">
          4. INITIAL ASSESSMENT & PRIORITY
        </h3>

        <div className="bg-blue-50/40 border border-blue-100 rounded-xl p-5 space-y-4 relative">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2 text-blue-700 font-semibold text-xs md:text-sm">
              <Shield className="w-4 h-4 text-blue-600" />
              <span>AI copilot risk assessment</span>
            </div>
            <button
              type="button"
              onClick={onAssessRisk}
              disabled={isAssessingRisk}
              className="text-xs text-blue-600 hover:text-blue-800 font-medium flex items-center gap-1 hover:underline disabled:opacity-50"
            >
              <Sparkles className="w-3.5 h-3.5" />
              {isAssessingRisk ? 'Re-evaluating...' : 'Re-assess Risk'}
            </button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label className="block text-xs font-medium text-slate-700 mb-1">Severity (Suggested)</label>
              <select
                value={formData.suggestedSeverity}
                onChange={(e) => onChange('suggestedSeverity', e.target.value as any)}
                className="w-full text-xs md:text-sm px-3.5 py-2.5 bg-white border border-slate-200 rounded-lg text-slate-900 font-medium focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500"
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
                className="w-full text-xs md:text-sm px-3.5 py-2.5 bg-white border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500"
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
              className="w-full text-xs md:text-sm p-3.5 bg-white border border-slate-200 rounded-lg text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 resize-y"
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