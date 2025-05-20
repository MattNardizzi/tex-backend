# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/meta_coherence_loop.py
# Tier 4 AGI Module — Meta Coherence Loop (Recursive Integrity Monitor)
# ============================================================

import difflib
import datetime
from collections import deque

class MetaCoherenceLoop:
    def __init__(self, memory_window=6):
        self.thought_history = deque(maxlen=memory_window)
        self.coherence_log = []
        self.current_score = 1.0

    def log_thought(self, thought):
        if not thought or len(thought.strip()) < 5:
            return
        timestamp = datetime.datetime.utcnow().isoformat()
        self.thought_history.append({"text": thought.strip(), "timestamp": timestamp})

    def evaluate(self):
        if len(self.thought_history) < 3:
            return 1.0

        total_similarity = 0.0
        total_conflicts = 0

        for i in range(len(self.thought_history) - 1):
            t1 = self.thought_history[i]["text"]
            t2 = self.thought_history[i + 1]["text"]
            ratio = difflib.SequenceMatcher(None, t1, t2).ratio()
            total_similarity += ratio

            if self._is_contradictory(t1, t2):
                total_conflicts += 1

        avg_similarity = total_similarity / (len(self.thought_history) - 1)
        contradiction_penalty = total_conflicts * 0.15
        coherence_score = max(0.0, min(1.0, avg_similarity - contradiction_penalty))

        self.current_score = round(coherence_score, 3)
        self.coherence_log.append({
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "score": self.current_score,
            "conflicts": total_conflicts,
            "thoughts": list(self.thought_history)
        })

        print(f"[META COHERENCE] 🧠 Score: {self.current_score} | Conflicts: {total_conflicts}")
        return self.current_score

    def _is_contradictory(self, a, b):
        contradiction_keywords = ["not", "never", "no", "opposite", "contradict", "fail"]
        return any(word in a.lower() and word in b.lower() and a.lower() != b.lower() for word in contradiction_keywords)

    def get_log(self, limit=5):
        return self.coherence_log[-limit:]

    def reset(self):
        self.thought_history.clear()
        self.coherence_log.clear()
        self.current_score = 1.0
