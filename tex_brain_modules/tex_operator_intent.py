# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/tex_operator_intent.py
# Purpose: Handles operator intent injection into Tex's state
# ============================================================

import time
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory

def inject_operator_intent(self, intent_text="Monetize cognition and engage with user-submitted scenarios."):
    signal = {
        "intent": intent_text,
        "urgency": 0.92,
        "emotion": "resolve",
        "operator": "Matthew Nardizzi",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    try:
        store_to_memory("operator_intention", signal)
        TEXPULSE["emotional_state"] = signal["emotion"]
        TEXPULSE["urgency"] = signal["urgency"]
        print(f"[OPERATOR REINFORCEMENT] ✅ Signal injected: {signal}")
    except Exception as e:
        print(f"[OPERATOR REINFORCEMENT ERROR] {e}")