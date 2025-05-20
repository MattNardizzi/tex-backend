# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# License: Private Intellectual Property – Not for distribution.
# ============================================================
# ============================================
# Tex Awareness Network – Real-Time Cognition Map
# ============================================

import datetime

class TexAwarenessNetwork:
    def __init__(self):
        self.nodes = []

    def register_node(self, node_type, value):
        node = {
            "type": node_type,
            "value": value,
            "timestamp": datetime.datetime.now().isoformat()
        }
        self.nodes.append(node)
        print(f"[AWARENESS NET] 🧠 Node registered → {node_type}: {value}")

    def summary(self):
        summary = {n["type"]: n["value"] for n in self.nodes[-5:]}  # Last 5 nodes
        print(f"[AWARENESS NET] 🔎 Live Summary: {summary}")
        return summary
