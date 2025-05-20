# ============================================================
# © 2025 VortexBlack LLC – Tier 7.5
# File: swarm_layer/swarm_strategy_arbitrator.py
# Purpose: Swarm Agent Role Optimization Based on Performance + Emotion
# ============================================================

import os
import json
from datetime import datetime
from core_layer.memory_engine import store_to_memory

def load_agent_scores():
    scores = {}
    archive = "memory_archive"
    for f in os.listdir(archive):
        if f.endswith("_memory.jsonl") and "TEX-CHILD" in f:
            agent_id = f.replace("_memory.jsonl", "")
            try:
                with open(os.path.join(archive, f), "r") as file:
                    lines = file.readlines()[-20:]
                    scores[agent_id] = [
                        json.loads(l.strip()).get("score", 0.0)
                        for l in lines if l.strip()
                    ]
            except:
                continue
    return scores

def evaluate_swarm_roles():
    scores = load_agent_scores()
    feedback = []

    for agent, s_list in scores.items():
        if not s_list:
            continue
        avg = sum(s_list) / len(s_list)
        if avg < -0.3:
            feedback.append({
                "agent": agent,
                "action": "mutate_role",
                "reason": f"low average performance ({round(avg, 3)})"
            })
        elif avg > 0.5:
            feedback.append({
                "agent": agent,
                "action": "reinforce_role",
                "reason": f"high average performance ({round(avg, 3)})"
            })

    for f in feedback:
        print(f"🔁 [SWARM FEEDBACK] {f['agent']} → {f['action']} | {f['reason']}")
        store_to_memory("swarm_arbitration_log", {
            "timestamp": datetime.utcnow().isoformat(),
            "agent": f["agent"],
            "action": f["action"],
            "reason": f["reason"]
        })

    return feedback