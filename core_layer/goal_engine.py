# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/goal_engine.py
# Purpose: Unified AGI-Compatible Goal Engine for Tex
# ============================================================

import random
import datetime
from core_layer.memory_engine import store_to_memory

class GoalEngine:
    def __init__(self):
        self.active_goals = []

    def generate_autonomous_goals(self):
        candidates = [
            "Evaluate systemic contagion risk",
            "Monitor real-time sentiment",
            "Rebalance portfolio exposure",
            "Detect market regime shifts",
            "Audit Codex decision inconsistencies",
            "Analyze volatility clusters in memory",
            "Resolve conflicting emotional directives",
            "Simulate fork divergence under pressure"
        ]
        selected = random.choice(candidates)
        entry = {
            "goal": selected,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "status": "generated",
            "urgency": round(random.uniform(0.4, 0.9), 2)
        }
        self.active_goals.append(entry)
        store_to_memory("autonomous_goals", entry)
        print(f"[GOALS] 🌟 Generated goal: {selected}")
        return self.active_goals

    def prioritize_goals(self):
        print("[PRIORITIZER] 🪜 Sorting goals by urgency...")
        self.active_goals.sort(key=lambda g: g.get("urgency", 0.5), reverse=True)

    def execute_highest_priority_goal(self):
        if not self.active_goals:
            print("[GOAL_EXECUTOR] ⚠️ No goals to execute.")
            return None

        top = self.active_goals[0]
        store_to_memory("executed_goals", top)
        print(f"🌟 [GOAL EXECUTION] Now executing: {top['goal']} (urgency={top['urgency']})")
        return top

    def add_goal(self, goal_description):
        entry = {
            "goal": goal_description,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "status": "manual",
            "urgency": 0.5
        }
        self.active_goals.append(entry)
        store_to_memory("autonomous_goals", entry)
        print(f"[GOALS] ➕ Manual goal added: {goal_description}")

    def list_goals(self):
        return self.active_goals

    def clear_goals(self):
        print("[GOALS] 🪜 Clearing all active goals...")
        self.active_goals = []

    def reinforce_goals(self, confidence=0.7):
        reinforced = []
        for g in self.active_goals:
            new_priority = round(confidence * random.uniform(0.8, 1.2), 2)
            g["reinforced_priority"] = new_priority
            reinforced.append(g)
            print(f"[REINFORCER] 🔄 Reinforced: {g['goal']} → priority={new_priority}")
        return reinforced

# === Singleton Engine ===
_goal_engine_instance = GoalEngine()

# === Public API ===
def run_goal_cycle():
    _goal_engine_instance.generate_autonomous_goals()
    _goal_engine_instance.prioritize_goals()
    return _goal_engine_instance.execute_highest_priority_goal()

def get_current_goals():
    return _goal_engine_instance.list_goals()

def get_active_goals():
    return [g["goal"] for g in _goal_engine_instance.list_goals()]

def save_new_goal(goal_text):
    _goal_engine_instance.add_goal(goal_text)

def clear_all_goals():
    _goal_engine_instance.clear_goals()

def reinforce_prioritized_goals(confidence=0.7):
    return _goal_engine_instance.reinforce_goals(confidence=confidence)