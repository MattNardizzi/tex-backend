# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/emotion_drift_damper.py
# Purpose: Prevent runaway emotion loops by damping extreme drift values
# ============================================================

from core_layer.tex_manifest import TEXPULSE

class EmotionDriftDamper:
    def __init__(self, threshold=0.5, damping_factor=0.7):
        self.threshold = threshold  # Max allowed emotional drift
        self.damping_factor = damping_factor  # Scale factor for dampening

    def stabilize(self):
        drift = TEXPULSE.get("emotion_drift", 0.0)
        coherence = TEXPULSE.get("coherence", 1.0)

        if drift > self.threshold and coherence < 0.5:
            print(f"[DAMPER] 🧊 Emotion drift high ({drift}), coherence low ({coherence}) — dampening...")
            TEXPULSE["emotion_drift"] *= self.damping_factor
            TEXPULSE["urgency"] *= self.damping_factor
            TEXPULSE["coherence"] = min(1.0, TEXPULSE["coherence"] + 0.1)
            return True

        return False