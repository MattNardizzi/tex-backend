# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: tools/real_time_cognition_dashboard.py
# Purpose: Tex Real-Time Cognitive Signal Fusion Viewer
# ============================================================

import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime

# === File Path
FUSION_FILE = "memory_archive/tex_signal_fusion.jsonl"

# === Load Function
def load_fusion_stream():
    if not os.path.exists(FUSION_FILE):
        return pd.DataFrame()

    try:
        with open(FUSION_FILE, "r") as f:
            lines = [json.loads(line) for line in f if line.strip()]
        if not lines:
            return pd.DataFrame()
        return pd.DataFrame(lines)
    except Exception as e:
        st.error(f"❌ Error loading fusion stream: {e}")
        return pd.DataFrame()

# === Main Render Function
def render_real_time_cognition_dashboard():
    st.markdown("## 🔁 Real-Time Cognitive Fusion Stream")

    df = load_fusion_stream()

    if df.empty:
        st.warning("⚠️ No real-time cognition data available yet.")
        return

    # === Signal Metrics
    st.markdown("### 📡 Signal Metrics")

    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce', utc=True)
        df = df.dropna(subset=['timestamp'])
        df = df.sort_values('timestamp', ascending=False)

    signal_count = len(df)
    st.metric("📡 Signals Captured", signal_count)

    # === Main View
    st.markdown("### 📖 Latest Cognitive Signals")

    if {'timestamp', 'source', 'title', 'urgency', 'confidence'}.issubset(df.columns):
        st.dataframe(
            df[['timestamp', 'source', 'title', 'urgency', 'confidence']].fillna("N/A"),
            use_container_width=True
        )
    else:
        st.warning("⚠️ Missing expected columns in signal fusion data.")

    st.markdown("---")

    # === Visualization
    st.markdown("### 📊 Urgency vs Confidence Map")
    if {'urgency', 'confidence'}.issubset(df.columns):
        st.scatter_chart(df[['urgency', 'confidence']])

    st.success("✅ Live cognition stream updated and running.")