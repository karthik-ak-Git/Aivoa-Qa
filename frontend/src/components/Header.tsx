import { ShieldCheck, PlusCircle } from 'lucide-react';

interface HeaderProps {
  onNewComplaint: () => void;
}

export const Header: React.FC<HeaderProps> = ({
  onNewComplaint,
}) => {
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
          <button
            onClick={onNewComplaint}
            className="px-3 py-1.5 rounded-lg text-xs font-medium flex items-center gap-1.5 transition-all bg-blue-600 text-white shadow-2xs hover:bg-blue-700"
          >
            <PlusCircle className="w-3.5 h-3.5" />
            New Complaint
          </button>
        </div>
      </div>
    </header>
  );
};