# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/bias_awareness_monitor.py
# Purpose: Monitors Tex’s internal emotion and coherence for bias drift
# ============================================================

import json
import os
from core_layer.tex_manifest import TEXPULSE
from datetime import datetime

BIAS_LOG_PATH = "memory_archive/bias_detections.jsonl"

def monitor_bias_drift(cycle_id: int):
    emotion = TEXPULSE.get("emotional_state", "neutral")
    urgency = TEXPULSE.get("urgency", 0.5)
    coherence = TEXPULSE.get("coherence", 0.5)

    drift_detected = False
    reason = None

    if emotion in ["hope", "greed"] and coherence < 0.55:
        drift_detected = True
        reason = "optimism_bias"

    if emotion == "fear" and urgency > 0.85:
        drift_detected = True
        reason = "panic_bias"

    if drift_detected:
        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "cycle": cycle_id,
            "bias_type": reason,
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence
        }
        os.makedirs(os.path.dirname(BIAS_LOG_PATH), exist_ok=True)
        with open(BIAS_LOG_PATH, "a") as f:
            f.write(json.dumps(event) + "\n")