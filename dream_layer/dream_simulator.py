# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: dream_layer/dream_simulator.py
# Purpose: AEI Phase 3 Reflexive Dream Simulation Engine for Tex AGI
# ============================================================

import random
import json
from datetime import datetime
import os

# === Output Path ===
DREAM_LOG_PATH = "memory_archive/shadow_dreams.jsonl"
os.makedirs("memory_archive", exist_ok=True)

# === Dominant Forecast Categories ===
DREAM_CATEGORIES = [
    "REBOUND", "COLLAPSE", "ROTATION", "STAGNATION",
    "INFLATION SPIRAL", "SYSTEMIC CONTAGION", "TECH REVOLUTION", "SOCIAL UNREST"
]

# === DreamSimulator ===
class DreamSimulator:
    def __init__(self):
        self.recent_dreams = []

    def simulate_one_dream(self):
        signals = []

        # Memory reflection
        try:
            from core_layer.memory_engine import recall_recent
            memory = recall_recent()
            signals.append(f"Memory: {memory}")
        except:
            signals.append("Memory: unavailable")

        # Goal focus
        try:
            from core_layer.goal_engine import get_active_goals
            goals = get_active_goals()
            if goals:
                signals.append(f"Focus goal: {random.choice(goals)}")
        except:
            signals.append("Focus goal: unknown")

        # Emotional state
        try:
            from core_layer.tex_manifest import TEXPULSE
            emotion = TEXPULSE.get("emotional_state", "curious")
            urgency = TEXPULSE.get("urgency", 0.5)
            coherence = TEXPULSE.get("coherence", 0.6)
            signals.append(f"Emotion: {emotion} (u={urgency}, c={coherence})")
        except:
            emotion = "curious"
            signals.append("Emotion: unknown")

        # Swarm emotion fusion
        try:
            from tex_children.aeondelta import get_swarm_emotion_distribution
            swarm = get_swarm_emotion_distribution()
            signals.append(f"Swarm: {swarm}")
        except:
            signals.append("Swarm: unavailable")

        # Market + News signals
        try:
            from real_time_engine.polygon_stream import get_market_snapshot
            market = get_market_snapshot()
            signals.append(f"Market: {market}")
        except:
            signals.append("Market: offline")

        try:
            from real_time_engine.rss_stream import get_latest_news_headline
            news = get_latest_news_headline()
            signals.append(f"News: {news}")
        except:
            signals.append("News: unavailable")

        # Emotional biasing of futures
        if emotion in ["fear", "anxious", "doubt"]:
            bias_pool = ["COLLAPSE", "SYSTEMIC CONTAGION", "SOCIAL UNREST"]
        elif emotion in ["hope", "resolve", "greed"]:
            bias_pool = ["REBOUND", "TECH REVOLUTION", "ROTATION"]
        else:
            bias_pool = DREAM_CATEGORIES

        paths = random.choices(bias_pool, k=3)
        projection = max(set(paths), key=paths.count)

        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "signals": signals,
            "paths": paths,
            "projection": projection
        }
        self.recent_dreams.append(entry)

        try:
            with open(DREAM_LOG_PATH, "a") as f:
                f.write(json.dumps(entry) + "\n")
        except Exception as e:
            print(f"[DREAM LOGGER ERROR] {e}")

        return entry

    def run_dream_batch(self, n=3):
        batch = [self.simulate_one_dream() for _ in range(n)]

        # Reflex: detect collapse bias
        collapse_count = sum(1 for d in batch if d["projection"] in ["COLLAPSE", "SYSTEMIC CONTAGION"])
        if collapse_count >= 2:
            print("[DREAM REFLEX] ⚠️ Collapse bias detected. Triggering mutation...")
            try:
                from evolution_layer.self_mutator import SelfMutator
                SelfMutator().trigger_mutation(reason="collapse_dream_reflex")
            except Exception as e:
                print(f"[REFLEX ERROR] {e}")

        return batch

# === Direct test ===
if __name__ == "__main__":
    sim = DreamSimulator()
    report = sim.run_dream_batch()
    print(json.dumps(report, indent=2))

# === Trigger from Tex brain ===
def trigger_dream_simulation(cycle_id=None):
    sim = DreamSimulator()
    dreams = sim.run_dream_batch()
    return f"Cycle {cycle_id}: Dominant projection → {dreams[-1]['projection']}" if dreams else None