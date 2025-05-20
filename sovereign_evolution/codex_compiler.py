# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/codex_compiler.py
# Purpose: Fuse reasoning fragments into executable logic snippets
# ============================================================

import os
import json
from datetime import datetime

COMPILED_CODEX_PATH = "memory_archive/compiled_codex_fragments.jsonl"

class CodexCompiler:
    def __init__(self):
        os.makedirs(os.path.dirname(COMPILED_CODEX_PATH), exist_ok=True)

    def compile(self, reasoning_fragments, context="unknown"):
        """
        Accepts a list of strings (thought fragments), and compiles them into a synthetic codex block.
        """
        fragment_block = "\n".join(reasoning_fragments)
        codex = {
            "timestamp": datetime.utcnow().isoformat(),
            "context": context,
            "compiled_logic": fragment_block,
            "lines": len(reasoning_fragments)
        }

        with open(COMPILED_CODEX_PATH, "a") as f:
            f.write(json.dumps(codex) + "\n")

        print(f"[CODEX COMPILER] 🧠 Codex logic compiled ({codex['lines']} lines)")
        return codex