# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/sovereign_codex_differ.py
# Purpose: Compare before/after Codex blocks to detect mutation deltas
# ============================================================

from difflib import unified_diff
from datetime import datetime

class SovereignCodexDiffer:
    def __init__(self):
        self.last_diff = None

    def compare_codex_fragments(self, original_lines, mutated_lines, context=""):
        """
        Returns a unified diff of two codex blocks.
        """
        diff = list(unified_diff(
            original_lines,
            mutated_lines,
            lineterm='',
            fromfile='original',
            tofile='mutated',
        ))

        self.last_diff = {
            "timestamp": datetime.utcnow().isoformat(),
            "context": context,
            "lines_changed": len(diff),
            "diff_output": diff
        }

        print(f"[CODEX DIFFER] 🧬 {len(diff)} lines changed during mutation ({context})")
        return self.last_diff