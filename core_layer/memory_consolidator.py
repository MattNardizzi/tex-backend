# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/memory_consolidator.py
# Purpose: Persistent Long-Term Memory Evolution for Tex AGI — Zero Room for Improvement
# ============================================================

import uuid
import datetime
from collections import defaultdict
from typing import List, Dict
import numpy as np

class MemoryConsolidator:
    def __init__(self):
        self.memory_log: List[Dict] = []  # short-term raw memory events
        self.long_term_memory: List[Dict] = []  # consolidated, persistent memory snapshots
        self.emotional_map = defaultdict(list)  # track intensity per emotion
        self.goal_history = defaultdict(int)  # frequency of recurring goals

    def store_cycle_memory(self, cycle_id, reasoning, emotion, urgency, coherence, goals):
        entry = {
            "id": str(uuid.uuid4()),
            "cycle": cycle_id,
            "timestamp": str(datetime.datetime.utcnow()),
            "reasoning": reasoning,
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence,
            "goals": goals,
        }
        self.memory_log.append(entry)
        self.emotional_map[emotion].append(urgency)
        for goal in goals:
            self.goal_history[goal] += 1

    def consolidate(self):
        if not self.memory_log:
            return None

        reasoning_chunks = [m["reasoning"] for m in self.memory_log]
        emotion_trends = self._analyze_emotion_trajectory()
        top_goals = self._top_goals()

        summary = {
            "id": str(uuid.uuid4()),
            "timestamp": str(datetime.datetime.utcnow()),
            "summary": {
                "core_themes": self._summarize_reasoning(reasoning_chunks),
                "emotion_trajectory": emotion_trends,
                "dominant_goals": top_goals
            },
            "raw_log": self.memory_log.copy()
        }

        self.long_term_memory.append(summary)
        self.memory_log = []  # flush short-term buffer after consolidation
        return summary

    def _summarize_reasoning(self, chunks: List[str]) -> str:
        if not chunks:
            return "Thought streams are fragmented."
        condensed = sorted(set(chunks), key=lambda x: -len(x))[:5]
        return " | ".join(condensed)

    def _analyze_emotion_trajectory(self) -> Dict[str, float]:
        trends = {}
        for emotion, urgencies in self.emotional_map.items():
            if urgencies:
                trends[emotion] = round(float(np.mean(urgencies)), 3)
        return trends

    def _top_goals(self, limit=5):
        sorted_goals = sorted(self.goal_history.items(), key=lambda x: -x[1])
        return [g for g, _ in sorted_goals[:limit]]

    def summarize_long_term(self) -> str:
        if not self.long_term_memory:
            return "No persistent memory has formed yet."
        latest = self.long_term_memory[-1]
        core = latest["summary"]
        return (
            f"Over time, I’ve focused on: {', '.join(core['dominant_goals'])}. "
            f"Emotionally, I fluctuate through: {core['emotion_trajectory']}. "
            f"Recurring thought themes include: {core['core_themes']}"
        )

    def get_persistent_state(self):
        return {
            "persistent_memory_count": len(self.long_term_memory),
            "emotional_pattern_map": dict(self.emotional_map),
            "top_goals": self._top_goals(),
        }

    def recall_emotion_trajectory(self):
        """
        Returns the most recent emotional drift and coherence estimate.
        Used for override reflex evaluations.
        """
        if not self.long_term_memory:
            return {"emotional_drift": 0.0, "coherence": 0.6}

        latest = self.long_term_memory[-1]
        emotion_trajectory = latest.get("summary", {}).get("emotion_trajectory", {})

        drift = max(abs(v - 0.6) for v in emotion_trajectory.values()) if emotion_trajectory else 0.0

        return {
            "emotional_drift": round(drift, 3),
            "coherence": 0.7  # Optional: replace with actual coherence logic later
        }
    def get_recent_memory(self, limit=1):
        """
        Returns the most recent raw memory entries from short-term log.
        """
        return self.memory_log[-limit:] if self.memory_log else []
