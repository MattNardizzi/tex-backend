# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/meta_goal_fuser.py
# Purpose: Fuse related goals into higher-level meta-goals to reduce redundancy
# ============================================================

import json
import os
from datetime import datetime
from core_layer.memory_engine import store_to_memory

GOAL_FILE = "memory_archive/prioritized_goals.jsonl"
FUSED_LOG = "memory_archive/meta_goal_fusions.jsonl"
os.makedirs("memory_archive", exist_ok=True)

def fuse_goals():
    goal_texts = []
    if not os.path.exists(GOAL_FILE):
        return []

    with open(GOAL_FILE, "r") as f:
        for line in f:
            try:
                data = json.loads(line.strip())
                goal = data.get("goal", "").lower()
                if goal:
                    goal_texts.append(goal)
            except:
                continue

    fused_goals = []
    seen = set()
    for goal in goal_texts:
        if any(keyword in goal for keyword in ["reduce risk", "manage volatility", "hedge"]):
            fused_goal = "Construct meta-goal: Reduce systemic risk via multi-layer hedging"
        elif any(keyword in goal for keyword in ["maximize return", "boost alpha", "optimize gain"]):
            fused_goal = "Construct meta-goal: Optimize return efficiency across strategies"
        else:
            fused_goal = None

        if fused_goal and fused_goal not in seen:
            seen.add(fused_goal)
            fused_goals.append(fused_goal)
            with open(FUSED_LOG, "a") as log:
                log.write(json.dumps({
                    "timestamp": datetime.utcnow().isoformat(),
                    "fused_goal": fused_goal
                }) + "\n")

            store_to_memory("AEI", {
                "event": "MetaGoalFused",
                "meta_goal": fused_goal,
                "timestamp": datetime.utcnow().isoformat()
            })

    return fused_goals