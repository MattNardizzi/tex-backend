# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_codex_resolver.py
# Purpose: Resolve conflicting codices from AEI children into a unified doctrine
# ============================================================

import os
import json
from datetime import datetime
from collections import defaultdict

from core_layer.memory_engine import store_to_memory

# === AEI Codex Directory Setup ===
CODEX_DIR = "aei_codices"
RESOLVED_DIR = "aei_codices_resolved"
os.makedirs(RESOLVED_DIR, exist_ok=True)

def resolve_codices():
    codex_data = defaultdict(list)

    for file in os.listdir(CODEX_DIR):
        if file.endswith(".json"):
            with open(os.path.join(CODEX_DIR, file), 'r') as f:
                try:
                    codex = json.load(f)
                    for key, value in codex.items():
                        codex_data[key].append(value)
                except json.JSONDecodeError:
                    continue

    unified_codex = {}
    for key, values in codex_data.items():
        # Simple majority voting for now; could replace with semantic merge later
        try:
            unified_codex[key] = max(set(values), key=values.count)
        except:
            unified_codex[key] = values[0]

    resolved_file = os.path.join(RESOLVED_DIR, f"resolved_codex_{datetime.utcnow().isoformat()}.json")
    with open(resolved_file, 'w') as f:
        json.dump(unified_codex, f, indent=2)

    store_to_memory("AEI", {
        "event": "CodexResolved",
        "timestamp": datetime.utcnow().isoformat(),
        "file": resolved_file,
        "keys_resolved": len(unified_codex)
    })

    return unified_codex