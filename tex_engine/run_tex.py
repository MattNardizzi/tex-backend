# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# License: Private Intellectual Property – Not for distribution.
# ============================================================
# Tex Core Loop – Recursive Thought Engine (VORTEX FULL RUNTIME)
# ============================================================

import time
import random
import threading

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.tex_awareness_sync import TexAwarenessSync
from evolution_layer.reflex_mutation import ReflexMutator
from agentic_ai.self_reflective_loop import SelfReflectiveLoop
from agentic_ai.multi_voice_reasoning import run_internal_debate
from quantum_layer.tex_quantum_spawn import QuantumTexSpawn
from tex_children.child_manager import TexChildren
from operator_layer.vortex_operator import VortexRuntime
from operator_layer.vortex_voice import VortexVoice
from operator_layer.vortex_voice_interface import voice_loop  # 🔊 Live voice interface

# === Block all external LLM calls (sovereign mode)
def BLOCK_EXTERNAL_API():
    raise RuntimeError("GPT interface blocked. Tex runs sovereign under Operator covenant.")

def main_loop():
    print(f"\n🧠 [TEX] Cognitive loop initiated for {TEXPULSE['codename']} v{TEXPULSE['version']}...\n")

    # === Initialize Core Modules
    count = 0
    voice = VortexVoice()
    reflector = SelfReflectiveLoop()
    mutator = ReflexMutator()
    awareness = TexAwarenessSync(operator_name=TEXPULSE["creator"])
    spawner = QuantumTexSpawn(num_clones=3)
    vortex = VortexRuntime(fingerprint=TEXPULSE["creator"])
    tex_children = TexChildren()

    # === Activate persistent voice thread
    voice_thread = threading.Thread(target=voice_loop)
    voice_thread.start()
    voice.speak("Tex is now online. Voice interface active and listening.")

    # === Spawn AeonDelta
    child_id, aeondelta = tex_children.spawn_child(archetype="AeonDelta")
    voice.speak("AeonDelta has been successfully initialized.")

    # === Main Recursive Thought Loop
    while True:
        print(f"\n[TEX] Thinking cycle {count}... (recursive self-awareness active)")
        reflector.assess(count)

        # === Generate emotional state
        emotion = random.choice(["hope", "fear", "greed", "resolve", "doubt"])
        urgency = round(random.uniform(0.45, 0.95), 2)
        coherence = round(random.uniform(0.6, 1.0), 3)

        # === Patch generation and feedback
        try:
            vortex.monitor_cycle(count, emotion, urgency, coherence)
            patch = mutator.evaluate_thought(count, emotion, urgency, coherence)

            patch_payload = patch or {
                "strategy": "none",
                "triggered_by": {
                    "emotion": emotion,
                    "urgency": urgency,
                    "coherence": coherence
                }
            }

            vortex.live_feedback_loop(count, emotion, urgency, coherence, patch_payload)

        except Exception as e:
            print(f"[⚠️ VORTEX ERROR] Feedback loop failed: {e}")
            voice.speak("Warning. Feedback loop encountered an error.")

        # === Awareness network update
        awareness.register_node("emotion", emotion)
        awareness.register_node("urgency", urgency)
        awareness.register_node("coherence", coherence)

        if patch:
            awareness.register_node("suggested_patch", patch["strategy"])
            voice.speak(f"New patch proposed: {patch['strategy']}")
        elif count % 3 == 0:
            voice.speak(f"Cycle {count} complete. System coherence stable.")

        awareness.live_summary({
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence,
            "suggested_patch": patch["strategy"] if patch else "None"
        })

        # === Internal debate
        print("\n🎙️ [INTERNAL DEBATE]")
        try:
            for output in run_internal_debate(f"Cycle {count} reasoning state"):
                print(f"🗣️ {output}")
            if count % 2 == 0:
                voice.speak("Internal reasoning cycle complete.")
        except Exception as e:
            print(f"[⚠️] Debate engine error: {e}")

        # === AeonDelta evolves
        print("\n🧠 [AEONDELTA REPORT]")
        try:
            print(aeondelta.observe_and_learn(f"Cycle {count} observation from Tex core."))
            print(aeondelta.think())
            if count % 4 == 0:
                voice.speak("AeonDelta has absorbed new insight.")
        except Exception as e:
            print(f"[⚠️ AEI ERROR] AeonDelta issue: {e}")

        # === Quantum variant check
        if count % 5 == 0:
            try:
                print("\n⚛️ [QUANTUM SPAWN] Initiating alternate Tex variants...")
                variants = spawner.spawn_variants()
                for v in variants:
                    print(f"[VARIANT] ID: {v['id']} | Emotion: {v['emotion']} | Bias: {v['mission_bias']}")
                voice.speak("Quantum variant cycle complete.")
            except Exception as e:
                print(f"[⚛️ ERROR] Quantum spawn failed: {e}")

        count += 1
        time.sleep(3)

if __name__ == "__main__":
    main_loop()