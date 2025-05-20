# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# License: Private Intellectual Property – Not for distribution.
# ============================================================
# Tex Dashboard – Live Cognitive Awareness Panel
# ============================================================

import streamlit as st
import time
from pathlib import Path

# === Page Setup
st.set_page_config(page_title="Tex AGI Dashboard", layout="wide")
st.title("🧠 Tex AGI Dashboard – Live Cognitive Awareness")

# === Awareness Sync Log Path
log_file = Path("agentic_ai/tex_operator_sync.txt")

# === Display Live Thought Stream
st.subheader("🔁 Live Thought Stream (Last 10 Cycles)")

if log_file.exists():
    lines = log_file.read_text().splitlines()
    if lines:
        recent = lines[-10:]
        for line in recent:
            st.markdown(f"- `{line}`")
    else:
        st.warning("No cognitive data yet... Tex is initializing.")
else:
    st.info("📡 Waiting for Tex to register awareness...")

# === Auto-refresh
st.markdown("⏳ Refreshing every 5 seconds...")
time.sleep(5)
st.experimental_rerun()
# === Cognitive State Evolution Plot
from agentic_ai.cognition_plotter import load_cognition_data, plot_emotion_trajectory

st.markdown("---")
st.subheader("📊 Cognitive State Evolution")

df = load_cognition_data()
fig = plot_emotion_trajectory(df)

if fig:
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("⚠️ No cognitive summary data yet.")