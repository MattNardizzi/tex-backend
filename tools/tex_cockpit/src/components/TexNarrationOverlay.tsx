 'use client'

import React, { useEffect, useState } from 'react'
import { motion } from 'framer-motion'

type Thought = {
  text: string
  emotion?: string
  timestamp?: string
}

const emotionMap: Record<string, { color: string; tag: string }> = {
  joy: { color: 'text-green-400', tag: '🌞' },
  anger: { color: 'text-red-500', tag: '⚠️' },
  fear: { color: 'text-purple-400', tag: '🔮' },
  resolve: { color: 'text-blue-400', tag: '♻️' },
  curiosity: { color: 'text-yellow-400', tag: '❓' },
  hope: { color: 'text-emerald-400', tag: '🌱' },
  greed: { color: 'text-orange-400', tag: '🔥' },
  default: { color: 'text-slate-300', tag: '🧠' },
}

export default function TexNarrationOverlay() {
  const [thoughts, setThoughts] = useState<Thought[]>([])

  useEffect(() => {
    const interval = setInterval(() => {
      const emotions = Object.keys(emotionMap)
      const emotion = emotions[Math.floor(Math.random() * emotions.length)]
      const sample = {
        text: `Tex says: ${Math.random().toString(36).slice(2)}`,
        emotion,
        timestamp: new Date().toISOString(),
      }
      setThoughts((prev) => [sample, ...prev.slice(0, 12)])
    }, 1800)

    return () => clearInterval(interval)
  }, [])

  return (
    <div className="bg-cockpit-panel/80 p-4 rounded-xl border border-cockpit-border shadow-lg w-full space-y-2">
      {thoughts.map((thought, idx) => {
        const emotion = thought.emotion || 'default'
        const { tag, color } = emotionMap[emotion]

        return (
          <motion.div
            key={idx}
            initial={{ opacity: 0, x: -12 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.3 }}
            className={`font-mono text-sm ${color}`}
          >
            <span className="mr-2">{tag}</span>
            <span>{thought.text}</span>
            <span className="ml-2 text-xs text-zinc-500 italic">
              ({new Date(thought.timestamp || '').toLocaleTimeString()})
            </span>
          </motion.div>
        )
      })}
    </div>
  )
}