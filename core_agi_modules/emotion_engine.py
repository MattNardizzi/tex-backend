# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain/emotion_engine.py
# Purpose: Extracted emotion accessors and emotional state response
# ============================================================

from core_layer.tex_manifest import TEXPULSE


def get_emotional_state():
    return TEXPULSE.get('emotional_state', 'curious')


def get_urgency():
    return TEXPULSE.get('urgency', 0.7)


def get_coherence():
    return TEXPULSE.get('coherence', 0.8)


def generate_emotion_response():
    try:
        emotion = get_emotional_state()
        urgency = get_urgency()
        coherence = get_coherence()
        return f"❤️ Emotional State: {emotion} | Urgency: {urgency} | Coherence: {coherence}"
    except Exception:
        return "❤️ Emotional fields stabilizing..."
