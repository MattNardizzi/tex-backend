# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/awareness_sync.py
# Purpose: Tex Awareness Sync — Pure Procedural Emotional Urgency State Management
# ============================================================

from agentic_ai.tex_awareness_sync import TexAwarenessSync

awareness = TexAwarenessSync(operator_name="Matthew Nardizzi")

def update_awareness(emotion, urgency, coherence, patch_payload):
    awareness.register_node("emotion", emotion)
    awareness.register_node("urgency", urgency)
    awareness.register_node("coherence", coherence)
    if patch_payload:
        awareness.register_node("suggested_patch", patch_payload.get("strategy", "none"))
    awareness.live_summary({
        "emotion": emotion,
        "urgency": urgency,
        "coherence": coherence,
        "suggested_patch": patch_payload.get("strategy", "none")
    })
