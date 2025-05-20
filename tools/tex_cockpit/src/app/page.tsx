'use client';

import React from 'react';
import TexNarrationOverlay from '@/components/TexNarrationOverlay';
import EmotionPulseRing from '@/components/EmotionPulseRing';
import CognitiveHUD from '@/components/CognitiveHUD';
import InternalDebateLog from '@/components/InternalDebateLog';
import AlphaEngineHUD from '@/components/AlphaEngineHUD';

export default function HomePage() {
  return (
    <main className="relative min-h-screen bg-cockpit-bg text-white font-primary px-6 py-12 flex flex-col items-center gap-12 overflow-hidden">
      {/* === Cognitive Status HUD (top-left) === */}
      <CognitiveHUD />

      {/* === Zone 0: Emotion HUD (centered) === */}
      <section className="flex flex-col items-center gap-3">
        <EmotionPulseRing />
        <h2 className="text-cockpit-title text-xl font-mono">
          Tex Cognition System
        </h2>
      </section>

      {/* === Zone 1: Tex Narration Feed === */}
      <section className="w-full max-w-4xl">
        <div className="rounded-2xl border border-cockpit-border p-6 shadow-2xl bg-cockpit-panel/90 backdrop-blur-sm">
          <h3 className="text-lg font-semibold text-cockpit-soft mb-4 font-mono">
            🧠 Real-Time Thought Feed
          </h3>
          <TexNarrationOverlay />
        </div>
      </section>

      {/* === Zone 2: Internal Debate === */}
      <section className="w-full max-w-4xl">
        <InternalDebateLog />
      </section>

      {/* === Zone 3: Alpha Engine Status === */}
      <section className="w-full max-w-4xl">
        <AlphaEngineHUD />
      </section>
    </main>
  );
}