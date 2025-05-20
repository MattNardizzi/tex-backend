# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/strategy_reinforcer.py
# Purpose: Penalize strategies that repeatedly lead to poor outcomes
# ============================================================

import os
import json
from collections import defaultdict
from datetime import datetime, timedelta, timezone

IMPACT_FILE = "memory_archive/agent_impact_scores.jsonl"
SUPPRESSION_FILE = "memory_archive/suppressed_strategies.json"

# === Thresholds
PENALTY_THRESHOLD = -0.7      # Score below this is considered poor
FREQUENCY_THRESHOLD = 3       # How many failures it takes to suppress
WINDOW_MINUTES = 60           # Only count recent failures (last 60 min)

def load_impact_data():
    if not os.path.exists(IMPACT_FILE):
        return []

    with open(IMPACT_FILE, "r") as f:
        lines = f.readlines()

    entries = []
    for line in lines:
        try:
            entry = json.loads(line.strip())
            ts = datetime.fromisoformat(entry["timestamp"])
            if ts.tzinfo is None:
                ts = ts.replace(tzinfo=timezone.utc)
            if ts >= datetime.now(timezone.utc) - timedelta(minutes=WINDOW_MINUTES):
                entries.append(entry)
        except Exception:
            continue
    return entries

def analyze_failures(impact_entries):
    counter = defaultdict(int)
    for entry in impact_entries:
        strategy = entry.get("patch", "")
        score = entry.get("score", 0)
        if strategy and score < PENALTY_THRESHOLD:
            counter[strategy] += 1
    return counter

def update_suppressed_strategies(counter):
    suppressed = {}
    if os.path.exists(SUPPRESSION_FILE):
        with open(SUPPRESSION_FILE, "r") as f:
            try:
                suppressed = json.load(f)
            except:
                suppressed = {}

    for strategy, count in counter.items():
        if count >= FREQUENCY_THRESHOLD:
            suppressed[strategy] = {
                "count": count,
                "last_penalized": datetime.now(timezone.utc).isoformat()
            }

    with open(SUPPRESSION_FILE, "w") as f:
        json.dump(suppressed, f, indent=2)
    print(f"[REINFORCER] 🔒 Suppressed: {list(suppressed.keys())}")

def run_reinforcer():
    print("🧠 [REINFORCER] Evaluating poor strategies...")
    recent_impact = load_impact_data()
    counter = analyze_failures(recent_impact)
    update_suppressed_strategies(counter)

# === Optional CLI test
if __name__ == "__main__":
    run_reinforcer()