# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/reflection_loop.py
# Purpose: Tex Reflection Loop — Pure Procedural Internal Debate and Agent Scoring
# ============================================================

import random

from agentic_ai.multi_voice_reasoning import run_internal_debate
from agentic_ai.agent_scorer import AgentScorer
from agentic_ai.vectorize_reasoning import store_reasoning
from evolution_layer.self_mutator import SelfMutator

mutator = SelfMutator()
scorer = AgentScorer()

def run_reflection_cycle(count, emotion, urgency, coherence):
    print("\n🎧 [INTERNAL DEBATE]")
    debate_outputs = run_internal_debate(f"Cycle {count} reasoning state")
    for output in debate_outputs:
        print(f"🗣️ {output}")

    debate_agents = [{"id": f"debate_{i}", "reasoning": d, "metrics": {
        "alignment": random.uniform(0.5, 1.0),
        "performance": random.uniform(0.4, 1.0),
        "novelty": random.uniform(0.3, 1.0),
        "efficiency": random.uniform(0.5, 1.0)
    }} for i, d in enumerate(debate_outputs)]

    ranked_agents = scorer.score_agents(debate_agents)
    if ranked_agents:
        top_agent = ranked_agents[0]
        print(f"\n🏆 [TOP AGENT SELECTED] {top_agent[0]} | Impact Score: {top_agent[1]}")
        mutator.reinforce_with_agent(top_agent[2])

        try:
            reasoning_text = top_agent[2]["reasoning"]
            store_reasoning(reasoning_text)
        except Exception as e:
            print(f"[❌ VECTOR STORAGE ERROR] {e}")

        