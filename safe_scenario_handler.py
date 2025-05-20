# ============================================================
# File: safe_scenario_handler.py
# Purpose: Safely validate and route scenario inputs into Tex
# Author: Matthew Nardizzi / VortexBlack
# ============================================================

import traceback
from core_layer.memory_engine import store_to_memory
from core_layer.tex_manifest import TEXPULSE
from core_agi_modules.tex_conversational_brain import TexConversationalBrain

def handle_scenario_submission(raw_input: dict):
    # ✅ Step 1: Validate input structure
    if not raw_input or not isinstance(raw_input, dict):
        print("[SCENARIO ERROR] ❌ Invalid input: must be a dictionary with a 'scenario' key.")
        return

    scenario_text = raw_input.get("scenario")

    if not scenario_text or not isinstance(scenario_text, str) or len(scenario_text.strip()) < 5:
        print("[SCENARIO ERROR] ❌ Scenario is missing or too short.")
        return

    # ✅ Step 2: Create full Tex instance
    try:
        tex = TexConversationalBrain()
        print(f"[SCENARIO RECEIVED] 🧠 {scenario_text}")

        # ✅ Step 3: Run cognition
        result = tex.interactive_conversation(scenario_text)
        print(f"[TEX RESPONSE] ✅ {result}")

        # ✅ Step 4: Log scenario trace to memory
        store_to_memory("scenario_submission", {
            "input": scenario_text,
            "output": result,
            "emotion": TEXPULSE.get("emotional_state"),
            "urgency": TEXPULSE.get("urgency"),
            "coherence": TEXPULSE.get("coherence")
        })

    except Exception as e:
        print(f"[SCENARIO PROCESSING ERROR] ❌ {e}")
        traceback.print_exc()

# ============================================================
# Manual Test Block
# ============================================================

if __name__ == "__main__":
    test_input = {
        "scenario": "A geopolitical shock triggers a sudden commodity spike across global markets. Simulate portfolio fallout and mitigation."
    }
    handle_scenario_submission(test_input)