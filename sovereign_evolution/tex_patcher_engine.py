# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/tex_patcher_engine.py
# Purpose: Allows Tex to propose self-patches based on thought patterns or cognitive signals
# ============================================================

import os
import json
from datetime import datetime

PATCH_LOG_PATH = "memory_archive/patch_proposals.jsonl"

class TexPatcherEngine:
    def __init__(self):
        os.makedirs(os.path.dirname(PATCH_LOG_PATH), exist_ok=True)

    def propose_patch(self, module, function_name, description, patch_code, trigger_reason=""):
        """
        Tex proposes a patch to a file/function with reason and timestamp.
        """
        patch = {
            "timestamp": datetime.utcnow().isoformat(),
            "module": module,
            "function": function_name,
            "description": description,
            "proposed_patch": patch_code,
            "reason": trigger_reason
        }

        try:
            with open(PATCH_LOG_PATH, "a") as f:
                f.write(json.dumps(patch) + "\n")
            print(f"[TEX PATCHER] 🧠 Proposed patch to {module}.{function_name}")
        except Exception as e:
            print(f"[PATCHER ERROR] {e}")

        return patch