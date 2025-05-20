# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/tex_explainer.py
# Purpose: Tex explains his decision logic after executing goals
# ============================================================

from core_layer.memory_engine import recall_latest

def explain_latest_decision():
    """
    Prints a reasoning trace of the most recent memory, strategy, and emotion state.
    """
    memory = recall_latest("tex")
    if not memory:
        print("❌ [EXPLAIN] No memory found for latest decision.")
        return

    data = memory.get("data", {})
    emotion = data.get("emotion", "unknown")
    urgency = data.get("urgency", "unknown")
    strategy = data.get("patch", {}).get("strategy", "none")
    score = data.get("score", "unknown")
    explanation = data.get("explanation", "No explanation found.")

    print(f"""
[🧠 TEX EXPLAINS]
→ Emotion: {emotion}
→ Urgency: {urgency}
→ Strategy Chosen: {strategy}
→ Outcome Score: {score}
→ Reason: {explanation}
""")