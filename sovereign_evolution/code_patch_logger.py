# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/code_patch_logger.py
# Purpose: Log patch attempts and mutations for audit and transparency
# ============================================================

import os
import json
from datetime import datetime

PATCH_EXECUTION_LOG = "memory_archive/patch_execution_log.jsonl"

class CodePatchLogger:
    def __init__(self):
        os.makedirs(os.path.dirname(PATCH_EXECUTION_LOG), exist_ok=True)

    def log(self, patch_result, approved=False):
        """
        Logs the result of a proposed or executed patch mutation.
        """
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "result": patch_result,
            "approved": approved
        }

        try:
            with open(PATCH_EXECUTION_LOG, "a") as f:
                f.write(json.dumps(entry) + "\n")
            print(f"[PATCH LOGGER] 📜 Logged patch execution.")
        except Exception as e:
            print(f"[PATCH LOGGER ERROR] {e}")