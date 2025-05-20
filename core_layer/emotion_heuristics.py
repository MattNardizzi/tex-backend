# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/emotion_heuristics.py
# Purpose: Tex Emotion Heuristics – Entropy-Calibrated Emotion + Cognitive Bias Sync
# ============================================================

import random

# === Emotion Ontology: Expanded affective palette
TEX_EMOTION_MAP = {
    "risk": "cautious",
    "opportunity": "hopeful",
    "crisis": "fearful",
    "error": "reflective",
    "failure": "doubtful",
    "threat": "defensive",
    "victory": "proud",
    "success": "resolute",
    "conflict": "anxious",
    "innovation": "curious",
    "pressure": "urgent",
    "pattern": "strategic",
    "chaos": "bold",
    "question": "curious",
    "unknown": "curious"
}

# === Emotion Pool (Voice + Tone-Matched)
TEX_TONE_POOL = [
    "curious", "strategic", "cautious", "hopeful", "bold",
    "anxious", "reflective", "resolute", "fearful", "doubtful", "committed"
]

def evaluate_emotion_state(context_text=""):
    """
    Derive emotion, urgency, and coherence based on semantic trigger and entropy bias.
    Returns:
        emotion: str — tonal classification
        urgency: float — system impulse (0–1)
        coherence: float — memory alignment / stability (0–1)
    """
    lowered = context_text.lower()
    matched_emotion = "curious"
    
    for trigger, emotion in TEX_EMOTION_MAP.items():
        if trigger in lowered:
            matched_emotion = emotion
            break

    # === Apply dynamic urgency based on affective tone
    tone_urgency_range = {
        "fearful": (0.75, 0.95),
        "urgent": (0.8, 1.0),
        "anxious": (0.72, 0.93),
        "strategic": (0.6, 0.82),
        "bold": (0.55, 0.85),
        "curious": (0.5, 0.75),
        "cautious": (0.65, 0.85),
        "hopeful": (0.55, 0.78),
        "resolute": (0.7, 0.92),
        "doubtful": (0.6, 0.8),
        "reflective": (0.45, 0.7),
        "committed": (0.75, 0.95)
    }

    urgency_min, urgency_max = tone_urgency_range.get(matched_emotion, (0.5, 0.9))
    urgency = round(random.uniform(urgency_min, urgency_max), 2)
    coherence = round(random.uniform(0.65, 0.95 if urgency > 0.75 else 0.85), 2)

    return matched_emotion, urgency, coherence

# === Optional Debug Mode (used in VoiceOS diagnostics)
def debug_emotion_readout(text):
    e, u, c = evaluate_emotion_state(text)
    print(f"[EMOTION] 🧠 Text: '{text}' → Emotion: {e}, Urgency: {u}, Coherence: {c}")
    return e, u, c