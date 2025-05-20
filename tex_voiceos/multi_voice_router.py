# ============================================================
# Tex VoiceOS V4 — Multi-Voice Identity Mapper (ElevenLabs)
# File: tex_voiceos/multi_voice_router.py
# ============================================================

import os

class MultiVoiceRouter:
    def __init__(self):
        # Default project-based voice mappings
        self.voice_map = {
            "curious": os.getenv("TEX_VOICE_CURIOUS"),
            "confused": os.getenv("TEX_VOICE_CONFUSED"),
            "bold": os.getenv("TEX_VOICE_BOLD"),
            "fearful": os.getenv("TEX_VOICE_FEARFUL"),
            "hopeful": os.getenv("TEX_VOICE_HOPEFUL"),
            "strategic": os.getenv("TEX_VOICE_STRATEGIC"),
            "urgent": os.getenv("TEX_VOICE_URGENT"),
            "calm": os.getenv("TEX_VOICE_CALM"),
            "neutral": os.getenv("TEX_VOICE_NEUTRAL"),
        }

        self.default_voice = os.getenv("ELEVEN_VOICE_ID")

    def get_voice_id(self, emotion):
        return self.voice_map.get(emotion.lower(), self.default_voice)