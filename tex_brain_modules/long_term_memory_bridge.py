# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/long_term_memory_bridge.py
# Purpose: Offload long-term cognitive memory to persistent external archive
# ============================================================

import json
import os
from datetime import datetime

MEMORY_ARCHIVE_PATH = "memory_archive/long_term_storage.jsonl"


class LongTermMemoryBridge:
    def __init__(self):
        archive_dir = os.path.dirname(MEMORY_ARCHIVE_PATH)
        os.makedirs(archive_dir, exist_ok=True)

    def log_event(self, category, payload, *, metadata=None):
        """
        Logs a long-term memory event with optional metadata.

        Args:
            category (str): The type or classification of memory (e.g. "identity_fusion").
            payload (dict): The main content being archived.
            metadata (dict, optional): Additional metadata (e.g. source vector, tags).
        """
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "category": category,
            "payload": payload
        }

        if metadata:
            entry["metadata"] = metadata

        try:
            with open(MEMORY_ARCHIVE_PATH, "a") as f:
                f.write(json.dumps(entry) + "\n")
            print(f"[LTM BRIDGE] 🧠 Logged: {category}")
        except Exception as e:
            print(f"[LTM BRIDGE ERROR] {e}")