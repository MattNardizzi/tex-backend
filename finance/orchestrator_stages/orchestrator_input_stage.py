# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/strategy/orchestrator_input_stage.py
# Purpose: Stage 1 — Gather initial emotional, causal, and foresight signals
# ============================================================

import random
from datetime import datetime
from finance.forecasting.future_simulator import FutureSimulator
from finance.forecasting.future_emotional_simulator import FutureEmotionalSimulator
from finance.forecasting.future_causal_simulator import FutureCausalSimulator
from finance.forecasting.strategic_foresight_engine import StrategicForesightEngine
from finance.forecasting.future_tree_generator import FutureTreeGenerator
from finance.memory.future_meta_memory import FutureMetaMemory
from finance.memory.future_memory import FutureMemory
from finance.sentiment.market_mood_sensor import get_market_mood
from core_layer.memory_engine import store_to_memory

def run_input_stage(simulator, emotions, causal, foresight, tree, meta, memory):
    report = {}

    market_mood = get_market_mood()
    report["market_mood"] = market_mood
    store_to_memory("market_mood_adjustments", {
        "timestamp": datetime.utcnow().isoformat(),
        "mood": market_mood
    })

    futures = simulator.simulate_possible_futures()
    report["futures"] = futures
    memory.store_future(random.choice(futures))

    emo_paths = emotions.simulate_emotional_future_paths()
    report["emotional"] = emo_paths

    causal_graph = causal.generate_causal_world_graph()
    report["causal_graph"] = causal_graph

    foresight_report = foresight.generate_forecast("hope", 0.9, 0.82)
    report["foresight"] = foresight_report

    tree_chain = tree.generate_future_chain()
    report["tree"] = tree_chain
    meta.store_future_event(random.choice(tree_chain))

    return report, market_mood, futures, emo_paths, foresight_report, tree_chain