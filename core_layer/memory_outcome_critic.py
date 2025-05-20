# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: core_layer/memory_outcome_critic.py
# Purpose: Detect poor memory outcomes and penalize agent influence
# ============================================================

import os
import json
from datetime import datetime, timezone
from core_layer.memory_engine import recall_all, store_to_memory

SCORE_THRESHOLD = -0.5
TARGET_AGENT = "tex"
IMPACT_LOG = "memory_archive/agent_impact_scores.jsonl"

def penalize_bad_memories(agent=TARGET_AGENT):
    print(f"[CRITIC] 🧠 Scanning {agent} memory for poor performance...")
    entries = recall_all(agent)
    flagged = [e for e in entries if e["data"].get("score", 0) < SCORE_THRESHOLD]

    if not flagged:
        print("[CRITIC] ✅ No penalizable memories found.")
        return

    with open(IMPACT_LOG, "a") as f:
        for entry in flagged:
            impact = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "agent": entry["agent"],
                "cycle": entry["data"].get("cycle"),
                "score": entry["data"].get("score"),
                "explanation": entry["data"].get("explanation", ""),
                "patch": entry["data"].get("patch", {}).get("strategy", "none"),
                "action": "penalize_strategy"
            }
            f.write(json.dumps(impact) + "\n")
            print(f"[CRITIC] ⚠️ Penalized strategy: {impact['patch']} | Score: {impact['score']}")

if __name__ == "__main__":
    penalize_bad_memories()