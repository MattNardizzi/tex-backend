# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: swarm_layer/signal_entropy_checker.py
# Purpose: Tex Inter-Agent Signal Leak Detector — Entropy-Based Echo Detection
# ============================================================

from datetime import datetime
import hashlib

class SignalEntropyChecker:
    def __init__(self, entropy_threshold=0.65):
        self.entropy_threshold = entropy_threshold

    def analyze_signals(self, agent_signals):
        hashes = [self._hash_signal(s) for s in agent_signals if s.strip()]
        unique_hashes = set(hashes)

        if not hashes:
            return self._build_packet(0.0, 0, 0)

        entropy_score = 1.0 - (len(unique_hashes) / len(hashes))
        entropy_score = round(min(max(entropy_score, 0.0), 1.0), 3)

        return self._build_packet(entropy_score, len(agent_signals), len(unique_hashes))

    def _hash_signal(self, signal):
        return hashlib.sha256(signal.lower().strip().encode()).hexdigest()

    def _build_packet(self, entropy_score, total_signals, unique_signals):
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "signal_entropy": entropy_score,
            "total_signals": total_signals,
            "unique_signals": unique_signals,
            "echo_chamber_risk": entropy_score > self.entropy_threshold
        }
