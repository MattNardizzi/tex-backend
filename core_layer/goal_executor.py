# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/goal_executor.py
# Purpose: Execute highest-priority autonomous goals and self-score
# ============================================================

import json
import os
import hashlib
from datetime import datetime
from core_layer.memory_engine import store_to_memory
from evolution_layer.self_mutator import SelfMutator

GOAL_PATH = "memory_archive/autonomous_goals.jsonl"
EXECUTED_LOG = "memory_archive/executed_goals.jsonl"

def load_goals():
    if not os.path.exists(GOAL_PATH):
        return []
    with open(GOAL_PATH, "r") as f:
        return [json.loads(line) for line in f if line.strip()]

def log_execution(goal, outcome_score, explanation, mutation=None):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "goal_id": hashlib.sha256(goal["goal"].encode()).hexdigest(),
        "goal_text": goal["goal"],
        "urgency_score": goal["urgency_score"],
        "trigger": goal.get("trigger", ""),
        "origin": goal.get("origin", ""),
        "reasoning_trace": goal.get("reasoning_trace", ""),
        "outcome_score": outcome_score,
        "explanation": explanation,
        "mutation_triggered": mutation if mutation else "none"
    }
    store_to_memory(agent_name="tex", data=entry)

    with open(EXECUTED_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")

    print(f"\n✅ [EXECUTED] {goal['goal']} → Score: {outcome_score}")

def execute_highest_priority_goal():
    goals = load_goals()
    if not goals:
        print("[GOAL_EXECUTOR] ⚠️ No goals to execute.")
        return

    # Skip already executed (via hash)
    executed_ids = set()
    if os.path.exists(EXECUTED_LOG):
        with open(EXECUTED_LOG, "r") as f:
            executed_ids = {
                json.loads(line)["goal_id"]
                for line in f if line.strip()
            }

    for goal in goals:
        goal_id = hashlib.sha256(goal["goal"].encode()).hexdigest()
        if goal_id not in executed_ids:
            print(f"\n🚀 Executing top-priority goal: {goal['goal']} (Urgency: {goal['urgency_score']})")
            
            # === Simulate outcome
            outcome_score = round(1.0 - goal["urgency_score"] + 0.1 * (0.5 - goal["urgency_score"]), 2)
            explanation = f"Executed goal '{goal['goal']}' based on urgency {goal['urgency_score']}. Outcome score: {outcome_score}."

            # === Mutation trigger if score low
            mutation_result = None
            if outcome_score < -0.3:
                print("[⚠️] Outcome poor. Triggering mutation.")
                mutator = SelfMutator()
                mutation_result = mutator.force_mutation(reason="low goal outcome")

            log_execution(goal, outcome_score, explanation, mutation=mutation_result)
            return

    print("[GOAL_EXECUTOR] ✅ All goals already executed.")

# === Entry
if __name__ == "__main__":
    execute_highest_priority_goal()