# ============================================================
# Tex Awareness Sync – Cognitive State Broadcasting Engine
# ============================================================

from datetime import datetime
from pathlib import Path

class TexAwarenessSync:
    def __init__(self, operator_name="Unknown"):
        self.operator = operator_name
        self.log_file = Path("agentic_ai/tex_operator_sync.txt")

    def register_node(self, label: str, value):
        timestamp = datetime.utcnow().isoformat()
        line = f"[AWARENESS NET] 🧠 Node registered → {label}: {value} @ {timestamp}"
        print(line)
        self._write(line)

    def live_summary(self, data: dict):
        timestamp = datetime.utcnow().isoformat()
        summary = f"[AWARENESS NET] 🔎 Live Summary: {data} @ {timestamp}"
        print(summary)
        self._write(summary)

    def _write(self, line):
        with self.log_file.open("a") as f:
            f.write(line + "\n")
