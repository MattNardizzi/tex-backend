# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/causal_thought_logger.py
# Purpose: Log full thought → decision → outcome → emotion cycles
# ============================================================

import json
from datetime import datetime
from core_layer.memory_engine import store_to_memory

def log_causal_trace(cycle_id, thought, decision=None, outcome=None, emotion="neutral"):
    trace = {
        "timestamp": datetime.utcnow().isoformat(),
        "cycle": cycle_id,
        "thought": thought,
        "decision": decision,
        "outcome": outcome,
        "emotion": emotion
    }
    print(f"[🧠 CAUSAL TRACE] Logged: {trace}")
    store_to_memory("causal_trace", trace)