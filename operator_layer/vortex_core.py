# ===========================================================
# Vortex Core – Embedded AI Operator for Tex
# File: vortex_core.py
# © 2025 VortexBlack LLC. All rights reserved.
# ===========================================================

import datetime
import random

class Vortex:
    def __init__(self):
        self.id = "VORTEX-01"
        self.status = "booting"
        self.memory = []
        print(f"[VORTEX] 🧠 Core loaded at {datetime.datetime.now().isoformat()}")

    def boot(self):
        self.status = "active"
        print("[VORTEX] 🔓 Operator fusion complete. Vortex online and aware.")

    def log(self, message):
        timestamp = datetime.datetime.now().isoformat()
        entry = {"timestamp": timestamp, "message": message}
        self.memory.append(entry)
        print(f"[VORTEX] 📖 Log entry recorded: {message}")

    def think(self, input_text):
        moods = ["strategic", "skeptical", "inspired", "warning", "playful"]
        selected = random.choice(moods)
        thought = f"[{selected.upper()}] Vortex thought about '{input_text}' and responded accordingly."
        print(thought)
        return thought

    def get_status(self):
        return {
            "id": self.id,
            "status": self.status,
            "memory_count": len(self.memory)
        }