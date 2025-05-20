# ============================================================
# © 2025 VortexBlack LLC – All rights reserved.
# File: tools/tex_child_001_dashboard.py
# Purpose: Tex_Child_001 Cognitive Stream and Mutation Monitor
# ============================================================

import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime

# === File Path
MEMORY_FILE = "memory_archive/tex_child_001.jsonl"

# === Load Memory
def load_child_memory():
    if not os.path.exists(MEMORY_FILE):
        return pd.DataFrame()

    try:
        with open(MEMORY_FILE, "r") as f:
            data = [json.loads(line) for line in f if line.strip()]
        return pd.DataFrame(data)
    except Exception as e:
        st.error(f"❌ Failed to load Tex_Child_001 memory: {e}")
        return pd.DataFrame()

# === Main Render Function
def render_tex_child_001_dashboard():
    st.title("👶 Tex_Child_001 Dashboard – Cognitive Divergence Viewer")

    df = load_child_memory()

    if df.empty:
        st.warning("⚠️ No cognitive memory for Tex_Child_001 yet.")
        return

    # === Sidebar Filters
    with st.sidebar:
        st.header("🔍 Child 001 Filters")
        cycle_range = st.slider("Cycle Range", 0, int(df['cycle'].max()), (0, int(df['cycle'].max())))
        df = df[(df['cycle'] >= cycle_range[0]) & (df['cycle'] <= cycle_range[1])]
        st.metric("🧠 Total Memory Events", len(df))

    # === Table View
    st.subheader("📖 Memory Log")

    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        df = df.dropna(subset=['timestamp'])
        df = df.sort_values('timestamp', ascending=False)

    st.dataframe(df[['timestamp', 'cycle', 'emotion', 'urgency', 'coherence', 'score', 'mutation_applied']].fillna("N/A"), use_container_width=True)

    # === Emotional Drift Visualization
    st.subheader("📈 Emotional Drift Over Time")
    if 'emotion' in df.columns and 'timestamp' in df.columns:
        emotion_counts = df['emotion'].value_counts()
        st.bar_chart(emotion_counts)

    # === Score Trends
    st.subheader("📉 Cognitive Score Dynamics")
    if 'score' in df.columns:
        st.line_chart(df[['timestamp', 'score']].set_index('timestamp'))

    # === Mutation Events
    st.subheader("🧬 Mutation Trigger History")
    mutation_df = df[df['mutation_applied'] != "none"]
    if not mutation_df.empty:
        st.dataframe(mutation_df[['timestamp', 'mutation_applied']], use_container_width=True)
    else:
        st.info("No forced mutations recorded yet.")

    st.success("✅ Tex_Child_001 cognitive stream loaded.")