# ===========================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: agentic_ai/reasoning_trace.py
# Purpose: Logs and stores every reasoning step for transparency, audit, and LLM detachment
# ===========================================================

import json
import os
from datetime import datetime

REASONING_LOG = "memory_archive/reasoning_trace_log.jsonl"

def log_reasoning_step(source, input_text, output_text, confidence=0.85, agent="TexCore"):
    """Logs each decision or reasoning trace to persistent memory."""
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "source": source,
        "input": input_text,
        "output": output_text,
        "confidence": confidence,
        "agent": agent
    }

    os.makedirs("memory_archive", exist_ok=True)
    with open(REASONING_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")

    print(f"[🧠] Reasoning logged by {agent}: {output_text[:80]}...")

def get_recent_traces(n=10):
    if not os.path.exists(REASONING_LOG):
        return []

    with open(REASONING_LOG, "r") as f:
        lines = f.readlines()[-n:]
        return [json.loads(line) for line in lines if line.strip()]

def trace_to_memory_vector(trace):
    """Simulated embedding vector for future use in local reasoning (LLM detachment prep)."""
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model.encode(trace["output"])

# === Example ===
if __name__ == "__main__":
    log_reasoning_step(
        source="tex_brain.py > decision loop",
        input_text="RSS headline: Federal Reserve signals another rate hike.",
        output_text="Reduce exposure to high-leverage positions.",
        confidence=0.92
    )
    recent = get_recent_traces()
    print(f"[📄] Last Reasoning: {recent[-1]['output']}")