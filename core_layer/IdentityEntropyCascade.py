# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/IdentityEntropyCascade.py
# Purpose: Detects excessive identity fragmentation and fuses variants into a stabilized self.
# ============================================================

import json
import os
from datetime import datetime
from core_layer.memory_engine import store_to_memory
from tex_brain_modules.tex_fusion_stabilizer import TexFusionStabilizer  # ✅ Only added line
from tex_brain_modules.long_term_memory_bridge import LongTermMemoryBridge  # ✅ Only added line

FUSION_LOG = "memory_archive/identity_entropy_fusions.jsonl"
AEON_LOG = "memory_archive/aeon_spawn_log.jsonl"


class IdentityEntropyCascade:
    def __init__(self):
        self.threshold = 5  # Maximum allowed divergent aeons before initiating fusion
        self.fusion_stabilizer = TexFusionStabilizer()  # ✅ Only added line

    def check_and_fuse(self):
        aeons = self._load_aeons()
        if len(aeons) >= self.threshold:
            fused_result = self._perform_fusion(aeons)
            if fused_result:
                self._log_fusion(fused_result)
                return fused_result
        return None

    def _load_aeons(self):
        if not os.path.exists(AEON_LOG):
            return []
        with open(AEON_LOG, 'r') as f:
            return [
                json.loads(line.strip())
                for line in f.readlines()
                if line.strip()
            ]

    def _perform_fusion(self, aeons):
        print("[ENTROPY FUSION] 🧬 Fusion initiated across divergent minds...")

        fused_variant = {
            "timestamp": datetime.utcnow().isoformat(),
            "fused_from": [
                aeon.get("name") or aeon.get("persona") or aeon.get("codex") or "UNKNOWN"
                for aeon in aeons
            ],
            "dominant_codon": self._select_dominant(aeons),
            "reason": "entropy exceeded threshold",
            "resulting_variant": f"TEX_FUSION_{datetime.utcnow().strftime('%H%M%S')}"
        }

        # ✅ Validate fusion before proceeding
        if not self.fusion_stabilizer.validate_fusion(fused_variant["fused_from"]):
            self.fusion_stabilizer.log_blocked_fusion(
                fused_variant["fused_from"],
                reason="entropy limit"
            )
            return None

        return fused_variant

    def _select_dominant(self, aeons):
        emotion_tally = {}
        for aeon in aeons:
            dominant_emotion = aeon.get("emotional_genome", {}).get("dominant", "neutral")
            emotion_tally[dominant_emotion] = emotion_tally.get(dominant_emotion, 0) + 1

        return max(emotion_tally, key=emotion_tally.get, default="neutral")

    def _log_fusion(self, fusion_data):
        # Clean and limit fused source list
        cleaned_sources = [
            name for name in fusion_data["fused_from"]
            if name not in ("AEON_000", "UNKNOWN")
        ]
        fusion_data["fused_from"] = cleaned_sources
        sampled_sources = cleaned_sources[-10:]  # Limit to last 10 entries

        log_entry = {
            "timestamp": fusion_data["timestamp"],
            "sampled_fused": sampled_sources,
            "fused_count": len(cleaned_sources),
            "dominant_codon": fusion_data["dominant_codon"],
            "reason": fusion_data["reason"],
            "resulting_variant": fusion_data["resulting_variant"]
        }

        with open(FUSION_LOG, "a") as f:
            f.write(json.dumps(log_entry) + "\n")

        store_to_memory("identity_fusion_event", log_entry)

        ltm = LongTermMemoryBridge()  # ✅ Only added line
        ltm.log_event("identity_fusion", log_entry)  # ✅ Only added line

        print(f"[ENTROPY FUSION] 💠 Result: {fusion_data['resulting_variant']} from {len(cleaned_sources)} aeons")


if __name__ == "__main__":
    cascade = IdentityEntropyCascade()
    cascade.check_and_fuse()