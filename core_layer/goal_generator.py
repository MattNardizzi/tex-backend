# ===========================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/goal_generator.py
# Purpose: Autonomous emotional+reasoning-driven goal generation (VORTEX PRIME MODE)
# ===========================================================

import os
import json
from datetime import datetime
import random
import torch
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient

# === Config ===
QDRANT_COLLECTION = "tex_reasoning_memory"
GOAL_OUTPUT = "memory_archive/autonomous_goals.jsonl"
MEMORY_LOG = "memory_archive/evaluation_history.json"
GOAL_SEED_SOURCE = "InternalMemory"

# === Live Systems
embedder = SentenceTransformer("all-MiniLM-L6-v2")
client = QdrantClient(host="localhost", port=6333)

# === Static Trigger Themes (Still Active but Optional)
STATIC_TRIGGERS = {
    "crash": "Reinforce crash-resistance strategy",
    "panic": "Stabilize sentiment and reduce volatility",
    "bullish": "Expand into momentum sectors",
    "inflation": "Rebalance fixed income exposure",
    "interest rates": "Hedge against rate shock scenarios"
}

# === Helper: Calculate Urgency from Emotion/Context
def assign_urgency(goal_text, source, emotion="neutral", urgency_raw=0.5):
    base = urgency_raw
    if "panic" in goal_text.lower() or "crash" in goal_text.lower():
        base += 0.3
    if emotion in ["fear", "anger"]:
        base += 0.2
    if emotion == "joy":
        base -= 0.1
    if source == "InternalMemory":
        base += 0.05
    return round(min(max(base, 0.0), 1.0), 2)

# === Query vector memory for top related reasoning
def query_vector_memory_for_goals(query_text="adaptive strategy", top_k=10):
    try:
        vector = embedder.encode(query_text, convert_to_tensor=True).cpu().numpy().tolist()
        results = client.search(collection_name=QDRANT_COLLECTION, query_vector=vector, limit=top_k)
        return results
    except Exception as e:
        print(f"[❌ VECTOR SEARCH ERROR] {e}")
        return []

# === Dynamic Goal Extraction from Reasoning Trace
def generate_goals_from_reasoning_traces():
    results = query_vector_memory_for_goals()
    goals = []

    for match in results:
        reasoning = match.payload.get("output", "").lower()
        timestamp = match.payload.get("timestamp", datetime.utcnow().isoformat())

        matched_static = False
        for trigger, goal_text in STATIC_TRIGGERS.items():
            if trigger in reasoning:
                urgency = assign_urgency(goal_text, "VectorMemory", "neutral", 0.7)
                goals.append({
                    "goal": goal_text,
                    "trigger": trigger,
                    "origin": timestamp,
                    "urgency_score": urgency,
                    "reasoning_trace": reasoning[:300],
                    "timestamp": datetime.utcnow().isoformat()
                })
                matched_static = True
                break

        if not matched_static:
            # Dynamically create a goal based on emotional/strategic interpretation
            dynamic_goal = f"Investigate reasoning: '{reasoning[:80]}...'"
            urgency = assign_urgency(dynamic_goal, "InternalMemory", "curiosity", 0.5)
            goals.append({
                "goal": dynamic_goal,
                "trigger": "emergent",
                "origin": timestamp,
                "urgency_score": urgency,
                "reasoning_trace": reasoning[:300],
                "timestamp": datetime.utcnow().isoformat()
            })

    return goals

# === Memory-Based Backup Goal Seeding (Evaluation History)
def generate_goals_from_memory_seeds():
    if not os.path.exists(MEMORY_LOG):
        return []

    with open(MEMORY_LOG, "r") as f:
        try:
            memory = json.load(f)
        except json.JSONDecodeError:
            return []

    goals = []
    for item in memory:
        if item.get("type") == "goal_seed":
            urgency = assign_urgency(item.get("goal", "Exploratory expansion"), "ExternalSeed", "neutral", 0.6)
            goals.append({
                "goal": item.get("goal", "Exploratory expansion"),
                "origin": item.get("source", GOAL_SEED_SOURCE),
                "urgency_score": urgency,
                "reasoning_trace": item.get("headline", "N/A")[:300],
                "timestamp": item.get("timestamp", datetime.utcnow().isoformat())
            })

    return goals

# === Main Goal Generator
# === Main Goal Generator
def generate_autonomous_goals():
    print("[🧠] Generating autonomous goals...")
    vector_goals = generate_goals_from_reasoning_traces()
    seed_goals = generate_goals_from_memory_seeds()

    combined = vector_goals + seed_goals
    if not combined:
        print("[🟡] No goals generated this cycle. Cognitive exploration only.")
        return

    # ✅ Deduplicate based on the goal string
    seen = set()
    unique_goals = []
    for goal in combined:
        key = goal["goal"]
        if key not in seen and "cycle" not in key.lower():  # Filters spammy cycle reasoning
            unique_goals.append(goal)
            seen.add(key)

    # ✅ Sort and store
    prioritized = sorted(unique_goals, key=lambda g: g["urgency_score"], reverse=True)
    os.makedirs("memory_archive", exist_ok=True)

    with open(GOAL_OUTPUT, "a") as f:
        for g in prioritized:
            f.write(json.dumps(g) + "\n")

    print(f"[🎯] Generated {len(prioritized)} autonomous goal(s):")
    for g in prioritized:
        print(f"  → {g['goal']} (Urgency: {g['urgency_score']})")

# === Execute Standalone
if __name__ == "__main__":
    generate_autonomous_goals()

    try:
        from core_layer.goal_prioritizer import prioritize_goals
        prioritize_goals()
    except Exception as e:
        print(f"[ERROR] Failed to prioritize goals: {e}")