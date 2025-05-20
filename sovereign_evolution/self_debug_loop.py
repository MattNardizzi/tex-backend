# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/self_debug_loop.py
# Purpose: Tex scans his own past thoughts and decisions for contradictions
# ============================================================

import os
import json
from datetime import datetime
from evolution_layer.self_mutator import trigger_mutation

THOUGHT_HISTORY_PATH = "memory_archive/causal_trace.jsonl"

class SelfDebugLoop:
    def __init__(self, regret_trigger_threshold=0.6):
        self.regret_trigger_threshold = regret_trigger_threshold

    def scan_for_contradictions(self):
        """
        Looks for obvious contradictions in recent causal trace.
        If contradictions exceed threshold, a mutation is triggered.
        """
        if not os.path.exists(THOUGHT_HISTORY_PATH):
            print("[SELF-DEBUG] No causal trace found.")
            return

        try:
            with open(THOUGHT_HISTORY_PATH, "r") as f:
                lines = [json.loads(l) for l in f if l.strip()]
        except Exception as e:
            print(f"[SELF-DEBUG ERROR] Failed to parse trace: {e}")
            return

        contradictions = [line for line in lines if line.get("decision") == "contradiction"]
        print(f"[SELF-DEBUG] Found {len(contradictions)} contradictions in memory.")

        if len(contradictions) >= 3:
            print(f"[SELF-DEBUG] ❌ Threshold exceeded. Initiating mutation...")
            trigger_mutation(reason="contradiction accumulation in trace")

        return contradictions