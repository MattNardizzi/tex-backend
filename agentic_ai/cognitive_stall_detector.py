# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/cognitive_stall_detector.py
# Purpose: Detect stalled goals, recursion, contradiction in reasoning
# ============================================================

import os
import json
from datetime import datetime, timezone, timedelta
from core_layer.memory_engine import recall_recent
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

class CognitiveStallDetector:
    def __init__(self, memory_window=15, contradiction_threshold=0.88):
        self.memory_window = memory_window
        self.threshold = contradiction_threshold

    def _extract_thoughts(self):
        recent = recall_recent(n=20, within_minutes=self.memory_window)
        return [m["data"].get("explanation", "") for m in recent if "explanation" in m["data"]]

    def detect_looping_thoughts(self):
        thoughts = self._extract_thoughts()
        if len(thoughts) < 5:
            return False, "Not enough cognitive history"

        embeddings = model.encode(thoughts, convert_to_tensor=True)
        sim_matrix = util.pytorch_cos_sim(embeddings, embeddings).cpu().numpy()

        loop_count = 0
        for i in range(len(sim_matrix)):
            for j in range(i + 1, len(sim_matrix)):
                if sim_matrix[i][j] > self.threshold:
                    loop_count += 1

        is_looping = loop_count > 5
        return is_looping, f"Loop similarity count = {loop_count}" if is_looping else "Stable reasoning"

    def detect_stalled_goals(self):
        thoughts = self._extract_thoughts()
        if not thoughts:
            return False, "No reasoning history to analyze"

        recent_strategies = [t for t in thoughts if "strategy 'none'" in t]
        if len(recent_strategies) >= 10:
            return True, "Repeated fallback to 'none' strategy detected"

        return False, "Strategy pattern appears healthy"

    def check(self):
        looping, loop_msg = self.detect_looping_thoughts()
        stall, stall_msg = self.detect_stalled_goals()

        issues = []
        if looping:
            issues.append("cognitive_looping")
        if stall:
            issues.append("stalled_goals")

        return {
            "issues_detected": issues,
            "loop_check": loop_msg,
            "stall_check": stall_msg,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

# === CLI test ===
if __name__ == "__main__":
    detector = CognitiveStallDetector()
    result = detector.check()
    print("\n[Cognitive Stall Detection Report] 🧠")
    print(json.dumps(result, indent=4))
