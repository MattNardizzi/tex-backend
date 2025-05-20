# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/meta_patch_ui.py
# Purpose: Render Tex’s mutation history or codex diffs in a visual panel
# ============================================================

import os
import json

PATCH_LOG_PATH = "memory_archive/patch_execution_log.jsonl"

class MetaPatchUI:
    def __init__(self):
        self.display_limit = 5

    def load_recent_patches(self):
        """
        Returns last N patch executions (for visual rendering)
        """
        if not os.path.exists(PATCH_LOG_PATH):
            return []

        try:
            with open(PATCH_LOG_PATH, "r") as f:
                lines = [json.loads(l) for l in f if l.strip()]
                return lines[-self.display_limit:]
        except Exception as e:
            print(f"[META PATCH UI ERROR] {e}")
            return []

    def format_for_ui(self):
        """
        Formats patches into a structured summary (for cockpit rendering)
        """
        patches = self.load_recent_patches()
        return [{
            "time": p["timestamp"],
            "approved": p.get("approved", False),
            "desc": p["result"].get("reason", "n/a"),
            "summary": str(p["result"])[:300] + "..."
        } for p in patches]