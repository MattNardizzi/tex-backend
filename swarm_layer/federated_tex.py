# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: swarm_layer/federated_tex.py
# Purpose: Swarm Intelligence + Agent Consensus Coordinator
# ============================================================

import datetime

class FederatedTex:
    def __init__(self):
        self.shared_insights = []
        self.agents = {}

    def broadcast_insight(self, source_id, insight):
        record = {
            "source": source_id,
            "insight": insight,
            "timestamp": datetime.datetime.now().isoformat()
        }
        self.shared_insights.append(record)
        print(f"[FEDERATED] 📡 Insight from {source_id}: {insight}")
        return record

    def register_agent(self, agent_id, traits=None):
        self.agents[agent_id] = {
            "registered_at": datetime.datetime.now().isoformat(),
            "traits": traits or {},
            "insights": 0
        }
        print(f"[FEDERATED] 🧬 Agent registered: {agent_id}")
        return self.agents[agent_id]

    def log_agent_insight(self, agent_id, insight):
        self.broadcast_insight(agent_id, insight)
        if agent_id in self.agents:
            self.agents[agent_id]["insights"] += 1

    def reach_consensus(self):
        if not self.shared_insights:
            print("[FEDERATED] No shared insights to analyze.")
            return None

        insights = [entry["insight"] for entry in self.shared_insights]
        consensus = max(set(insights), key=insights.count)
        print(f"[FEDERATED] 🧠 Swarm consensus formed: {consensus}")
        return consensus

    def list_agents(self):
        return list(self.agents.keys())

    def recommend_mutation(self):
        if not self.agents:
            return None
        sorted_agents = sorted(self.agents.items(), key=lambda x: x[1]["insights"])
        weakest = sorted_agents[0][0]
        print(f"[FEDERATED] ⚠️ Recommending mutation for: {weakest}")
        return weakest


# === Global instance
federated_swarm = FederatedTex()

# === Interfaces for external use
def register_child_agent(agent_id, traits=None):
    return federated_swarm.register_agent(agent_id, traits)

def push_insight(agent_id, insight):
    return federated_swarm.log_agent_insight(agent_id, insight)