# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: tools/thought_stream_dashboard.py
# Purpose: Real-Time Live Thought Stream of Tex Cognitive Outputs
# ============================================================

import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime

# === File Path
THOUGHT_STREAM_FILE = "memory_archive/reasoning_trace_log.jsonl"

# === Load Function
def load_thought_stream():
    if not os.path.exists(THOUGHT_STREAM_FILE):
        return pd.DataFrame()

    try:
        with open(THOUGHT_STREAM_FILE, "r") as f:
            lines = [json.loads(line) for line in f if line.strip()]
        df = pd.DataFrame(lines)
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
            df = df.dropna(subset=['timestamp'])
            df = df.sort_values('timestamp', ascending=False)
        return df
    except Exception as e:
        st.error(f"❌ Error loading thought stream: {e}")
        return pd.DataFrame()

# === Main Render Function
def render_thought_stream_dashboard():
    st.markdown("## 🔁 Tex Thought Stream – Real-Time Cognitive Reflection")
    st.caption("Live reasoning threads flowing directly from Tex's cognition core. Newest at the top.")

    df = load_thought_stream()

    if df.empty:
        st.warning("⚠️ No cognitive thoughts recorded yet.")
        return

    st.markdown("### 🧠 Thought Stream Timeline")

    if 'urgency' in df.columns:
        min_urgency = st.slider("🔍 Minimum Urgency Level", 0.0, 1.0, 0.0, 0.05)
        df = df[df['urgency'] >= min_urgency]

    st.metric("💬 Total Recorded Thoughts", len(df))

    st.markdown("---")

    for idx, row in df.iterrows():
        ts = row.get('timestamp', 'Unknown Time')
        thought = row.get('thought', row.get('reasoning', 'No thought recorded.'))
        urgency = row.get('urgency', "N/A")
        coherence = row.get('coherence', "N/A")

        st.markdown(f"**🕓 {ts}**")
        st.markdown(f"> {thought}")
        st.caption(f"Urgency: {urgency} | Coherence: {coherence}")
        st.markdown("---")

    st.success("✅ Live thought stream loaded successfully.")