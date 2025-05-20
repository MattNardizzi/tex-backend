'use client';

import useSWR from 'swr';
import { motion } from 'framer-motion';

const fetcher = (url: string) => fetch(url).then(res => res.text());

interface DebateEntry {
  agent_id: string;
  timestamp: string;
  score: number;
  reasoning: string;
  metrics: {
    alignment: number;
    performance: number;
    novelty: number;
    efficiency: number;
  };
}

export default function InternalDebateLog() {
  const { data, error } = useSWR('/live_outputs/agent_scores.jsonl', fetcher, { refreshInterval: 3000 });

  if (error) return <div className="text-red-500">Failed to load debate log.</div>;
  if (!data) return <div className="text-cockpit-soft">Loading internal debate...</div>;

  const lines = data.trim().split('\n');
  const entries: DebateEntry[] = lines.map(line => JSON.parse(line)).reverse().slice(0, 5);

  const getColor = (agent: string) => {
    if (agent.includes('logic')) return 'text-cockpit-logic';
    if (agent.includes('emotion')) return 'text-cockpit-emotion';
    if (agent.includes('skeptic')) return 'text-yellow-300';
    return 'text-white';
  };

  return (
    <div className="w-full max-w-4xl rounded-2xl bg-cockpit-panel/90 border border-cockpit-border shadow-xl p-5 space-y-3 backdrop-blur">
      <h3 className="text-lg font-mono text-cockpit-title mb-3">🎧 Internal Debate Log</h3>
      {entries.map((entry, index) => (
        <motion.div
          key={index}
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.3 }}
          className="bg-cockpit-bg/50 border border-cockpit-border rounded-xl p-3"
        >
          <div className="flex items-center justify-between mb-1">
            <span className={`font-bold uppercase text-xs ${getColor(entry.agent_id)}`}>
              {entry.agent_id}
            </span>
            <span className="text-cockpit-soft text-xs">🧠 {entry.score.toFixed(3)}</span>
          </div>
          <div className="text-sm text-white font-mono">{entry.reasoning}</div>
        </motion.div>
      ))}
    </div>
  );
}