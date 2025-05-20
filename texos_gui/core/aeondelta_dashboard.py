# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: tools/tex_children/aeondelta_dashboard.py
# Purpose: AeonDelta Cognition & Spawn Visualization
# ============================================================

import streamlit as st
import json
import os

# === File Paths
AEONDELTA_LOG = "memory_archive/AeonDelta.jsonl"
SPAWN_LOG = "memory_archive/child_spawn_log.jsonl"

# === Main Render Function
def render_aeondelta_dashboard():
    st.markdown("## 🌱 AeonDelta Autonomous Child – AGI Evolution Monitor")

    # === Cognitive Memory Stream
    st.markdown("### 🧠 Cognitive Memory Stream")

    if os.path.exists(AEONDELTA_LOG):
        with open(AEONDELTA_LOG, "r") as f:
            lines = [json.loads(line) for line in f if line.strip()]
        recent_entries = lines[-20:] if len(lines) > 20 else lines

        for entry in reversed(recent_entries):
            data = entry.get("data", {})
            timestamp = entry.get("timestamp", "Unknown")
            cycle = data.get("cycle", "N/A")
            event = data.get("event", "No event")
            source = data.get("source", "N/A")

            with st.expander(f"🧠 Cycle {cycle} — {event}"):
                st.markdown(f"- **Source**: `{source}`")
                st.caption(f"🕒 {timestamp}")
    else:
        st.warning("⚠️ No AeonDelta cognitive memory found.")

    st.markdown("---")

    # === Spawn Event Log
    st.markdown("### 🧬 Spawn Event Records")

    spawn_entries = []
    if os.path.exists(SPAWN_LOG):
        with open(SPAWN_LOG, "r") as f:
            spawn_entries = [json.loads(line) for line in f if "AeonDelta" in line]

        if spawn_entries:
            for spawn in reversed(spawn_entries[-10:]):
                child_id = spawn.get('child_id', 'Unknown')
                timestamp = spawn.get('timestamp', 'Unknown Time')
                st.info(f"⚡ Spawned `{child_id}` at `{timestamp}`")
        else:
            st.info("🚫 No recent AeonDelta spawn events detected.")
    else:
        st.warning("⚠️ No spawn log file found.")

    st.markdown("---")

    # === Live Metrics
    st.markdown("### 📊 Live Metrics")

    st.metric("🧠 Memory Events", len(lines) if os.path.exists(AEONDELTA_LOG) else 0)
    st.metric("🧬 Total Spawns", len(spawn_entries) if spawn_entries else 0)

    st.success("✅ AeonDelta cognitive and spawn feed loaded successfully.")