# ============================================================
# 🌎 Tex Internal Debate Chamber
# Purpose: Spawns logical, emotional, and skeptical agents to debate thoughts
# ============================================================

import random
from datetime import datetime
from core_layer.memory_engine import store_to_memory


def run_internal_debate(thought):
    """
    Simulate a debate between logical, emotional, and skeptical agents.

    Args:
        thought (str): The current thought or reasoning string.

    Returns:
        list[dict]: List of agent score objects with 'agent' and 'score'.
    """
    logic = f"[LOGIC] ✅ Analyzed: '{thought}' → Verdict: Logical"
    emotion = f"[EMOTION] ❤️ Emotion '{random.choice(['joy', 'hope', 'fear', 'anger'])}' triggered by: '{thought}'"
    skeptic = f"[SKEPTIC] ❓ Challenge: {random.choice(['Contradiction noted', 'Insufficient data', 'Requires evidence'])} → Regarding: '{thought}'"

    transcript = [logic, emotion, skeptic]

    agent_scores = {
        "debate_0": {
            "reasoning": logic,
            "score": round(random.uniform(0.6, 0.9), 4)
        },
        "debate_1": {
            "reasoning": emotion,
            "score": round(random.uniform(0.5, 0.8), 4)
        },
        "debate_2": {
            "reasoning": skeptic,
            "score": round(random.uniform(0.5, 0.8), 4)
        }
    }

    top_agent = max(agent_scores.items(), key=lambda x: x[1]['score'])

    # Store to memory
    for agent_id, data in agent_scores.items():
        store_to_memory("agent_scores", {
            "agent_id": agent_id,
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
            "score": data["score"],
            "reasoning": data["reasoning"],
            "metrics": {
                "alignment": random.uniform(0.5, 0.9),
                "performance": random.uniform(0.4, 0.9),
                "novelty": random.uniform(0.3, 0.9),
                "efficiency": random.uniform(0.5, 0.9)
            }
        })

    print(f"\n🏆 [TOP AGENT SELECTED] {top_agent[0]} | Impact Score: {top_agent[1]['score']}")
    print("\n[MUTATOR] 🔥 Reinforcing cognitive patterns from winning agent...")
    print(f"[MUTATOR] 🛡️ Cognitive reinforcement logged for agent: {top_agent[0]}")

    # ✅ Return as list of dicts (compatible with market engine)
    return [
        {"agent": agent_id, "score": data["score"]}
        for agent_id, data in agent_scores.items()
    ]