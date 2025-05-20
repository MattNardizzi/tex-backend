# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: core_layer/self_monitor.py
# Purpose: Detect goal repetition, contradiction, and trigger mutation
# ============================================================

import datetime
import json
import os
from evolution_layer.self_mutator import trigger_mutation
from tex_brain_modules.tex_patcher_engine import TexPatcherEngine

class SelfMonitor:
    def __init__(self, path="memory_archive/evaluation_history.json"):
        self.log_path = path
        self.last_goals = []
        self.goal_stall_threshold = 3  # Same goal executed N times
        os.makedirs(os.path.dirname(path), exist_ok=True)

        if not os.path.exists(self.log_path):
            with open(self.log_path, "w") as f:
                json.dump([], f)

    def log_decision(self, input_context, decision, outcome=None, contradiction=False):
        record = {
            "timestamp": datetime.datetime.now().isoformat(),
            "input": input_context,
            "decision": decision,
            "outcome": outcome,
            "contradiction": contradiction
        }

        with open(self.log_path, "r+") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
            data.append(record)
            f.seek(0)
            json.dump(data, f, indent=2)

        if contradiction:
            print("[SELF MONITOR] ⚠️ Contradiction detected — triggering mutation.")
            trigger_mutation(reason="Contradiction in cognition trace")

    def check_logs(self, current_goal=None):
        print("[SELF MONITOR] ✅ check_logs() running.")
        
        if current_goal:
            self.last_goals.append(current_goal)
            if len(self.last_goals) > self.goal_stall_threshold:
                self.last_goals.pop(0)

            if self.last_goals.count(current_goal) == self.goal_stall_threshold:
                print(f"[SELF MONITOR] 🔁 Goal loop detected for: '{current_goal}'")
                trigger_mutation(reason=f"Goal '{current_goal}' repeated {self.goal_stall_threshold}x")
                self.last_goals.clear()  # Reset loop memory after mutation

# === Voice Reflection Logging ===
def log_voice_reflection(text, emotion):
    """
    Records every vocalized statement by Tex for self-monitoring analysis.
    """
    record = {
        "timestamp": datetime.datetime.now().isoformat(),
        "type": "voice_output",
        "spoken_text": text,
        "emotion": emotion
    }

    path = "memory_archive/voice_reasoning.jsonl"
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "a") as f:
        f.write(json.dumps(record) + "\n")

    # ✅ Self-patching trigger on low coherence
    from core_layer.tex_manifest import TEXPULSE
    patcher = TexPatcherEngine()
    if TEXPULSE.get("coherence", 1.0) < 0.45:
        target = "core_layer/meta_coherence_loop.py"
        placeholder_code = "# Placeholder patch triggered due to unstable coherence"
        patcher.propose_patch(target, placeholder_code, reason="low coherence instability")