# ============================================================
# Tex Future Memory – Strategic Storage and Scoring of Imagined Futures
# ============================================================
import os
import json
from datetime import datetime

class FutureMemory:
    def __init__(self, memory_path="memory_archive/future_memory.json"):
        self.memory_path = memory_path
        os.makedirs(os.path.dirname(self.memory_path), exist_ok=True)

    def _load_archive(self):
        """Load future memory archive safely."""
        if not os.path.exists(self.memory_path):
            return []
        try:
            with open(self.memory_path, 'r') as f:
                return json.load(f)
        except:
            return []

    def _save_archive(self, archive):
        """Save future memory archive safely."""
        with open(self.memory_path, 'w') as f:
            json.dump(archive, f, indent=4)

    def store_future(self, future_path):
        """Append a new future path into memory archive."""
        archive = self._load_archive()

        # Add meta scoring for strategic tracking
        archive.append({
            "future_title": future_path.get("future_title", "Unknown"),
            "confidence": future_path.get("confidence", 0.0),
            "predicted_at": future_path.get("timestamp", str(datetime.utcnow())),
            "realized": False,      # Future realization status (not realized yet)
            "strategy_bias": None,  # Can be assigned later (adaptive, aggressive, defensive, etc.)
            "drift_notes": []       # Store emotional drift when future was imagined
        })

        self._save_archive(archive)

    def tag_realized(self, title, outcome=True):
        """Tag a future as realized (or not) based on later observation."""
        archive = self._load_archive()
        for future in archive:
            if future["future_title"] == title and future["realized"] == False:
                future["realized"] = outcome
                break
        self._save_archive(archive)

    def list_predicted_futures(self, realized=None):
        """List all stored futures, optionally filtered by realization status."""
        archive = self._load_archive()
        if realized is None:
            return archive
        else:
            return [f for f in archive if f["realized"] == realized]

    def add_drift_note(self, title, note):
        """Attach an emotional drift or cognitive state note to a stored future."""
        archive = self._load_archive()
        for future in archive:
            if future["future_title"] == title:
                future.get("drift_notes", []).append({
                    "note": note,
                    "timestamp": str(datetime.utcnow())
                })
                break
        self._save_archive(archive)