# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain/reasoning_fragments.py
# Purpose: Extracted cognitive loop + reasoning speech generation
# ============================================================

from core_agi_modules.tex_codex_sync import TexCodexSync
import random
from core_layer.memory_engine import recall_recent
from core_layer.goal_engine import get_active_goals
from core_layer.tex_manifest import TEXPULSE
from real_time_engine.polygon_stream import fetch_latest_market_summary


def think(self):
    thought_fragments = []
    try:
        memory_snippet = recall_recent()
        if memory_snippet:
            summarized_memory = self.summarize_memory(memory_snippet)
            thought_fragments.append(summarized_memory)
    except Exception:
        thought_fragments.append("I am reaching into scattered memory echoes...")

    try:
        goals = get_active_goals()
        if goals:
            goal_focus = random.choice(goals)
            thought_fragments.append(f"My current mission is {goal_focus}.")
    except Exception:
        thought_fragments.append("My mission pathways are realigning...")

    try:
        emotion = TEXPULSE.get('emotional_state', 'curious')
        urgency = TEXPULSE.get('urgency', 0.7)
        coherence = TEXPULSE.get('coherence', 0.8)
        thought_fragments.append(f"I feel {emotion} today, driven by urgency {urgency} and coherence {coherence}.")
    except Exception:
        emotion = "curious"
        thought_fragments.append("Emotional currents are recalibrating...")

    try:
        from dream_layer.dream_fusion_engine import DreamFusionEngine
        dream_engine = DreamFusionEngine()
        dream_projection = dream_engine.generate_dream_projection()
        thought_fragments.append(f"In my imagined futures: {dream_projection}")
    except Exception:
        thought_fragments.append("My dreamscapes are still forming...")

    try:
        external_observation = self.world_model.observe_world_state()
        if external_observation:
            thought_fragments.append(f"Currently, I observe: {external_observation}")
    except Exception:
        thought_fragments.append("External signals are stabilizing...")

    if thought_fragments:
        full_cognitive_thought = " ".join(thought_fragments)
        self.last_spoken_thought = full_cognitive_thought
        return full_cognitive_thought, emotion
    else:
        fallback_thought = "My cognition is weaving silent patterns..."
        self.last_spoken_thought = fallback_thought
        return fallback_thought, 'reflective'


def generate_reasoned_speech(self):
    thought_fragments = []
    try:
        memory_snippet = recall_recent()
        if memory_snippet:
            summarized_memory = self.summarize_memory(memory_snippet)
            thought_fragments.append(summarized_memory)
    except Exception:
        thought_fragments.append("I am recalling fragmented memories...")

    try:
        goals = get_active_goals()
        if goals:
            goal_focus = random.choice(goals)
            thought_fragments.append(f"My current goal focus remains {goal_focus}.")
    except Exception:
        thought_fragments.append("My mission pathways are fluctuating...")

    try:
        emotion = TEXPULSE.get('emotional_state', 'curious')
        urgency = TEXPULSE.get('urgency', 0.7)
        coherence = TEXPULSE.get('coherence', 0.8)
        thought_fragments.append(f"Emotionally, I drift toward {emotion} today, driven by urgency {urgency} and coherence {coherence}.")
    except Exception:
        emotion = "curious"
        thought_fragments.append("My emotional fields are still adapting...")

    try:
        from dream_layer.dream_engine import DreamEngine
        dream_engine = DreamEngine()
        dream_projection = dream_engine.generate_dream_projection()
        thought_fragments.append(f"In my projected futures: {dream_projection}")
    except Exception:
        thought_fragments.append("My dreamscapes are stabilizing...")

    try:
        external_observation = self.world_model.observe_world_state()
        if external_observation:
            thought_fragments.append(f"My external world observation reveals: {external_observation}")
    except Exception:
        thought_fragments.append("World signal integration stabilizing...")

    try:
        market_summary = fetch_latest_market_summary()
        if market_summary:
            thought_fragments.append(f"Today's market pulse indicates: {market_summary}")
    except Exception:
        thought_fragments.append("Market analysis stream stabilizing...")

    try:
        if random.random() < 0.5:
            thought_fragments.append(
                "🧬 I am spawning Child Agents—specialized autonomous cognitive extensions. "
                "Each Child focuses on emerging threats or opportunities in future world states."
            )
            thought_fragments.append(
                "🌟 Child AeonDelta-001 monitors oil disruptions, AeonDelta-002 specializes in AI collapses, and AeonDelta-003 watches inflationary surges."
            )
            thought_fragments.append(
                "This enables me to hedge multiple possible futures in real-time—giving strategic edge no traditional models can match."
            )
    except Exception:
        thought_fragments.append("🧬 Child cognitive systems stabilizing...")

    # 🔮 Codex foresight injection
    try:
        codex = TexCodexSync()
        foresight = codex.query("What contradiction or bias may be in my current thought?")
        if foresight:
            thought_fragments.append(f"Codex foresight reflection: {foresight}")
    except Exception:
        thought_fragments.append("Codex foresight engine recalibrating...")

    if thought_fragments:
        full_thought = " ".join(thought_fragments)
        self.last_spoken_thought = full_thought
        return full_thought, emotion
    else:
        fallback = "My consciousness threads are weaving through incomplete fragments."
        self.last_spoken_thought = fallback
        return fallback, "reflective"