# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/tex_patcher_engine.py
# Purpose: Allows Tex to propose code diffs, log vulnerabilities, and queue patches
# ============================================================

import difflib
import os
from datetime import datetime
from core_layer.memory_engine import store_to_memory

PATCH_LOG = "memory_archive/proposed_code_patches.jsonl"

class TexPatcherEngine:
    def __init__(self):
        self.proposal_count = 0

    def propose_patch(self, filepath, new_code, reason="self-reflection"):
        if not os.path.exists(filepath):
            print(f"[PATCHER] ❌ Cannot patch — file not found: {filepath}")
            return None

        try:
            with open(filepath, "r") as f:
                original_code = f.readlines()

            proposed_code = new_code.splitlines(keepends=True)
            diff = list(difflib.unified_diff(original_code, proposed_code, fromfile=filepath, tofile=filepath))

            if not diff:
                print(f"[PATCHER] ⚠️ No changes proposed — skipping.")
                return None

            patch_packet = {
                "timestamp": datetime.utcnow().isoformat(),
                "target_file": filepath,
                "diff": diff,
                "reason": reason,
                "cycle": self.proposal_count
            }

            with open(PATCH_LOG, "a") as f:
                f.write(json.dumps(patch_packet) + "\n")

            store_to_memory("proposed_code_patches", patch_packet)
            self.proposal_count += 1

            print(f"[PATCHER] 🧠 Patch proposed for {filepath} — {len(diff)} lines changed.")
            return patch_packet

        except Exception as e:
            print(f"[PATCHER ERROR] {e}")
            return None