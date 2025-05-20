# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# License: Private Intellectual Property – Not for distribution.
# ============================================================
# ============================================
# Tex Bootstrap – AGI Runtime Initializer
# ============================================

from core_layer.tex_manifest import TEXPULSE
from core_layer.goal_engine import GoalEngine
from core_layer.memory_engine import MemoryEngine
from core_layer.persona_engine import PersonaEngine

class TexBootstrap:
    def __init__(self):
        self.memory = MemoryEngine()
        self.goals = GoalEngine()
        self.persona = PersonaEngine()

    def boot(self):
        print("🚀 [BOOTSTRAP] Tex initializing...")
        print(f"🧠 [BOOTSTRAP] Codename: {TEXPULSE['codename']} | Version: {TEXPULSE['version']}")
        self.persona.activate()
        self.memory.initialize()
        self.goals.generate_goals()
        print("✅ [BOOTSTRAP] AGI systems active and synced.")
