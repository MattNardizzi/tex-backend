# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_orchestrators/tex_codex_orchestrator.py
# Purpose: Orchestrate Codex Sync & Validation Subsystem
# ============================================================

from core_agi_modules.tex_codex_sync import TexCodexSync

class TexCodexOrchestrator:
    def __init__(self):
        self.codex_sync = TexCodexSync()

    def validate_codex_modules(self):
        try:
            result = self.codex_sync.validate_codex()
            print(f"[CODEX ORCHESTRATOR] ✅ Codex modules verified → {len(result)} modules")
        except Exception as e:
            print(f"[CODEX ORCHESTRATOR ERROR] ❌ Failed Codex sync: {e}")