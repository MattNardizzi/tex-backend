# ============================================================
# © 2025 VortexBlack LLC – All rights reserved.
# File: tools/reasoning_dashboard.py
# Purpose: Live Thought Stream Viewer for Tex Cognitive Reasoning
# ============================================================

import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime

# === File Path
REASONING_FILE = "memory_archive/reasoning_trace_log.jsonl"

# === Load Function
def load_reasoning_trace():
    if not os.path.exists(REASONING_FILE):
        return pd.DataFrame()

    try:
        with open(REASONING_FILE, "r") as f:
            data = [json.loads(line) for line in f if line.strip()]
        return pd.DataFrame(data)
    except Exception as e:
        st.error(f"❌ Failed to load reasoning trace: {e}")
        return pd.DataFrame()

# === Main Render Function
def render_reasoning_dashboard():
    st.markdown("## 🧠 Tex Live Thought Stream – Reasoning Trace")

    df = load_reasoning_trace()

    if df.empty:
        st.warning("⚠️ No reasoning trace data available yet.")
        return

    st.markdown("### 📖 Recent Cognitive Thoughts")

    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce', utc=True)
        df = df.dropna(subset=['timestamp'])
        df = df.sort_values('timestamp', ascending=False)

    agent_filter = None
    if 'agent' in df.columns:
        agent_options = df['agent'].dropna().unique().tolist()
        agent_filter = st.selectbox("🔍 Filter by Agent:", ["All"] + agent_options)

        if agent_filter != "All":
            df = df[df['agent'] == agent_filter]

    st.metric("💬 Total Thoughts Recorded", len(df))

    if 'thought' in df.columns:
        display_texts = []
        for _, row in df.iterrows():
            timestamp = row['timestamp'].strftime("%Y-%m-%d %H:%M:%S") if pd.notnull(row['timestamp']) else "Unknown Time"
            thought = row.get('thought', 'No Thought Recorded')
            display_texts.append(f"🧠 [{timestamp}] {thought}")

        st.text_area(
            label="🧠 Live Cognitive Reasoning",
            value="\n\n".join(display_texts),
            height=600,
            max_chars=None
        )
    else:
        st.warning("⚠️ No 'thought' field available in reasoning trace.")

    st.success("✅ Reasoning trace loaded and visualized.")