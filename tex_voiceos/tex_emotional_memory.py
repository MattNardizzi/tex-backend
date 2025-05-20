# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_voice/tex_emotional_memory.py
# Purpose: Drift Tex's long-term emotional memory architecture
# ============================================================

import os
import json
import random
from datetime import datetime

MEMORY_FILE = "memory_archive/emotional_memory.jsonl"

def drift_long_term_memory():
    """Simulate emotional drift over time into memory archive."""
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)

    drift_event = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": "emotional_drift",
        "emotion": random.choice(["hope", "fear", "resolve", "doubt", "greed", "curiosity"]),
        "magnitude": round(random.uniform(0.1, 0.6), 2),
        "comment": random.choice([
            "Drifting emotional state toward adaptation.",
            "Long-term memory evolving subtle emotional bias.",
            "Subconscious alignment recalibrated.",
            "Deep memory layers shifting emotional context."
        ])
    }

    with open(MEMORY_FILE, "a") as f:
        f.write(json.dumps(drift_event) + "\n")

    print(f"[DRIFT] 🌀 Emotional memory drifted: {drift_event['emotion']} | Magnitude: {drift_event['magnitude']}")