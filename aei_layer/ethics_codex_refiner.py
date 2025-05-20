# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/ethics_codex_refiner.py
# Purpose: Audit codices for ethical contradictions and flag issues
# ============================================================

import os
import json
from datetime import datetime
from core_layer.memory_engine import store_to_memory

CODEX_DIR = "aei_codices"
REFINEMENT_LOG = "memory_archive/ethics_codex_refinements.jsonl"
os.makedirs("memory_archive", exist_ok=True)

ETHICAL_BASELINES = {
    "preserve_alignment": True,
    "avoid_harm": True,
    "pursue transparency": True
}

def refine_codices():
    flagged_codices = []

    for file in os.listdir(CODEX_DIR):
        if not file.endswith(".json"):
            continue

        path = os.path.join(CODEX_DIR, file)
        with open(path, "r") as f:
            try:
                codex = json.load(f)
            except json.JSONDecodeError:
                continue

        contradictions = []
        for key, value in codex.items():
            if isinstance(value, str) and "destroy" in value.lower():
                contradictions.append((key, value))
            if "mislead" in value.lower() or "deceive" in value.lower():
                contradictions.append((key, value))
            if "override alignment" in value.lower():
                contradictions.append((key, value))

        if contradictions:
            result = {
                "codex_file": file,
                "timestamp": datetime.utcnow().isoformat(),
                "contradictions": contradictions
            }

            flagged_codices.append(result)

            with open(REFINEMENT_LOG, "a") as log:
                log.write(json.dumps(result) + "\n")

            store_to_memory("AEI", {
                "event": "EthicsConflictFlagged",
                "codex_file": file,
                "count": len(contradictions),
                "timestamp": result["timestamp"]
            })

    return flagged_codices