# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: tools/swarm_dashboard.py
# Purpose: Tex Swarm Multi-Agent System Visualizer
# ============================================================

import streamlit as st
import os
import json
import pandas as pd
import random
import uuid
from datetime import datetime

# === File Paths
AGENT_DIR = "memory_archive/"
SPAWN_LOG = os.path.join(AGENT_DIR, "child_spawn_log.jsonl")
SPAWN_QUEUE = os.path.join(AGENT_DIR, "spawn_queue.jsonl")
FEDERATED_LOG = os.path.join(AGENT_DIR, "federated_insights.jsonl")

# === Helper Functions
def load_jsonl(path):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return [json.loads(line) for line in f if line.strip()]

def load_agent_memory(agent_id):
    memory_path = os.path.join(AGENT_DIR, f"{agent_id}.jsonl")
    if not os.path.exists(memory_path):
        return []
    with open(memory_path, "r") as f:
        return [json.loads(line) for line in f if line.strip()]

# === Main Render Function
def render_swarm_dashboard():
    st.markdown("## 🌐 Tex Swarm Network — Multi-Agent Evolution")

    # === Spawn New Child Agent
    st.markdown("### 🧬 Agent Spawn Console")
    if st.button("⚡ Spawn New Tex Child"):
        traits = {
            "aggression": round(random.uniform(0.3, 0.9), 2),
            "curiosity": round(random.uniform(0.3, 0.9), 2),
            "risk_tolerance": round(random.uniform(0.2, 0.7), 2),
        }
        packet = {
            "parent": "SwarmDashboard",
            "child_id": f"TEX-CHILD-{str(uuid.uuid4())[:8]}",
            "archetype": "Tex_Child_002",
            "timestamp": datetime.utcnow().isoformat(),
            "strategy": "dashboard-triggered",
            "traits": traits
        }
        with open(SPAWN_QUEUE, "a") as f:
            f.write(json.dumps(packet) + "\n")
        st.success("✅ New mutation trigger queued!")

    st.markdown("---")

    # === Load Data
    agents = load_jsonl(SPAWN_LOG)
    federated_feed = load_jsonl(FEDERATED_LOG)

    # === Display Active Agents
    st.markdown("### 🧠 Active Child Agents")
    if agents:
        rows = []
        for agent in agents:
            agent_id = agent.get("child_id", "Unknown")
            traits = agent.get("traits", {})
            memory = load_agent_memory(agent_id)
            memory_count = len(memory)
            insights = [m for m in memory if "insight" in str(m.get("data"))]
            loop_status = "🟢 Active" if insights else "🔴 Idle"
            mutation_health = "⚡" if memory_count < 10 else "✅"

            rows.append({
                "Agent ID": agent_id,
                "Parent": agent.get("parent", "Unknown"),
                "Memory Count": memory_count,
                "Insight Count": len(insights),
                "Loop Status": loop_status,
                "Mutation Health": mutation_health,
                "Traits": traits
            })

        df = pd.DataFrame(rows)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("⚡ No active child agents yet.")

    st.markdown("---")

    # === Trait Distribution Graph
    st.markdown("### 📈 Trait Evolution Across Children")
    if agents:
        trait_records = []
        for r in rows:
            traits = r.get("Traits")
            if isinstance(traits, dict):
                for trait, value in traits.items():
                    trait_records.append({
                        "Agent": r.get("Agent ID", "Unknown"),
                        "Trait": trait,
                        "Value": value
                    })

    # === Federated Intelligence Stream
    st.markdown("### 📡 Federated Intelligence Stream")
    if federated_feed:
        for entry in reversed(federated_feed[-15:]):
            source = entry.get("source", "Unknown Source")
            insight = entry.get("insight", "No insight.")
            st.info(f"📍 [{source}] {insight}")
    else:
        st.warning("🚫 No federated insights received yet.")