'use client';

import useSWR from 'swr';
import { motion } from 'framer-motion';
import clsx from 'clsx';

// Fetch JSON from live_outputs
const fetcher = (url: string) => fetch(url).then(res => res.json());

// Define valid emotion types
type EmotionType =
  | 'fear'
  | 'greed'
  | 'hope'
  | 'resolve'
  | 'doubt'
  | 'curiosity'
  | 'neutral';

const emotionColorMap: Record<EmotionType, string> = {
  fear: 'border-cockpit-regret',
  greed: 'border-cockpit-accent',
  hope: 'border-cockpit-soft',
  resolve: 'border-cockpit-title',
  doubt: 'border-cockpit-border',
  curiosity: 'border-cockpit-urgency',
  neutral: 'border-cockpit-logic',
};

export default function CognitiveHUD() {
  const { data } = useSWR('/live_outputs/texpulse.json', fetcher, { refreshInterval: 3000 });

  const emotion = (data?.emotion || 'neutral') as EmotionType;
  const urgency = data?.urgency?.toFixed(2) || '0.00';
  const coherence = data?.coherence?.toFixed(2) || '0.00';
  const mutation = data?.mutation_triggered || false;
  const phase = data?.phase || 'Initializing';

  const borderClass = emotionColorMap[emotion] || 'border-white';

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="fixed top-4 left-4 z-50 p-4 backdrop-blur-md bg-cockpit-panel border border-cockpit-border rounded-2xl text-xs text-white shadow-xl flex gap-4"
    >
      <div className={clsx("w-14 h-14 rounded-full border-4 animate-pulse", borderClass)} />
      <div className="flex flex-col justify-center">
        <div className="uppercase text-cockpit-soft text-[10px] tracking-wide mb-1">TEXPULSE STATUS</div>
        <div>🧠 Emotion: <span className="font-bold">{emotion}</span></div>
        <div>🔥 Urgency: <span className="text-cockpit-urgency font-semibold">{urgency}</span></div>
        <div>📐 Coherence: <span className="text-cockpit-logic font-semibold">{coherence}</span></div>
        <div>🌐 Phase: <span className="text-cockpit-title">{phase}</span></div>
        {mutation && <div className="text-cockpit-accent font-bold mt-1">⚠️ Mutation Triggered</div>}
      </div>
    </motion.div>
  );
}