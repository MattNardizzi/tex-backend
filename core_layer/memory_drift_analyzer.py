# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# License: Private Intellectual Property – Not for distribution.
# ============================================================
# Memory Drift Analyzer — Tracks Long-Term AGI Memory Coherence
# ============================================================

import datetime
import hashlib

class MemoryDriftAnalyzer:
    def __init__(self):
        self.snapshots = []

    def capture_snapshot(self, memory_state: dict):
        hash_val = self._hash_memory(memory_state)
        timestamp = datetime.datetime.now().isoformat()
        self.snapshots.append((timestamp, hash_val))
        print(f"[DRIFT] 📦 Snapshot taken @ {timestamp} → Hash: {hash_val}")

    def detect_drift(self):
        if len(self.snapshots) < 2:
            print("[DRIFT] ⏳ Not enough data to detect drift.")
            return False
        _, last = self.snapshots[-1]
        _, prev = self.snapshots[-2]
        drift_detected = last != prev
        if drift_detected:
            print("[DRIFT] ⚠️ Drift detected between last two snapshots.")
        else:
            print("[DRIFT] ✅ Memory stable.")
        return drift_detected

    def _hash_memory(self, memory: dict):
        serialized = str(sorted(memory.items())).encode()
        return hashlib.sha256(serialized).hexdigest()
