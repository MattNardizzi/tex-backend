# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: tools/emotion_pulse_dashboard.py
# Purpose: Live Cognitive Pulse Metrics – Urgency, Risk, Coherence
# ============================================================

import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime

# === File Path
PULSE_FILE = "memory_archive/awareness_net.jsonl"

# === Load Function
def load_emotion_pulse():
    if not os.path.exists(PULSE_FILE):
        return pd.DataFrame()

    try:
        with open(PULSE_FILE, "r") as f:
            lines = [json.loads(line) for line in f if line.strip()]
        df = pd.DataFrame(lines)
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
            df = df.dropna(subset=['timestamp'])
            df = df.sort_values('timestamp', ascending=False)
        return df
    except Exception as e:
        st.error(f"❌ Failed to load emotion pulse: {e}")
        return pd.DataFrame()

# === Main Render Function
def render_emotion_pulse_dashboard():
    st.markdown("## 🫀 Tex Emotion Pulse Monitor – Live Metrics")
    st.caption("Track Tex's live evolving urgency, risk appetite, and coherence across thought cycles.")

    df = load_emotion_pulse()

    if df.empty:
        st.warning("⚠️ No awareness data found yet.")
        return

    latest = df.iloc[0]  # Most recent entry

    urgency = latest.get('urgency', 0)
    coherence = latest.get('coherence', 0)
    risk_appetite = round(1 - float(coherence), 2)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("⚡ Urgency Level", f"{urgency*100:.1f}%")

    with col2:
        st.metric("🎯 Risk Appetite", f"{risk_appetite*100:.1f}%")

    with col3:
        st.metric("🧠 Coherence Stability", f"{coherence*100:.1f}%")

    st.markdown("---")

    # Optional: Line chart for historical pulse
    if len(df) > 1:
        st.markdown("### 📈 Cognitive Stability Over Time")
        pulse_df = df[['timestamp', 'urgency', 'coherence']].set_index('timestamp')
        st.line_chart(pulse_df)

    st.success("✅ Pulse monitoring updated successfully.")