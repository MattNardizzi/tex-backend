'use client';

import useSWR from 'swr';
import { motion } from 'framer-motion';

const fetcher = (url: string) => fetch(url).then(res => res.json());

export default function AlphaEngineHUD() {
  const { data, error } = useSWR('/live_outputs/strategy_status.json', fetcher, { refreshInterval: 3000 });

  if (error) return <div className="text-red-500">Failed to load strategy data.</div>;
  if (!data) return <div className="text-cockpit-soft">Loading alpha engine...</div>;

  const alpha = data?.alpha_confidence?.toFixed(2) || '0.00';
  const regret = data?.regret_score?.toFixed(2) || '0.00';
  const phase = data?.phase_state || 'Unknown';
  const logic = data?.strategy_reasoning || 'No live reasoning available.';

  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4 }}
      className="w-full max-w-4xl rounded-2xl bg-cockpit-panel/90 border border-cockpit-border shadow-xl p-5 space-y-3 backdrop-blur"
    >
      <h3 className="text-lg font-mono text-cockpit-accent mb-3">🎯 Alpha Engine Status</h3>
      
      <div className="flex flex-wrap justify-between gap-6 text-sm font-mono">
        <div>
          <span className="text-cockpit-soft">Alpha Confidence:</span>{' '}
          <span className="text-cockpit-logic font-bold">{alpha}</span>
        </div>
        <div>
          <span className="text-cockpit-soft">Regret Score:</span>{' '}
          <span className="text-cockpit-regret font-bold">{regret}</span>
        </div>
        <div>
          <span className="text-cockpit-soft">Phase State:</span>{' '}
          <span className="text-cockpit-title font-bold">{phase}</span>
        </div>
      </div>

      <div className="mt-2 text-cockpit-soft text-xs font-mono leading-snug italic">
        {logic}
      </div>
    </motion.div>
  );
}