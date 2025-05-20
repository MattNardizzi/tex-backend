# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: tools/memory_dashboard.py
# Purpose: Modular Tex AGI Memory Log Visualizer (for import)
# ============================================================

import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime

# === File Path
MEMORY_FILE = "logs/voice_memory.json"

# === Load Function
def load_memory_log():
    if not os.path.exists(MEMORY_FILE):
        return pd.DataFrame()

    try:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
        if isinstance(data, list):
            return pd.DataFrame(data)
        return pd.DataFrame()
    except Exception as e:
        st.error(f"❌ Failed to load memory: {e}")
        return pd.DataFrame()

# === Main Render Function
def render_memory_dashboard():
    st.markdown("## 🧠 Tex Memory Feed — Live Cognitive Stream")

    df = load_memory_log()

    if df.empty:
        st.warning("⚠️ No memory logs available.")
        return

    # === Filters
    if 'agent' in df.columns:
        agent_options = df['agent'].dropna().unique().tolist()
        selected_agent = st.selectbox("🔍 Filter by Agent", ["All"] + agent_options)

        if selected_agent != "All":
            df = df[df['agent'] == selected_agent]

    st.metric("🧠 Total Memory Entries", len(df))

    st.markdown("---")

    # === Timestamp Formatting
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        df = df.dropna(subset=['timestamp'])
        df = df.sort_values('timestamp', ascending=False)

    # === Display Memory Table
    st.markdown("### 📖 Recent Memory Events")
    if {'timestamp', 'agent', 'data'}.issubset(df.columns):
        st.dataframe(df[['timestamp', 'agent', 'data']].fillna("N/A"), use_container_width=True)
    else:
        st.warning("⚠️ Required columns missing from memory log.")

    st.markdown("---")

    # === Agent Event Chart
    if 'agent' in df.columns:
        st.markdown("### 📊 Memory Events by Agent")
        agent_counts = df['agent'].value_counts()
        st.bar_chart(agent_counts)

    st.success("✅ Memory dashboard loaded successfully.")