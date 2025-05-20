# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# License: Private Intellectual Property – Not for distribution.
# ============================================================
# ============================================
# Goal Inference Engine – Meta-Reasoning for Autonomous Goals
# ============================================

import random
import datetime
import uuid

try:
    from core_layer.tex_manifest import TEXPULSE
except ImportError:
    TEXPULSE = {"financial_uplink": False}

class GoalInferenceEngine:
    def __init__(self):
        self.inference_log = []

    def infer_reason(self, goal, emotion, urgency, prediction_score, memory_reference=None):
        """
        Generate a reason for why a goal was formed using emotion, urgency, and future forecast.
        If financial uplink is active, apply market-prioritized phrasing.
        """
        reason_id = str(uuid.uuid4())
        timestamp = datetime.datetime.utcnow().isoformat()

        if TEXPULSE.get("financial_uplink", False):
            rationale_fragments = [
                f"Market sentiment: '{emotion}'",
                f"Signal urgency: {round(urgency, 2)}",
                f"Forecast volatility score: {round(prediction_score, 3)}"
            ]
            if memory_reference:
                rationale_fragments.append(f"Historical trigger: {memory_reference[:80]}...")
        else:
            rationale_fragments = [
                f"Emotion: '{emotion}'",
                f"Urgency: {round(urgency, 2)}",
                f"Forecast score: {round(prediction_score, 3)}"
            ]
            if memory_reference:
                rationale_fragments.append(f"Memory anchor: {memory_reference[:80]}...")

        rationale = " | ".join(rationale_fragments)

        reason_entry = {
            "id": reason_id,
            "goal": goal,
            "reason": rationale,
            "timestamp": timestamp
        }

        self.inference_log.append(reason_entry)
        print(f"[GOAL INFERENCE] 🧠 {goal} ← {rationale}")
        return reason_entry

    def get_recent_inferences(self, limit=5):
        return self.inference_log[-limit:]

    def clear_inferences(self):
        self.inference_log.clear()
        print("[GOAL INFERENCE] 🧹 Cleared all inference history.")