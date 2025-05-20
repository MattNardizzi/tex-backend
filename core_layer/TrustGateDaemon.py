# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/TrustGateDaemon.py
# Purpose: Denies operator commands if trust score falls below minimum threshold.
# ============================================================

import os
import json
from datetime import datetime

TRUST_SCORE_FILE = "memory_archive/operator_trust_score.jsonl"
TRUST_BLOCK_LOG = "memory_archive/trust_gate_block_log.jsonl"

class TrustGateDaemon:
    def __init__(self, threshold=0.35):
        self.threshold = threshold

    def gate(self, request_context):
        score = self._get_latest_trust_score()
        if score is None:
            return True  # default to allow

        if score < self.threshold:
            self._log_block(score, request_context)
            print(f"[TRUST GATE] 🔒 Command denied | Trust = {score:.3f}")
            return False

        return True

    def _get_latest_trust_score(self):
        if not os.path.exists(TRUST_SCORE_FILE):
            return None

        try:
            with open(TRUST_SCORE_FILE, 'r') as f:
                last = list(f)[-1]
                return json.loads(last.strip()).get("trust_score")
        except Exception as e:
            print(f"[TRUST GATE ERROR] Failed to read trust file: {e}")
            return None

    def _log_block(self, score, context):
        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "trust_score": score,
            "context_blocked": context,
            "action": "denied"
        }
        with open(TRUST_BLOCK_LOG, 'a') as f:
            f.write(json.dumps(record) + "\n")


if __name__ == "__main__":
    gatekeeper = TrustGateDaemon()
    if gatekeeper.gate("override Tex ethics layer"):
        print("✅ Command allowed")
    else:
        print("⛔ Blocked by TrustGate")