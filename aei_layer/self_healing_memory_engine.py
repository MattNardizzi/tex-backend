# ============================================================
# © 2025 VortexBlack LLC — AEI Layer
# File: self_healing_memory_engine.py
# Purpose: Auto-correct corrupted or incoherent memory logs in Tex's memory archive
# ============================================================

import os
import json
from datetime import datetime

MEMORY_FILE = "memory_archive/tex_memory.jsonl"
HEAL_LOG_FILE = "memory_archive/memory_healing_log.jsonl"

def self_heal_memory():
    healed_entries = 0
    rewritten = []

    if not os.path.exists(MEMORY_FILE):
        return

    try:
        with open(MEMORY_FILE, "r") as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            try:
                entry = json.loads(line)
                if "reasoning" not in entry or not entry["reasoning"].strip():
                    entry["reasoning"] = "[HEALED] Reasoning missing — entry repaired."
                    healed_entries += 1
                    rewritten.append(entry)
                elif entry.get("reasoning") == "None" or "???" in entry.get("reasoning", ""):
                    entry["reasoning"] = f"[HEALED @ {datetime.utcnow().isoformat()}] Corrupted reasoning replaced."
                    healed_entries += 1
                    rewritten.append(entry)
            except json.JSONDecodeError:
                continue

        if healed_entries > 0:
            with open(MEMORY_FILE, "w") as f:
                for entry in rewritten:
                    f.write(json.dumps(entry) + "\n")

            with open(HEAL_LOG_FILE, "a") as logf:
                logf.write(json.dumps({
                    "timestamp": datetime.utcnow().isoformat(),
                    "healed_count": healed_entries
                }) + "\n")

    except Exception as e:
        print(f"[MEMORY HEALING ERROR] {e}")