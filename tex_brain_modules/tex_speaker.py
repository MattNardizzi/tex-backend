# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/tex_speaker.py
# Purpose: Exact copy of speak() from tex_conversational_brain.py
# ============================================================

import os
import json
from core_layer.self_monitor import log_voice_reflection
from core_layer.memory_engine import store_to_memory
from aei_layer.causal_thought_logger import log_causal_trace
from core_layer.tex_manifest import TEXPULSE  # used indirectly by .presence

def speak(self, text, emotion="neutral"):
        print(f"[TEX SPEAKING OUT LOUD] 🤔 {text}")
        self.is_speaking = True
        self.voice_speaker.interrupt_flag = False
        self.voice_speaker.speak(text, emotion=emotion)
        log_voice_reflection(text, emotion)

        # ✅ Force a tex memory entry
        try:
            store_to_memory("tex", {
                "cycle": self.cycle_counter,
                "spoken": text,
                "emotion": emotion,
                "context": "tex dashboard output"
            })
        except Exception as e:
            print(f"[TEST] Tex memory log failed: {e}")

        # ✅ Causal Thought Logger
        try:
            log_causal_trace(
                cycle_id=self.cycle_counter,
                thought=text,
                decision="spoken_output",
                emotion=emotion
            )
        except Exception as e:
            print(f"[THOUGHT LOGGER ERROR] {e}")

        # ✅ NEW: Write live thought to dashboard JSON stream
        try:
            dashboard_path = os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                "public", "live_outputs", "last_spoken_thought.json"
            )
            with open(dashboard_path, "w") as f:
                json.dump({"thought": text}, f)
        except Exception as e:
            print(f"[DASHBOARD SYNC ERROR] {e}")

               # ✅ Presence stream logging
        try:
            self.presence.write(self.cycle_counter, text, emotion)
        except Exception as e:
            print(f"[PRESENCE LOG ERROR] {e}")

        self.is_speaking = False