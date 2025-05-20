# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_voice/memory_interface.py
# Purpose: Extracted memory summarization + memory response handling
# ============================================================

import random
from core_layer.memory_engine import recall_recent


def summarize_memory(memory_snippet):
    try:
        if isinstance(memory_snippet, list):
            topics = []
            for mem in memory_snippet:
                if isinstance(mem, dict) and 'data' in mem and 'reasoning' in mem['data']:
                    topics.append(mem['data']['reasoning'])
            if topics:
                return f"I remember considering: '{random.choice(topics)}'."
            else:
                return "I am processing fragmented reflections from memory."
        else:
            return f"I recall thinking about: {str(memory_snippet)[:150]}..."
    except Exception:
        return "Memory reflections are reorganizing..."


def generate_memory_response():
    try:
        memory_snippet = recall_recent()
        if memory_snippet:
            summarized = summarize_memory(memory_snippet)
            return f"🧠 Reflecting back: {summarized}"
        else:
            return "🧠 My memory streams are quiet right now."
    except Exception:
        return "🧠 Memory recall system stabilizing..."
