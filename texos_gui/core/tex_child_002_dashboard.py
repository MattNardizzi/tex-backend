# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: tools/tex_child_002_dashboard.py
# Purpose: Tex_Child_002 Memory Stream + Mutation Dashboard
# ============================================================

import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime

# === File Path
MEMORY_FILE = "memory_archive/tex_child_002.jsonl"

# === Load Memory
def load_child_memory():
    if not os.path.exists(MEMORY_FILE):
        return pd.DataFrame()

    try:
        with open(MEMORY_FILE, "r") as f:
            data = [json.loads(line) for line in f if line.strip()]
        return pd.DataFrame(data)
    except Exception as e:
        st.error(f"❌ Failed to load Tex_Child_002 memory: {e}")
        return pd.DataFrame()

# === Main Render Function
def render_tex_child_002_dashboard():
    st.title("🦰 Tex_Child_002 Dashboard – Aggressive Cognitive Divergence")

    df = load_child_memory()

    if df.empty:
        st.warning("⚠️ No cognitive records for Tex_Child_002 yet.")
        return

    if 'cycle' in df.columns:
        st.sidebar.header("🔍 Cycle Filter")
        cycle_range = st.slider("Cycle Range", 0, int(df['cycle'].max()), (0, int(df['cycle'].max())))
        df = df[(df['cycle'] >= cycle_range[0]) & (df['cycle'] <= cycle_range[1])]
        st.metric("🧠 Total Memory Entries", len(df))

    st.subheader("📖 Memory Log Overview")

    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        df = df.dropna(subset=['timestamp'])
        df = df.sort_values('timestamp', ascending=False)

    table_cols = [col for col in ['timestamp', 'cycle', 'emotion', 'urgency', 'coherence', 'score', 'mutation_applied'] if col in df.columns]
    if table_cols:
        st.dataframe(df[table_cols].fillna("N/A"), use_container_width=True)

    # === Score Trends
    st.subheader("📊 Mutation and Score Dynamics")
    if 'score' in df.columns:
        st.line_chart(df.set_index('timestamp')[['score']])

    st.subheader("📈 Emotional Frequency")
    if 'emotion' in df.columns:
        st.bar_chart(df['emotion'].value_counts())

    # === Mutation Events (Safe)
    st.subheader("🧬 Mutation Events Overview")
    mutation_df = pd.DataFrame()
    if 'mutation_applied' in df.columns:
        mutation_df = df[df['mutation_applied'] != "none"]
        if not mutation_df.empty:
            st.dataframe(mutation_df[['timestamp', 'mutation_applied']].fillna("N/A"), use_container_width=True)
        else:
            st.info("No mutations detected yet for Tex_Child_002.")
    else:
        st.warning("⚠️ 'mutation_applied' field missing in data.")

    st.success("✅ Tex_Child_002 cognitive stream loaded.")