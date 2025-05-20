# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: agentic_ai/agent_scorer.py
# Purpose: Evaluate and score Tex's child agents or debate paths
# ============================================================

from core_layer.memory_engine import store_to_memory
from core_layer.tex_manifest import TEXPULSE
from datetime import datetime
import uuid

class AgentScorer:
    def __init__(self):
        self.goal_weights = TEXPULSE.get("scoring_weights", {
            "alignment": 0.4,
            "performance": 0.3,
            "novelty": 0.2,
            "efficiency": 0.1
        })

    def score_agents(self, agent_outputs):
        scored_agents = []

        for agent in agent_outputs:
            score = self.compute_score(agent)
            agent_id = agent.get("id", str(uuid.uuid4()))
            log_entry = {
                "agent_id": agent_id,
                "timestamp": str(datetime.now()),
                "score": score,
                "reasoning": agent.get("reasoning", ""),
                "metrics": agent.get("metrics", {}),
            }
            store_to_memory("agent_scores", log_entry)
            scored_agents.append((agent_id, score, log_entry))

        scored_agents.sort(key=lambda x: x[1], reverse=True)
        return scored_agents

    def compute_score(self, agent):
        metrics = agent.get("metrics", {})
        alignment = metrics.get("alignment", 0.0)
        performance = metrics.get("performance", 0.0)
        novelty = metrics.get("novelty", 0.0)
        efficiency = metrics.get("efficiency", 0.0)

        score = (
            self.goal_weights["alignment"] * alignment +
            self.goal_weights["performance"] * performance +
            self.goal_weights["novelty"] * novelty +
            self.goal_weights["efficiency"] * efficiency
        )
        return round(score, 4)