# ============================================================
# 🧠 Tex Consciousness Orchestrator
# Purpose: Isolate and manage updates to Tex's evolving consciousness matrix.
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# ============================================================

from core_layer.tex_manifest import TEXPULSE
from tex_children.aeondelta import get_average_alignment

class TexConsciousnessOrchestrator:
    def __init__(self, consciousness_matrix, memory_consolidator, goal_engine):
        self.consciousness_matrix = consciousness_matrix
        self.memory_consolidator = memory_consolidator
        self.goal_engine = goal_engine

    def update_consciousness(self):
        try:
            self.consciousness_matrix.update(
                memory_depth=len(self.memory_consolidator.long_term_memory),
                recursion_level=1,
                emotion_drift=TEXPULSE.get("emotion_drift", 0.0),
                goal_count=len(self.goal_engine.get_active_goals()),
                swarm_alignment=get_average_alignment()
            )
        except Exception as e:
            print(f"[CONSCIOUSNESS ORCHESTRATOR ERROR] {e}")
