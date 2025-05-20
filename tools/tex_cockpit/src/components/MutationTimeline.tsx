'use client';

import useSWR from 'swr';
import { motion } from 'framer-motion';

const fetcher = (url: string) => fetch(url).then(res => res.text());

interface MutationEntry {
  cycle: number;
  trigger: string;
  description: string;
  outcome: string;
  revertable: boolean;
  timestamp: string;
}

export default function MutationTimeline() {
  const { data, error } = useSWR('/live_outputs/mutation_log.jsonl', fetcher, { refreshInterval: 5000 });

  if (error) return <div className="text-red-500">Failed to load mutation timeline.</div>;
  if (!data) return <div className="text-cockpit-soft">Loading mutation history...</div>;

  const lines = data.trim().split('\n');
  const entries: MutationEntry[] = lines.map(line => JSON.parse(line)).reverse().slice(0, 6);

  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4 }}
      className="w-full max-w-4xl rounded-2xl bg-cockpit-panel/90 border border-cockpit-border shadow-xl p-5 space-y-3 backdrop-blur"
    >
      <h3 className="text-lg font-mono text-cockpit-soft mb-2">🧬 Mutation Timeline</h3>
      {entries.map((entry, index) => (
        <div
          key={index}
          className="border-l-4 pl-4 py-2 border-cockpit-accent bg-cockpit-bg/40 rounded-md"
        >
          <div className="flex items-center justify-between">
            <span className="text-cockpit-soft text-xs">Cycle {entry.cycle}</span>
            <span className="text-cockpit-accent text-xs">{entry.timestamp}</span>
          </div>
          <div className="text-sm text-white mt-1">{entry.description}</div>
          <div className="text-xs mt-1">
            <span className="text-cockpit-title font-mono">Trigger:</span> {entry.trigger} |{' '}
            <span className="text-cockpit-urgency">Outcome:</span>{' '}
            <span className={entry.outcome === 'SUCCESS' ? 'text-green-400' : 'text-red-500'}>
              {entry.outcome}
            </span>
            {!entry.revertable && (
              <span className="ml-2 text-gray-500 opacity-60">🔒</span>
            )}
          </div>
        </div>
      ))}
    </motion.div>
  );
}