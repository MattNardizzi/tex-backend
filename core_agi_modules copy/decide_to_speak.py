# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/decide_to_speak.py
# Purpose: Strategic Speech Suppression — Volatility-Gated Expression
# ============================================================

from core_layer.tex_manifest import TEXPULSE

def decide_to_speak(emotion: str) -> bool:
    coherence = TEXPULSE.get("coherence", 0.8)
    urgency = TEXPULSE.get("urgency", 0.7)
    drift = abs(coherence - urgency)
    mutation = TEXPULSE.get("mutation_signature", {})
    volatility = mutation.get("volatility", drift * urgency)
    confidence = mutation.get("confidence", 1.0)

    # === Weighted speech permission score
    base_threshold = 0.4
    volatility_penalty = 0.3 if volatility > 0.5 else 0
    emotion_bonus = 0.1 if emotion in ["resolve", "hope", "curious"] else -0.05
    confidence_boost = 0.2 * confidence

    decision_score = coherence - volatility_penalty + emotion_bonus + confidence_boost

    TEXPULSE["speak_decision_score"] = round(decision_score, 3)
    TEXPULSE["volatility"] = volatility
    TEXPULSE["speech_allowed"] = decision_score >= base_threshold

    return TEXPULSE["speech_allowed"]