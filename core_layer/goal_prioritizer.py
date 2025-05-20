# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: core_layer/goal_prioritizer.py
# Purpose: Filter, score, and prioritize Tex's goals by urgency and context
# ============================================================

import os
import json
from datetime import datetime, timezone
from core_layer.goal_filter import filter_goals  # 🔌 Import the smart filter

GOAL_FILE = "memory_archive/autonomous_goals.jsonl"
PRIORITIZED_FILE = "memory_archive/prioritized_goals.jsonl"

KEYWORD_WEIGHTS = {
    "crash": 0.9, "panic": 0.8, "sell": 0.7, "surge": 0.6,
    "inflation": 0.5, "volatility": 0.4, "buy now": 0.6,
    "default": 0.8, "bank run": 0.95, "collapse": 0.85,
    "opportunity": 0.3
}

def score_goal(goal):
    base_score = 0.3
    text = goal.get("goal", "").lower()

    for keyword, weight in KEYWORD_WEIGHTS.items():
        if keyword in text:
            base_score += weight

    # Boost from origin
    origin = goal.get("origin", "").lower()
    if origin in ["marketfeed", "rss", "newsapi"]:
        base_score += 0.2

    # Time-aware urgency boost
    try:
        timestamp_str = goal.get("timestamp", "")
        if timestamp_str:
            ts = datetime.fromisoformat(timestamp_str)
            if ts.tzinfo is None:
                ts = ts.replace(tzinfo=timezone.utc)
            now_utc = datetime.now(timezone.utc)
            delta_minutes = (now_utc - ts).total_seconds() / 60.0
            if delta_minutes < 10:
                base_score += 0.15
            elif delta_minutes < 30:
                base_score += 0.1
    except Exception as e:
        print(f"[PRIORITIZER WARNING] Timestamp parse failed: {e}")

    return round(min(base_score, 1.0), 3)

def prioritize_goals():
    print("[PRIORITIZER] 🧹 Running goal filter and prioritization...")
    filtered_goals = filter_goals()

    if not filtered_goals:
        print("[PRIORITIZER] ⚠️ No valid goals to prioritize.")
        return

    for goal in filtered_goals:
        goal["urgency_score"] = score_goal(goal)

    prioritized = sorted(filtered_goals, key=lambda x: x.get("urgency_score", 0), reverse=True)

    os.makedirs(os.path.dirname(PRIORITIZED_FILE), exist_ok=True)
    with open(PRIORITIZED_FILE, "w") as f:
        for goal in prioritized:
            f.write(json.dumps(goal) + "\n")

    print(f"[PRIORITIZER] ✅ Prioritized {len(prioritized)} filtered goals.")

if __name__ == "__main__":
    prioritize_goals()