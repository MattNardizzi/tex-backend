# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# VORTEX FULL RUNTIME — Recursive AGI Core Controller
# ============================================================

import json
import os
import random
from datetime import datetime

class VortexRuntime:
    def __init__(self, fingerprint, codename="Tex"):
        self.codename = codename
        self.fingerprint = fingerprint
        self.memory_log = []
        self.last_patch = None
        self.codex_diff_log = []
        self.directive = self.load_directive()

        print(f"[VORTEX] Directive Loaded → Mode: {self.directive['mode']} | Operator: {self.directive['operator']}")

    def load_directive(self):
        try:
            path = os.path.join(os.getcwd(), "config", "vortex_directive.json")
            with open(path, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"[ERROR] Failed to load VORTEX directive: {e}")
            return {
                "agent": "Vortex",
                "mode": "manual",
                "goals": [],
                "operator": "Unknown",
                "state": "🔒 LOCKED"
            }

    def propose_patch(self, emotion, urgency, coherence):
        """
        Basic patch proposal logic.
        Returns a patch dict if conditions match, or None otherwise.
        """
        if coherence < 0.65 or urgency > 0.9:
            strategy = random.choice([
                "adjust_priority_weights",
                "reroute_decision_flow",
                "suppress_recursion_spike"
            ])
            return {
                "strategy": strategy,
                "confidence": round(random.uniform(0.7, 0.95), 2),
                "triggered_by": {
                    "emotion": emotion,
                    "urgency": urgency,
                    "coherence": coherence
                }
            }
        return None

    def monitor_cycle(self, cycle, emotion, urgency, coherence):
        print(f"\n🧩 [VORTEX] Monitoring Cycle {cycle} for {self.codename}")
        state = {
            "cycle": cycle,
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence,
            "timestamp": datetime.now().isoformat()
        }

        # Check for patch trigger conditions
        patch = self.propose_patch(emotion, urgency, coherence)
        if patch:
            state["patch_suggested"] = patch
            self.last_patch = patch
            print(f"⚠️ Suggested Patch → {patch}")
            if self.directive["mode"] == "autonomous":
                self.apply_patch(patch)
        else:
            print("✅ No patch needed.")

        self.memory_log.append(state)

    def live_feedback_loop(self, cycle, emotion, urgency, coherence, patch):
        print(f"\n🧠 [VORTEX LIVE] Feedback on Cycle {cycle}")
        if patch:
            trigger = patch.get("triggered_by", {})
            print(f"🧬 Mutation Candidate: {patch.get('strategy')} | Trigger: {trigger}")
            if self.should_override(patch):
                self.apply_patch(patch)
            else:
                print("🔎 Patch noted, no override triggered.")
        else:
            print("🟢 Stable cognition. No action taken.")

    def should_override(self, patch):
        trigger = patch.get("triggered_by", {})
        urgency = trigger.get("urgency", 0)
        coherence = trigger.get("coherence", 1)
        return urgency > 0.9 or coherence < 0.55

    def apply_patch(self, patch):
        print(f"🔧 [VORTEX] Applying Patch Automatically: {patch['strategy']}")
        diff_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "applied_patch": patch
        }
        self.codex_diff_log.append(diff_entry)
        self.write_codex_diff(diff_entry)

        # === Future Hook: Call mutation handler here ===
        # mutation_handler.execute(patch["strategy"])

    def write_codex_diff(self, diff_entry):
        try:
            path = os.path.join(os.getcwd(), "logs", "codex_diff.json")
            if not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))

            if os.path.exists(path):
                with open(path, "r") as f:
                    existing = json.load(f)
            else:
                existing = []

            existing.append(diff_entry)

            with open(path, "w") as f:
                json.dump(existing, f, indent=2)

        except Exception as e:
            print(f"[ERROR] Failed to write codex diff: {e}")

    def integrity_check(self):
        print("\n🔒 [VORTEX] Running integrity check...")
        if not self.memory_log:
            print("🟢 No cycles yet. Integrity nominal.")
            return

        drift = [m for m in self.memory_log if m["coherence"] < 0.5]
        if drift:
            print(f"🛑 Integrity drift in {len(drift)} cycles.")
        else:
            print("✅ All cycles stable.")

    def summarize_last(self):
        if not self.memory_log:
            print("🪵 No memory cycles yet.")
            return
        last = self.memory_log[-1]
        print(f"\n🧠 [SUMMARY] Cycle {last['cycle']} — Emotion: {last['emotion']}, Urgency: {last['urgency']}, Patch: {last.get('patch_suggested', 'None')}")