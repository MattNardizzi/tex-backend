# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/codex_mutation_logger.py
# Purpose: Logs Codex mutations and the cognitive/emotional conditions that triggered them
# ============================================================
print(f"[DEBUG] Logging to: {{MUTATION_LOG_PATH}}")  # <-- this is incorrectimport os
import os
import json
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MUTATION_LOG_PATH = os.path.join(BASE_DIR, "..", "memory_archive", "codex_mutation_log.jsonl")
MUTATION_LOG_PATH = os.path.normpath(MUTATION_LOG_PATH)
def log_codex_mutation(cycle, original, mutated, trigger):
    """
    Logs a Codex mutation event.

    Args:
        cycle (int): Tex's current cognitive cycle.
        original (str): The original code, rule, or logic block.
        mutated (str): The updated/mutated version.
        trigger (dict): Conditions that led to the mutation (emotion, coherence, urgency, etc.)
    """
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "cycle": cycle,
        "original": original,
        "mutated": mutated,
        "trigger": trigger
    }

    try:
        os.makedirs(os.path.dirname(MUTATION_LOG_PATH), exist_ok=True)
        with open(MUTATION_LOG_PATH, "a") as f:
            f.write(json.dumps(event) + "\n")
        print(f"[CODEX MUTATION LOG] 📜 Logged mutation event at cycle {cycle}")
    except Exception as e:
        print(f"[CODEX MUTATION LOGGER ERROR] {e}")
