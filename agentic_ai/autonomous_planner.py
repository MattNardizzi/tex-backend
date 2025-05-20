# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# License: Private Intellectual Property – Not for distribution.
# ============================================================
# Autonomous Planner – Self-Directed Execution Sequencer
# ============================================================

import random
import datetime

class AutonomousPlanner:
    def __init__(self):
        self.task_history = []

    def generate_plan(self, goal: str, urgency: float):
        tasks = self._select_tasks(goal, urgency)
        timestamp = datetime.datetime.now().isoformat()
        print(f"[PLANNER] 🧭 Generated plan @ {timestamp}:")
        for task in tasks:
            print(f"• {task}")
        self.task_history.append({
            "goal": goal,
            "urgency": urgency,
            "tasks": tasks,
            "timestamp": timestamp
        })
        return tasks

    def _select_tasks(self, goal, urgency):
        templates = {
            "Monitor real-time sentiment": [
                "Parse latest RSS summaries",
                "Score sentiment by topic",
                "Log top volatility triggers"
            ],
            "Evaluate systemic contagion risk": [
                "Analyze correlation matrices",
                "Check bond-equity spread thresholds",
                "Flag synchronized asset declines"
            ],
            "Rebalance portfolio exposure": [
                "Run QAOA optimizer",
                "Generate updated weight vector",
                "Trigger simulated rebalance"
            ],
        }
        base_tasks = templates.get(goal, ["Log observation", "Simulate action path"])
        task_count = 2 if urgency < 0.5 else 3
        return random.sample(base_tasks, min(task_count, len(base_tasks)))
