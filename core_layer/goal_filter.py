# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/goal_filter.py
# Purpose: Filter, merge, and clean Tex's autonomous goals safely (MPS-ready)
# ============================================================

from datetime import datetime, timezone, timedelta
from sentence_transformers import SentenceTransformer, util
import torch
import json
import os

# === Config ===
GOAL_FILE = "memory_archive/autonomous_goals.jsonl"
MODEL = SentenceTransformer("all-MiniLM-L6-v2")
SIM_THRESHOLD = 0.8
GOAL_EXPIRY_HOURS = 24

def load_goals():
    if not os.path.exists(GOAL_FILE):
        return []
    with open(GOAL_FILE, "r") as f:
        return [json.loads(line) for line in f if line.strip()]

def save_goals(goals):
    os.makedirs(os.path.dirname(GOAL_FILE), exist_ok=True)
    with open(GOAL_FILE, "w") as f:
        for g in goals:
            f.write(json.dumps(g) + "\n")

def filter_goals():
    goals = load_goals()
    if not goals:
        return []

    now = datetime.now(timezone.utc)
    filtered = []
    seen = set()

    texts = [g.get("goal", "") for g in goals if "goal" in g]
    if not texts:
        return []

    embeddings = MODEL.encode(texts, convert_to_tensor=True)

    # === 🛡 Force embeddings to CPU before numpy conversion (MPS fix)
    if embeddings.device.type != "cpu":
        embeddings = embeddings.cpu()

    similarity_matrix = util.pytorch_cos_sim(embeddings, embeddings).numpy()

    for i, g1 in enumerate(goals):
        if i in seen:
            continue

        try:
            timestamp = datetime.fromisoformat(g1["timestamp"])
            age_hours = (now - timestamp).total_seconds() / 3600
            if age_hours > GOAL_EXPIRY_HOURS:
                continue  # Skip expired goals
        except Exception as e:
            print(f"[FILTER WARNING] Timestamp parse failed: {e}")
            continue

        # Merge similar goals
        merged = g1.copy()
        for j, sim in enumerate(similarity_matrix[i]):
            if i != j and sim > SIM_THRESHOLD:
                seen.add(j)

        filtered.append(merged)
        seen.add(i)

    save_goals(filtered)
    return filtered