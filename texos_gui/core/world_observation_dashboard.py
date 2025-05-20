# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: tools/world_observation_dashboard.py
# Purpose: Tex World Observation Stream — Real-Time Awareness Feed
# ============================================================

import streamlit as st
import os
import json
import pandas as pd
from datetime import datetime

# === File Path
WORLD_FILE = "memory_archive/world_observations.jsonl"

# === Load Function
def load_world_observations():
    if not os.path.exists(WORLD_FILE):
        return pd.DataFrame()

    try:
        with open(WORLD_FILE, "r") as f:
            lines = [json.loads(line) for line in f if line.strip()]
        df = pd.DataFrame(lines)
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
            df = df.dropna(subset=['timestamp'])
            df = df.sort_values("timestamp", ascending=False)
        return df
    except Exception as e:
        st.error(f"❌ Failed to load world observations: {e}")
        return pd.DataFrame()

# === Main Render Function
def render_world_observation_dashboard():
    st.markdown("## 🌍 Tex World Observation Stream – Real-Time Perception Feed")

    df = load_world_observations()

    if df.empty:
        st.warning("⚠️ No external observations detected yet.")
        return

    st.metric("🌐 Observations Logged", len(df))

    st.markdown("---")

    st.markdown("### 🌐 Live Observation Feed")

    for idx, row in df.iterrows():
        timestamp = row.get('timestamp', 'Unknown Timestamp')
        observation = row.get('observation', 'No detail.')
        priority = row.get('priority', 'N/A')

        st.markdown(f"**🕒 {timestamp}**")
        st.markdown(f"🔍 {observation}")
        st.caption(f"⚡ Priority: {priority}")
        st.markdown("---")

    # Quick Summary Table
    st.markdown("### 📋 Recent Observations Log (Top 20)")
    if {'timestamp', 'observation', 'priority'}.issubset(df.columns):
        st.dataframe(df[['timestamp', 'observation', 'priority']].head(20), use_container_width=True)

    st.success("✅ World observation feed active and operational.")