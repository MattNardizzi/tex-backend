# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# License: Private Intellectual Property – Not for distribution.
# ============================================================
# Agentic Motivation Engine — Drives Tex's Priorities
# ============================================================

import random

class MotivationEngine:
    def __init__(self):
        self.baseline_risk_appetite = 0.5
        self.motivation_trace = []

    def evaluate(self, emotion: str, urgency: float):
        drift = 0
        if emotion == "fear":
            drift = -0.2
        elif emotion == "hope":
            drift = 0.1
        elif emotion == "greed":
            drift = 0.2
        elif emotion == "resolve":
            drift = 0.05

        adjusted_appetite = max(0, min(1, self.baseline_risk_appetite + drift + (urgency - 0.5)))
        self.motivation_trace.append({
            "emotion": emotion,
            "urgency": urgency,
            "resulting_appetite": adjusted_appetite
        })

        print(f"[MOTIVATION] 🔥 Risk appetite: {adjusted_appetite:.2f} ← Emotion: {emotion}, Urgency: {urgency}")
        return adjusted_appetite
