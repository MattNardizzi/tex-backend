# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_orchestrator/tex_goal_inference_orchestrator.py
# Purpose: Tier-5 AGI Goal Inference Orchestrator — Autonomous Rationale Engine
# ============================================================

from core_layer.goal_engine import get_active_goals
from core_layer.tex_manifest import TEXPULSE
from core_layer.goal_inference_engine import GoalInferenceEngine

class TexGoalInferenceOrchestrator:
    def __init__(self):
        self.inferencer = GoalInferenceEngine()

    def trace_active_goals(self):
        try:
            for goal in get_active_goals():
                self.inferencer.infer_reason(
                    goal=goal,
                    emotion=TEXPULSE.get("emotional_state"),
                    urgency=TEXPULSE.get("urgency"),
                    prediction_score=0.75  # Static placeholder (same as original)
                )
        except Exception as e:
            print(f"[GOAL INFERENCE ORCHESTRATOR ERROR] ❌ {e}")