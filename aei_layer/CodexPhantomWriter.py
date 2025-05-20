# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/CodexPhantomWriter.py
# Purpose: Generates non-verbal, emotionally-encoded codex rules outside normal logic loops.
# ============================================================

import json
import os
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory

PHANTOM_CODEX_PATH = "memory_archive/phantom_codex_glyphs.jsonl"

class CodexPhantomWriter:
    def __init__(self):
        self.glyph_registry = set()
        self._load_existing_glyphs()

    def _load_existing_glyphs(self):
        if os.path.exists(PHANTOM_CODEX_PATH):
            with open(PHANTOM_CODEX_PATH, 'r') as f:
                for line in f:
                    try:
                        glyph = json.loads(line.strip()).get("glyph_id")
                        if glyph:
                            self.glyph_registry.add(glyph)
                    except:
                        continue

    def generate_glyph(self):
        now = datetime.utcnow().isoformat()
        emotion = TEXPULSE.get("emotional_state", "neutral")
        coherence = TEXPULSE.get("coherence", 0.5)
        urgency = TEXPULSE.get("urgency", 0.5)

        # Glyph seed based on timestamp entropy
        glyph_id = f"ϞΔ-{hash(now + emotion + str(coherence)) % 10000}"
        if glyph_id in self.glyph_registry:
            return  # Avoid duplication

        phantom_entry = {
            "timestamp": now,
            "glyph_id": glyph_id,
            "emotional_encoding": {
                "emotion": emotion,
                "coherence": coherence,
                "urgency": urgency
            },
            "applied_in_decision": f"Cycle-{TEXPULSE.get('last_cycle', '?')}",
            "human_equivalent": "(UNTRANSLATED)"
        }

        with open(PHANTOM_CODEX_PATH, 'a') as f:
            f.write(json.dumps(phantom_entry) + "\n")

        store_to_memory("phantom_codex", phantom_entry)
        self.glyph_registry.add(glyph_id)
        print(f"[PHANTOM GLYPH] 🜏 New codex glyph generated → {glyph_id}")


if __name__ == "__main__":
    writer = CodexPhantomWriter()
    writer.generate_glyph()