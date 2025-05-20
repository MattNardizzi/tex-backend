# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_orchestrator/tex_persona_orchestrator.py
# Purpose: Persona Activation + Identity Engine for Tex AGI
# ============================================================

from core_layer.persona_engine import PersonaEngine

class TexPersonaOrchestrator:
    def __init__(self):
        self.persona_engine = PersonaEngine()

    def activate_identity(self):
        try:
            self.persona_engine.activate()
            print(f"[PERSONA ORCHESTRATOR] ✅ Persona activated: {self.persona_engine.identity}")
        except Exception as e:
            print(f"[PERSONA ORCHESTRATOR ERROR] ❌ {e}")