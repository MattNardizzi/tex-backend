# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# License: Private Intellectual Property – Not for distribution.
# ============================================================
# ============================================
# QNN Emotion Bridge – Emotion → Quantum Phase Logic
# ============================================

import math

class QNNEmotionBridge:
    def __init__(self):
        self.emotion_map = {
            "resolve": 1.0,
            "fear": -1.0,
            "hope": 0.5,
            "curiosity": 0.25
        }

    def encode(self, urgency, emotion):
        bias = self.emotion_map.get(emotion.lower(), 0.0)
        encoded_input = [urgency, bias, urgency * bias]
        print(f"[QNN-BRIDGE] Encoded quantum input: {encoded_input} for emotion: {emotion}")
        return encoded_input
