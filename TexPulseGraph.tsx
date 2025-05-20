'use client';

// ============================================================
// © 2025 VortexBlack LLC. All rights reserved.
// File: TexPulseGraph.tsx
// Purpose: AGI Cognition Pulse Graph (alive signal for Tex)
// ============================================================

import React from 'react';
import { motion } from 'framer-motion';

export default function TexPulseGraph() {
  return (
    <div className="w-full py-2">
      <div className="flex items-center gap-2">
        <motion.div
          className="h-2 w-2 rounded-full bg-green-400"
          animate={{ opacity: [0.2, 1, 0.2] }}
          transition={{ duration: 1.2, repeat: Infinity, ease: 'easeInOut' }}
        />
        <div className="text-xs text-white/60 tracking-widest uppercase font-mono">
          Tex Cognitive Rhythm: <span className="text-green-400">Stable</span>
        </div>
      </div>
      <motion.div
        className="mt-2 h-1 w-full bg-gradient-to-r from-green-500 via-cyan-400 to-blue-500 rounded-full"
        initial={{ scaleX: 0 }}
        animate={{ scaleX: [0.4, 1, 0.6, 1, 0.4] }}
        transition={{ repeat: Infinity, duration: 3, ease: 'easeInOut' }}
        style={{ transformOrigin: 'left' }}
      />
    </div>
  );
}