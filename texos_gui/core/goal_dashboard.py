# ============================================================
# © 2025 VortexBlack LLC – All rights reserved.
# File: tools/goal_dashboard.py
# Purpose: Tex Autonomous Goal Tracker + Manager
# ============================================================

import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime

# === File Path
GOAL_FILE = "memory_archive/autonomous_goals.jsonl"

# === Load / Save Functions
def load_goals():
    if not os.path.exists(GOAL_FILE):
        return []
    with open(GOAL_FILE, "r") as f:
        return [json.loads(line) for line in f if line.strip()]

def save_goals(goal_list):
    with open(GOAL_FILE, "w") as f:
        for goal in goal_list:
            f.write(json.dumps(goal) + "\n")

# === Main Render Function
def render_goal_dashboard():
    st.markdown("## 🎯 Tex Autonomous Goals — Live Cognitive Mission Feed")

    goal_data = load_goals()
    remaining_goals = []

    if not goal_data:
        st.info("⚡ No active goals at the moment.")
    else:
        st.markdown("### 🧠 Active Goal List")

        for i, goal in enumerate(goal_data):
            col1, col2 = st.columns([8, 1])
            with col1:
                st.markdown(f"- **{goal.get('goal', 'Unnamed Goal')}**")
                st.caption(
                    f"Origin: {goal.get('origin', 'unknown')} | "
                    f"Priority: {goal.get('priority', 'normal')} | "
                    f"Timestamp: {goal.get('timestamp', '-')}"
                )
            with col2:
                if st.checkbox("✅ Complete", key=i):
                    st.success(f"✅ Marked complete: {goal.get('goal', '')}")
                else:
                    remaining_goals.append(goal)

        # Update file if any goals were marked complete
        if len(remaining_goals) < len(goal_data):
            save_goals(remaining_goals)
            st.rerun()

    # === Metrics Section
    st.markdown("---")
    st.markdown("### 📊 Goal Metrics Overview")
    st.metric("📋 Total Goals", len(goal_data))
    st.metric("🚀 Remaining Goals", len(remaining_goals))
    st.metric("🔥 High Priority", sum(1 for g in goal_data if g.get("priority") == "high"))

    st.markdown("---")
    st.caption("⏱️ Last Updated: " + datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"))
    if st.button("🔄 Manual Refresh"):
        st.rerun()