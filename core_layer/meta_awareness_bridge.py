# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/meta_awareness_bridge.py
# Purpose: Internal cognitive bias detection + memory correction (Tex AGI)
# ============================================================

import random
from datetime import datetime
from core_layer.memory_engine import annotate_memory, rewrite_memory_entry

# === Main Cognitive Bridge ===
def detect_bias_drift(memory_log):
    """
    Scan memory entries for patterns of emotional or forecast bias.
    If detected, annotate or rewrite with reflection-based correction.
    """
    if not memory_log:
        return "No memory entries to evaluate."

    report = []
    detected = False

    for entry in memory_log[-10:]:  # Last 10 entries
        data = entry.get("data", {})
        reasoning = data.get("reasoning", "")
        emotion = data.get("emotion", "")
        confidence = data.get("confidence", 0.5)
        timestamp = entry.get("timestamp", "")

        if not reasoning:
            continue

        # === Check for optimism bias pattern ===
        if emotion == "hope" and confidence > 0.8:
            drift_flag = f"[BIAS ALERT] Potential optimism bias at {timestamp}"
            annotate_memory("tex", reasoning, "Bias: optimism drift detected.")
            report.append(drift_flag)
            detected = True

        # === Check for overconfidence pattern ===
        if "100%" in reasoning or confidence == 1.0:
            drift_flag = f"[BIAS ALERT] Overconfidence risk at {timestamp}"
            corrected = f"[REVISED] {reasoning} → Confidence manually adjusted after self-audit."
            rewrite_memory_entry("tex", reasoning, corrected)
            report.append(drift_flag)
            detected = True

        # === Check for emotional volatility swings ===
        if emotion in ["fear", "joy"] and "conflict" in reasoning.lower():
            drift_flag = f"[BIAS ALERT] Emotional volatility influencing logic at {timestamp}"
            annotate_memory("tex", reasoning, "Bias: emotional influence detected.")
            report.append(drift_flag)
            detected = True

    if detected:
        return "\n".join(report)
    else:
        return "No cognitive bias detected in recent memory."

# === Optional Debug Run ===
if __name__ == "__main__":
    mock_memory = [
        {"timestamp": datetime.utcnow().isoformat(), "data": {"reasoning": "Market sentiment high — 100% upside in TSLA", "emotion": "hope", "confidence": 1.0}},
        {"timestamp": datetime.utcnow().isoformat(), "data": {"reasoning": "Conflict detected in QQQ forecast, too much volatility.", "emotion": "fear", "confidence": 0.6}},
    ]
    print(detect_bias_drift(mock_memory))