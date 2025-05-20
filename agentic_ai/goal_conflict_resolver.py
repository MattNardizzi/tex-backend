# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# License: Private Intellectual Property – Not for distribution.
# ============================================================
# Goal Conflict Resolver – Handles AGI Contradictions
# ============================================================

import datetime

class GoalConflictResolver:
    def __init__(self):
        self.resolution_log = []

    def resolve(self, goal_1: dict, goal_2: dict):
        print(f"[GOAL CONFLICT] ⚠️ Evaluating conflict:")
        print(f"• Goal 1: {goal_1['goal']} | Urgency: {goal_1['urgency']}")
        print(f"• Goal 2: {goal_2['goal']} | Urgency: {goal_2['urgency']}")

        if goal_1['urgency'] > goal_2['urgency']:
            selected = goal_1
        elif goal_2['urgency'] > goal_1['urgency']:
            selected = goal_2
        else:
            selected = goal_1 if goal_1['goal'] < goal_2['goal'] else goal_2

        timestamp = datetime.datetime.now().isoformat()
        self.resolution_log.append({
            "timestamp": timestamp,
            "selected_goal": selected['goal'],
            "rejected_goal": goal_2['goal'] if selected == goal_1 else goal_1['goal']
        })

        print(f"[GOAL CONFLICT] ✅ Selected: {selected['goal']}")
        return selected
