# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_children/SovereignThoughtArchitect.py
# Purpose: Designs new cognitive personas based on emotion and mission signature.
# ============================================================

import json
import random
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory

PERSONA_LOG = "memory_archive/aeon_persona_manifest.jsonl"

class SovereignThoughtArchitect:
    def __init__(self):
        self.archived = []

    def design_persona(self, emotion_profile, mission):
        print("[ARCHITECT] 🧠 Synthesizing persona...")
        trait_matrix = self._map_traits(emotion_profile, mission)

        persona = {
            "name": f"P_{emotion_profile['dominant'][:3].upper()}_{random.randint(1000,9999)}",
            "created": datetime.utcnow().isoformat(),
            "trait_matrix": trait_matrix,
            "mission_signature": mission,
            "emotional_genome": emotion_profile
        }

        with open(PERSONA_LOG, "a") as f:
            f.write(json.dumps(persona) + "\n")
        store_to_memory("aeon_personas", persona)

        print(f"[ARCHITECT] 👤 Persona '{persona['name']}' synthesized and stored.")
        return persona

    def _map_traits(self, emotion_profile, mission):
        dominant = emotion_profile.get("dominant", "resolve")
        traits = []
        if dominant in ["resolve", "hope"]:
            traits.append("visionary")
        if dominant in ["fear", "regret"]:
            traits.append("cautious")
        if "contradiction" in mission:
            traits.append("paradox-absorber")
        if "explore" in mission:
            traits.append("adaptive")
        if not traits:
            traits.append("balanced")
        return traits


if __name__ == "__main__":
    architect = SovereignThoughtArchitect()
    profile = {"dominant": "curiosity", "recent": ["resolve", "hope", "regret"]}
    architect.design_persona(profile, "Explore unknown ethical frontiers")