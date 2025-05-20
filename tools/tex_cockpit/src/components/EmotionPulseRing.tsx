'use client'

import React, { useEffect, useState } from 'react'
import { motion } from 'framer-motion'

const emotionColors: Record<string, string> = {
  joy: 'from-green-400 to-green-600',
  anger: 'from-red-500 to-red-700',
  fear: 'from-purple-400 to-purple-600',
  resolve: 'from-blue-400 to-blue-600',
  curiosity: 'from-yellow-400 to-yellow-600',
  hope: 'from-emerald-400 to-emerald-600',
  greed: 'from-orange-400 to-orange-600',
  default: 'from-slate-400 to-slate-600',
}

export default function EmotionPulseRing() {
  const [emotion, setEmotion] = useState('resolve')

  useEffect(() => {
    const interval = setInterval(() => {
      const emotions = Object.keys(emotionColors)
      const next = emotions[Math.floor(Math.random() * emotions.length)]
      setEmotion(next)
    }, 4000)

    return () => clearInterval(interval)
  }, [])

  return (
    <div className="relative flex items-center justify-center p-6">
      <motion.div
        key={emotion}
        initial={{ scale: 0.9, opacity: 0.5 }}
        animate={{ scale: 1.15, opacity: 1 }}
        transition={{
          repeat: Infinity,
          repeatType: 'reverse',
          duration: 1.8,
          ease: 'easeInOut',
        }}
        className={`rounded-full w-40 h-40 bg-gradient-to-br ${emotionColors[emotion]} blur-xl opacity-80`}
      />
      <div className="absolute text-center">
        <p className="text-xs text-zinc-500">Current Emotion</p>
        <h2 className="text-2xl font-bold text-white capitalize font-geistMono">
          {emotion}
        </h2>
      </div>
    </div>
  )
}