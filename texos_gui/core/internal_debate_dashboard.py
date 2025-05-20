# ============================================================
# Tex Internal Debates Visualizer
# File: tools/internal_debate_dashboard.py
# Purpose: Live feed of Tex's internal multi-voice debates
# ============================================================

import streamlit as st
import os
import json
from datetime import datetime

# === File Path ===
DEBATE_LOG = "memory_archive/debate_log.jsonl"

# === Load Debates ===
def load_debate_log():
    if not os.path.exists(DEBATE_LOG):
        return []
    with open(DEBATE_LOG, "r") as f:
        return [json.loads(line) for line in f if line.strip()]

# === Main Render Function ===
def render_internal_debate_dashboard():
    st.markdown("## 🗣️ Tex Internal Debates Tracker")
    st.caption("Live feed of internal agent disagreements, debates, and resolutions.")

    debates = load_debate_log()

    if not debates:
        st.info("⚠️ No internal debates recorded yet.")
        return

    # Sort debates by latest
    debates = sorted(debates, key=lambda x: x.get("timestamp", ""), reverse=True)

    st.markdown("### 📋 Latest Debates")

    for debate in debates[-15:][::-1]:  # Show the latest 15 debates
        timestamp = debate.get("timestamp", "Unknown Time")
        participants = debate.get("agents", [])
        votes = debate.get("votes", {})
        outcome = debate.get("outcome", "Undecided")

        with st.container():
            st.markdown(f"#### 🕒 {timestamp}")
            st.markdown(f"👥 **Participants:** {', '.join(participants) if participants else 'Unknown'}")
            st.markdown(f"🗳️ **Votes:** {votes if votes else 'No votes recorded.'}")
            st.markdown(f"🏆 **Final Decision:** **{outcome}**")
            st.markdown("---")

    st.success("✅ Internal debate tracking live and operational.")

# === End of File ===