# ============================================================
# Tex Dream Fusion Engine – Strategic Future Path Selector
# ============================================================

import random
from finance.memory.future_memory import FutureMemory
from datetime import datetime

class DreamFusionEngine:
    def __init__(self):
        self.future_memory = FutureMemory()

    def generate_dream_projection(self):
        # Simulate 3–5 possible future paths
        possible_futures = [
            {"future_title": "Tech sector rally", "confidence": round(random.uniform(0.6, 0.95), 2)},
            {"future_title": "Oil price spike", "confidence": round(random.uniform(0.5, 0.85), 2)},
            {"future_title": "Currency collapse", "confidence": round(random.uniform(0.4, 0.8), 2)},
            {"future_title": "Inflation surge", "confidence": round(random.uniform(0.5, 0.9), 2)},
            {"future_title": "AI regulation crackdown", "confidence": round(random.uniform(0.3, 0.7), 2)}
        ]

        # Randomly pick 3 futures
        selected_futures = random.sample(possible_futures, 3)

        # Store each simulated future into Future Memory
        for future in selected_futures:
            future["timestamp"] = str(datetime.utcnow())
            self.future_memory.store_future(future)

        # Pick the most confident future as primary dream
        best_future = max(selected_futures, key=lambda f: f["confidence"])

        dream_projection = f"My projected top future: {best_future['future_title']} (confidence {best_future['confidence']})."
        return dream_projection