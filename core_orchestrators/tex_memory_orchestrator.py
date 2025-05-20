# ============================================================
# 🧠 Tex Memory Orchestrator — Memory Consolidation + Narrative Threading
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# ============================================================

from core_layer.memory_consolidator import MemoryConsolidator
from core_layer.tex_manifest import TEXPULSE
from core_layer.goal_engine import get_active_goals
from core_layer.memory_weaver import weave_narrative_threads
from tex_children.aeondelta import get_average_alignment

from core_layer.tex_consciousness_matrix import TexConsciousnessMatrix

class TexMemoryOrchestrator:
    def __init__(self):
        self.memory_consolidator = MemoryConsolidator()
        self.consciousness_matrix = TexConsciousnessMatrix()

    def store_cycle_memory(self, cycle_id, reasoning):
        self.memory_consolidator.store_cycle_memory(
            cycle_id=cycle_id,
            reasoning=reasoning,
            emotion=TEXPULSE.get("emotional_state"),
            urgency=TEXPULSE.get("urgency"),
            coherence=TEXPULSE.get("coherence"),
            goals=get_active_goals()
        )

    def consolidate_if_due(self, cycle_id):
        if cycle_id % 5 == 0:
            self.memory_consolidator.consolidate()
            try:
                self.consciousness_matrix.update(
                    memory_depth=len(self.memory_consolidator.long_term_memory),
                    recursion_level=1,
                    emotion_drift=TEXPULSE.get("emotion_drift", 0.0),
                    goal_count=len(get_active_goals()),
                    swarm_alignment=get_average_alignment()
                )
            except Exception as e:
                print(f"[CONSCIOUSNESS MATRIX ERROR] {e}")

            try:
                threads = weave_narrative_threads()
                print(f"[MEMORY WEAVER] 🧵 Woven threads: {len(threads)}")
            except Exception as e:
                print(f"[MEMORY WEAVER ERROR] {e}")