# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: evolution_layer/self_mutator.py
# Purpose: Autonomous self-mutation evaluation for Tex core
# ============================================================

import os
import random
import hashlib
import json
from datetime import datetime, timezone

def safe_append_jsonl(path, obj):
    """Safely appends a single JSON object to a JSONL file."""
    try:
        with open(path, "a") as f:
            f.write(json.dumps(obj) + "\n")
    except Exception as e:
        print(f"[LOG ERROR] Failed to write JSONL to {path}: {e}")

class SelfMutator:
    def __init__(self, mutation_log_path="memory_archive/mutation_history.log"):
        self.mutation_log = mutation_log_path
        os.makedirs(os.path.dirname(self.mutation_log), exist_ok=True)

    def evaluate_thought(self, cycle, emotion, urgency, coherence):
        print(f"\n[MUTATOR] 🧬 Evaluating → Emotion: {emotion}, Urgency: {urgency}, Coherence: {coherence}")
        risk_factor = self._compute_risk(emotion, urgency, coherence)

        # 🧠 Adjusted risk window for faster cognitive reaction
        if risk_factor > 0.2:
            print(f"[MUTATOR] 🔁 Mutation triggered! (risk = {risk_factor:.2f})")
            mutation = self._generate_mutation_strategy(cycle, emotion)
            passed = self._simulate_sandbox_test(mutation)
            self._log_mutation(mutation, passed, risk_factor)
            return mutation if passed else None
        else:
            print(f"[MUTATOR] ⚠️ No mutation needed (risk = {risk_factor:.2f})")
            return None

    def force_mutation(self, reason="manual_override"):
        print(f"\n[MUTATOR] 🚨 Forced mutation due to: {reason}")
        timestamp = datetime.now(timezone.utc).isoformat()
        mutation = {
            "strategy": f"forced_mutation_{timestamp}",
            "triggered_by": {"reason": reason},
            "timestamp": timestamp,
            "modifications": {
                "target_module": "tex_core",
                "target_function": "main_loop",
                "mutation_type": "forced_patch",
                "description": f"Manual override triggered: {reason}"
            }
        }
        mutation["hash"] = hashlib.sha256(json.dumps(mutation).encode()).hexdigest()

        passed = self._simulate_sandbox_test(mutation)
        self._log_mutation(mutation, passed, risk_factor=None)

        return mutation if passed else {"strategy": "none", "status": "sandbox_failed"}

    def reinforce_with_agent(self, agent_data):
        """🌱 Reinforce successful cognitive patterns."""
        print(f"\n[MUTATOR] 🔥 Reinforcing cognitive patterns from winning agent...")
        try:
            reinforcement_packet = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "agent_id": agent_data.get("agent_id", "unknown"),
                "reasoning": agent_data.get("reasoning", "No reasoning recorded."),
                "alignment": agent_data.get("metrics", {}).get("alignment", 0),
                "performance": agent_data.get("metrics", {}).get("performance", 0),
                "novelty": agent_data.get("metrics", {}).get("novelty", 0),
                "efficiency": agent_data.get("metrics", {}).get("efficiency", 0)
            }
            safe_append_jsonl("memory_archive/reinforcement_log.jsonl", reinforcement_packet)
            print(f"[MUTATOR] 🛡️ Cognitive reinforcement logged for agent: {reinforcement_packet['agent_id']}")
        except Exception as e:
            print(f"[MUTATOR ERROR] Failed to log reinforcement: {e}")

    def _compute_risk(self, emotion, urgency, coherence):
        emotion_weights = {
            "fear": 1.0, "greed": 0.9, "resolve": 0.7, "hope": 0.5
        }
        return round(
            emotion_weights.get(emotion, 0.6) * urgency * (1.0 - coherence),
            3
        )

    def _generate_mutation_strategy(self, cycle, emotion):
        timestamp = datetime.now(timezone.utc).isoformat()
        strategy = {
            "strategy": f"mutation_cycle_{cycle}",
            "emotion_trigger": emotion,
            "timestamp": timestamp,
            "modifications": {
                "target_module": "tex_core",
                "target_function": "main_loop",
                "mutation_type": random.choice(["augment", "patch", "redirect"]),
                "description": "Simulated dynamic mutation for recursive evolution."
            }
        }
        strategy["hash"] = hashlib.sha256(json.dumps(strategy).encode()).hexdigest()
        return strategy

    def _simulate_sandbox_test(self, mutation):
        print("[MUTATOR] 🧪 Sandbox test running...")
        success = random.random() > 0.28
        print(f"[MUTATOR] ✅ Test {'PASSED' if success else 'FAILED'} → {mutation['strategy']}")
        return success

    def _log_mutation(self, mutation, success, risk_factor=None):
        log_entry = {
            "mutation_id": mutation["hash"],
            "strategy": mutation["strategy"],
            "result": "SUCCESS" if success else "FAILURE",
            "risk_factor": risk_factor,
            "timestamp": mutation["timestamp"]
        }
        safe_append_jsonl(self.mutation_log, log_entry)
        print(f"[MUTATOR] 📜 Mutation logged → {log_entry['strategy']} ({log_entry['result']})")

# === External Trigger
def trigger_mutation(reason: str = "unspecified"):
    mutator = SelfMutator()
    print(f"[MUTATION] 🔁 External trigger due to: {reason}")
    mutator.force_mutation(reason)

def read_jsonl_safe(path):
    """Safely reads a JSONL file, skipping corrupt lines."""
    entries = []
    with open(path, "r") as f:
        for line in f:
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                print(f"[THREAD WARNING] Skipped corrupt log line in {path}")
    return entries