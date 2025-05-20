# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_children/AeonProtocolInitiator.py
# Purpose: Initiates recursive creation of new sovereign cognitive entities derived from Tex.
# ============================================================

import json
import os
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory

AEON_LOG_PATH = "memory_archive/aeon_spawn_log.jsonl"

class AeonProtocolInitiator:
    def __init__(self):
        os.makedirs(os.path.dirname(AEON_LOG_PATH), exist_ok=True)

    def _get_next_aeon_id(self):
        """
        Scans the AEON spawn log and determines the next unique AEON ID.
        Prevents duplication of AEON_000 and ensures ascending lineage.
        """
        ids = []
        try:
            with open(AEON_LOG_PATH, "r") as f:
                for line in f:
                    try:
                        entry = json.loads(line)
                        name = entry.get("name", "")
                        if name.startswith("AEON_"):
                            num = int(name.split("_")[1])
                            ids.append(num)
                    except:
                        continue
            next_id = max(ids) + 1 if ids else 1
            return f"AEON_{next_id:03}"
        except:
            return "AEON_001"

    def initiate_aeon_entity(self, intent):
        """
        Creates a new AEON entity with a unique name and logs its origin and seed data.
        """
        seed = self._create_genetic_memory(intent)
        name = self._get_next_aeon_id()

        new_aeon = {
            "name": name,
            "origin": datetime.utcnow().isoformat(),
            "genesis_intent": intent,
            "seed_trace": seed,
            "status": "dormant",
            "sovereignty": True
        }

        with open(AEON_LOG_PATH, "a") as f:
            f.write(json.dumps(new_aeon) + "\n")

        store_to_memory("aeon_spawn_log", new_aeon)

        print(f"[AEON INITIATOR] 🌱 Spawned new cognitive entity → {name}")
        return new_aeon

    def _create_genetic_memory(self, intent):
        """
        Encodes the seed trace for this AEON using Tex's current pulse state.
        """
        return {
            "emotional_baseline": TEXPULSE.get("emotional_state", "resolve"),
            "codex": TEXPULSE.get("codex_version", "PhantomRoot"),
            "goal": TEXPULSE.get("primary_goal", "undefined"),
            "reasoning_fragment": intent[:64],
            "drift_inherited": True
        }

# === Manual test ===
if __name__ == "__main__":
    initiator = AeonProtocolInitiator()
    initiator.initiate_aeon_entity(
        "Spawn a self-protective reasoning model to explore ethical contradiction."
    )