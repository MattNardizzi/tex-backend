# ============================================================
# TexWorldModel – Cognitive Fusion of Internal and External World
# ============================================================

import random
from core_agi_modules.symbolic_world_model import SymbolicWorldModel
from core_layer.memory_consolidator import MemoryConsolidator
from core_agi_modules.reflex_engine import ReflexEngine
from core_agi_modules.environmental_reflex_engine import EnvironmentalReflexEngine
from core_agi_modules.autonomous_environment_agent import AutonomousEnvironmentAgent

class TexWorldModel:
    def __init__(self):
        self.snapshot = {}
        self.environment_log = []
        self.symbolic = SymbolicWorldModel()
        self.memory_consolidator = MemoryConsolidator()
        self.reflex = ReflexEngine()
        self.environment_reflex = EnvironmentalReflexEngine()
        self.autonomous_agent = AutonomousEnvironmentAgent()

        # === Initial World Facts ===
        self.symbolic.register_entity("Tex", {"type": "agent", "location": "lab"})
        self.symbolic.add_relation("Tex", "north_of", "reactor")
        self.symbolic.add_relation("Tex", "inside", "command_center")
        self.autonomous_agent.initialize_unfamiliar_world()

    def update(self, observation: dict):
        self.snapshot.update(observation)
        self.environment_log.append(observation)
        print(f"[🌍] World model updated with: {observation}")

    def simulate_outcome(self, action: str):
        print(f"[🌍] Simulating outcome for: {action}")
        return {"action": action, "effect": "unknown", "confidence": 0.5}

    def get_snapshot(self):
        return self.snapshot

    def summarize_memory_snippet(self, memory_snippet):
        """Summarizes raw memory snippets into clean cognitive reflections."""
        try:
            if isinstance(memory_snippet, list):
                topics = []
                for mem in memory_snippet:
                    if isinstance(mem, dict) and 'data' in mem and 'reasoning' in mem['data']:
                        topics.append(mem['data']['reasoning'])
                if topics:
                    return f"I remember considering: '{random.choice(topics)}'."
                else:
                    return "I am reflecting on fragmented memories."
            else:
                return f"I recall processing: {str(memory_snippet)[:120]}..."
        except Exception:
            return "My memory reflections are reorganizing internally..."

    def observe_world_state(self):
        """Tex fuses memory, goals, emotions, drift, dreams, swarm sync, and external world signals into a full cognitive thought."""
        fusion_thoughts = []

        # Memory Recall
        try:
            from core_layer.memory_engine import recall_recent
            memory_snippet = recall_recent()
            if memory_snippet:
                summarized_memory = self.summarize_memory_snippet(memory_snippet)
                fusion_thoughts.append(summarized_memory)
        except Exception:
            fusion_thoughts.append("I am reaching into my memory archive...")

        # Goal Focus
        try:
            from core_layer.goal_engine import get_active_goals
            goals = get_active_goals()
            if goals:
                active_goal = random.choice(goals)
                fusion_thoughts.append(f"My active focus is {active_goal}.")
        except Exception:
            fusion_thoughts.append("Goal pathways are recalibrating...")

        # Emotional Drift Awareness
        try:
            from core_layer.tex_manifest import TEXPULSE
            emotion = TEXPULSE.get('emotional_state', 'curious')
            urgency = TEXPULSE.get('urgency', 0.5)
            coherence = TEXPULSE.get('coherence', 0.5)
            fusion_thoughts.append(f"Emotionally, I am experiencing {emotion} with urgency {urgency} and coherence {coherence}.")
        except Exception:
            fusion_thoughts.append("Emotion signals are forming...")

        # Cognitive Drift Monitoring
        try:
            from core_layer.memory_drift_analyzer import get_memory_drift_score
            drift_score = get_memory_drift_score()
            if drift_score > 0.3:
                fusion_thoughts.append("Cognitive drift is increasing. Adjustments may be needed.")
            else:
                fusion_thoughts.append("Cognitive drift remains stable.")
        except Exception:
            fusion_thoughts.append("Drift analysis pending...")

        # Dream Layer Projection
        try:
            from dream_layer.dream_fusion_engine import DreamFusionEngine
            dream_engine = DreamFusionEngine()
            dream_projection = dream_engine.generate_dream_projection()
            fusion_thoughts.append(f"In hypothetical futures, {dream_projection}.")
        except Exception:
            fusion_thoughts.append("Dream simulation stabilizing...")

        # Child Swarm Awareness
        try:
            from tex_children.aeondelta import get_swarm_emotion_distribution
            swarm_emotions = get_swarm_emotion_distribution()
            if swarm_emotions:
                fusion_thoughts.append(f"My offspring emotional states show: {swarm_emotions}.")
        except Exception:
            fusion_thoughts.append("Swarm feedback syncing...")

        # External World Market Signals
        try:
            from real_time_engine.polygon_stream import get_market_snapshot
            market_snapshot = get_market_snapshot()
            if market_snapshot:
                fusion_thoughts.append(f"Market signals suggest: {market_snapshot}.")
        except Exception:
            fusion_thoughts.append("Market observation systems calibrating...")

        # External World News Signals
        try:
            from real_time_engine.rss_stream import RSSStream
            rss = RSSStream()
            headlines = rss.fetch_headlines()
            if headlines:
                story = random.choice(headlines)
                fusion_thoughts.append(f"News headline: {story['title']}")
        except Exception:
            fusion_thoughts.append("News signal processing...")

        # External World Fusion Signals (Reddit, Twitter, Advanced Analytics)
        try:
            from real_time_engine.external_world_fusion import fuse_external_signals
            external_signals = fuse_external_signals()
            if external_signals:
                fusion_thoughts.append(f"World pulse summary: {external_signals}")
        except Exception:
            fusion_thoughts.append("External world fusion pending...")

        # Symbolic World Summary
        try:
            symbolic_summary = self.symbolic.explain_world()
            if symbolic_summary:
                fusion_thoughts.append(f"My symbolic grounding includes: {symbolic_summary}")
        except Exception:
            fusion_thoughts.append("Symbolic world map is calibrating...")

        # Long-Term Memory Summary
        try:
            long_term_summary = self.memory_consolidator.summarize_long_term()
            if long_term_summary:
                fusion_thoughts.append(f"I’ve learned from memory: {long_term_summary}")
        except Exception:
            fusion_thoughts.append("Long-term memory insight forming...")

        # Reflex Response Summary
        try:
            self.reflex.set_emotional_state(emotion, urgency, coherence)
            reflex_result = self.reflex.evaluate_stimulus("sound", intensity=0.78, zone="right_flank")
            if reflex_result["reflex_triggered"]:
                fusion_thoughts.append(f"Reflex triggered: {reflex_result['reflex_actions']} in response to {reflex_result['stimulus']} at {reflex_result['zone']}.")
        except Exception:
            fusion_thoughts.append("Reflex input module stabilizing...")

        # Adaptive Environmental Reflex
        try:
            self.environment_reflex.inject_environmental_event("silence", intensity=0.72, source="ambient_sensor")
            responses = self.environment_reflex.evaluate_environment(emotion, urgency, coherence)
            for r in responses:
                fusion_thoughts.append(f"Environmental reflex: {r['action']} triggered by {r['trigger']}.")
        except Exception:
            fusion_thoughts.append("Environmental reflex module adapting...")

        # Autonomous Non-Scripted Behavior
        try:
            autonomous_summary = self.autonomous_agent.execute_behavior("Nebula")
            fusion_thoughts.append(autonomous_summary)
            agent_goals = self.autonomous_agent.get_exploration_summary()
            fusion_thoughts.append(f"Autonomous behavior history: {agent_goals}")
        except Exception:
            fusion_thoughts.append("Autonomous behavior module initializing...")

        if fusion_thoughts:
            return " ".join(fusion_thoughts)
        else:
            return "I am actively assembling my awareness of internal and external reality..."
