# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: tools/memory_recall_flash_dashboard.py
# Purpose: Live Streamlit Dashboard for Tex’s Memory Recalls
# ============================================================

import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime

# === File Path
RECALL_FILE = "memory_archive/memory_recall_log.jsonl"

# === Load Function
def load_memory_recalls():
    if not os.path.exists(RECALL_FILE):
        return pd.DataFrame()

    try:
        with open(RECALL_FILE, "r") as f:
            lines = [json.loads(line) for line in f if line.strip()]
        df = pd.DataFrame(lines)
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
            df = df.dropna(subset=['timestamp'])
            df = df.sort_values('timestamp', ascending=False)
        return df
    except Exception as e:
        st.error(f"❌ Failed to load memory recalls: {e}")
        return pd.DataFrame()

# === Main Render Function
def render_memory_recall_flash():
    st.markdown("## ⚡ Tex Memory Recall – Flash Stream")
    st.caption("Every time Tex recalls a memory, it flashes here in real-time.")

    df = load_memory_recalls()

    if df.empty:
        st.warning("⚠️ No memory recalls found yet.")
        return

    st.markdown("### 📖 Latest Memory Recalls")

    for _, row in df.iterrows():
        memory_text = row.get('memory', 'Unknown Memory')
        timestamp = row.get('timestamp', 'Unknown Time')

        st.markdown(f"**🧠 Memory:** {memory_text}")
        st.caption(f"🕰️ {timestamp}")
        st.markdown("---")

    st.success("✅ Memory recall flash feed active.")