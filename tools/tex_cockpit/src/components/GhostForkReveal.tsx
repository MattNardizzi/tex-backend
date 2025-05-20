'use client';

import useSWR from 'swr';
import { motion } from 'framer-motion';
import clsx from 'clsx';

const fetcher = (url: string) => fetch(url).then(res => res.json());

export default function GhostForkReveal() {
  const { data, error } = useSWR('/live_outputs/fork_comparison.json', fetcher, { refreshInterval: 5000 });

  if (error) return <div className="text-red-500">Failed to load fork data.</div>;
  if (!data) return <div className="text-cockpit-soft">Awaiting strategy fork comparison...</div>;

  const { tex_decision, ghost_variant, delta_confidence, can_override } = data;

  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4 }}
      className="w-full max-w-6xl bg-cockpit-panel/90 border border-cockpit-border rounded-2xl p-6 shadow-xl backdrop-blur-md space-y-4"
    >
      <div className="flex justify-between items-center">
        <h3 className="text-lg font-mono text-cockpit-accent">👁 Reveal Cognitive Fork</h3>
        <span className="text-xs text-cockpit-soft">
          Divergence Score: <span className="text-yellow-400 font-bold">{delta_confidence.toFixed(2)}</span>
        </span>
      </div>

      <div className="grid grid-cols-2 gap-6 text-sm font-mono">
        {/* Tex Decision */}
        <div className="bg-cockpit-bg/60 border border-cockpit-border p-4 rounded-xl space-y-2">
          <h4 className="text-cockpit-logic font-semibold">🔵 Tex Strategy</h4>
          <p><strong>Emotion:</strong> {tex_decision.emotion}</p>
          <p><strong>Forecast:</strong> {tex_decision.forecast}</p>
          <p><strong>Confidence:</strong> {tex_decision.confidence.toFixed(2)}</p>
          <p><strong>Reason:</strong> {tex_decision.reasoning}</p>
        </div>

        {/* Ghost Variant */}
        <div className="bg-cockpit-bg/60 border border-cockpit-border p-4 rounded-xl space-y-2">
          <h4 className="text-cockpit-emotion font-semibold">👻 Variant Fork</h4>
          <p><strong>Emotion:</strong> {ghost_variant.emotion}</p>
          <p><strong>Forecast:</strong> {ghost_variant.forecast}</p>
          <p><strong>Confidence:</strong> {ghost_variant.confidence.toFixed(2)}</p>
          <p><strong>Reason:</strong> {ghost_variant.reasoning}</p>
        </div>
      </div>

      {can_override && (
        <motion.button
          whileTap={{ scale: 0.97 }}
          className="mt-4 mx-auto block bg-cockpit-accent text-white px-6 py-2 rounded-full text-sm font-bold shadow-lg hover:opacity-90 transition"
        >
          ⚡ Integrate Variant Logic
        </motion.button>
      )}
    </motion.div>
  );
}