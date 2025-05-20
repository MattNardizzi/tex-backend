# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_orchestrator/tex_self_eval_orchestrator.py
# Purpose: Tex AGI Self-Evaluation Layer — Thought Evaluation + Mutation Trigger
# ============================================================

from core_layer.tex_self_eval_matrix import TexSelfEvalMatrix
from core_layer.tex_manifest import TEXPULSE
from evolution_layer.self_mutator import SelfMutator

class TexSelfEvalOrchestrator:
    def __init__(self, world_model, future_engine):
        self.evaluator = TexSelfEvalMatrix()
        self.self_mutator = SelfMutator()
        self.world_model = world_model
        self.future_engine = future_engine

    def run_self_eval(self, thought):
        try:
            snapshot = self.world_model.get_snapshot()
            current_goal = snapshot.get("active_goal", "")

            self.evaluator.evaluate(
                {
                    "thought": thought,
                    "goal": current_goal,
                    "actions": self.future_engine.last_actions if hasattr(self.future_engine, "last_actions") else []
                },
                {
                    "emotion": TEXPULSE.get("emotional_state")
                },
                trigger_mutation_fn=self.self_mutator.run_forced_mutation
            )
        except Exception as e:
            print(f"[SELF EVAL ORCHESTRATOR ERROR] ❌ {e}")