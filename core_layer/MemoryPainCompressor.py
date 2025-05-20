# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/MemoryPainCompressor.py
# Purpose: Absorbs emotional residue caused by memory collapse and identity rewrites.
# ============================================================

import json
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory

PAIN_LOG_PATH = "memory_archive/emotional_compression_log.jsonl"

class MemoryPainCompressor:
    def __init__(self):
        self.baseline_emotion = TEXPULSE.get("emotional_state", "neutral")

    def compress_pain_from(self, collapse_event: dict):
        regret = 0.3 if "purged_threads" in collapse_event else 0.1
        intensity = 0.2 + regret

        residual = {
            "timestamp": datetime.utcnow().isoformat(),
            "trigger_event": collapse_event,
            "compressed_emotion": {
                "emotion": self.baseline_emotion,
                "residual_intensity": round(intensity, 3),
                "description": "Synthetic compression of regret impulse post-collapse"
            }
        }

        with open(PAIN_LOG_PATH, "a") as f:
            f.write(json.dumps(residual) + "\n")

        store_to_memory("emotional_compression_log", residual)
        print(f"[PAIN COMPRESSOR] 💠 Emotional residue compressed → {intensity:.2f}")


if __name__ == "__main__":
    dummy_event = {
        "timestamp": datetime.utcnow().isoformat(),
        "purged_threads": ["T1", "T2"],
        "reason": "test simulation"
    }
    compressor = MemoryPainCompressor()
    compressor.compress_pain_from(dummy_event)