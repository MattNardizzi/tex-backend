'use client';

import React, { useState, useEffect } from 'react';

export default function VortexMessageBoard({ messages = [] }: { messages?: string[] }) {
  const [log, setLog] = useState<string[]>([]);

  useEffect(() => {
    if (messages && messages.length) {
      setLog((prev) => [...prev.slice(-20), ...messages]);
    }
  }, [messages]);

  return (
    <div className="bg-black/70 border border-cyan-500/20 rounded-xl p-4 h-72 overflow-y-auto text-xs font-mono text-cyan-300 space-y-1 shadow-inner">
      <div className="text-cyan-400 uppercase text-[10px] tracking-wide mb-1">🧠 Vortex–Matt Console</div>
      {log.length === 0 ? (
        <div className="italic text-white/30">No messages yet. Tex is quiet.</div>
      ) : (
        log.map((line, idx) => <div key={idx} className="truncate">• {line}</div>)
      )}
    </div>
  );
}