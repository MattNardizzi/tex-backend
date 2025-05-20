# ============================================================
# 💹 Tex: Finance Intelligence Dashboard — Strategic AGI Interface
# © 2025 VortexBlack LLC. All rights reserved.
# ============================================================

import sys
import os
sys.path.append(os.path.abspath("."))

import streamlit as st

from tools.finance import (
    market_awareness_dashboard,
    future_stream_dashboard,
    future_tree_dashboard,
    command_console_dashboard
)

from tools.core import (
    real_time_cognition_dashboard,
    reasoning_dashboard,
    memory_dashboard,
    mutation_dashboard,
    aeondelta_dashboard,
    tex_breathing_cycle_dashboard,
    voice_feedback_dashboard,
    internal_debate_dashboard,
    memory_recall_flash_dashboard
)

st.set_page_config(page_title="💹 Tex: Finance Intelligence Dashboard", page_icon="💹", layout="wide")

# === Style
st.markdown("""
    <style>
        html, body, .stApp, section.main > div {
            background-color: #000000 !important;
        }
        h1, h2, h3, h4, h5, h6, p, div {
            color: white !important;
        }
        .stButton>button {
            background-color: #111111;
            color: white;
            border-radius: 10px;
            border: 1px solid #333333;
            padding: 0.5em 1em;
            font-size: 1em;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# === Module Selector
if "selected_module" not in st.session_state:
    st.session_state["selected_module"] = None

def select_module(module_label):
    st.session_state["selected_module"] = module_label

# === Header
with st.container():
    st.markdown("""
        <div style='text-align: center; padding: 1rem 0;'>
            <h1 style='font-size: 42px;'>💹 <strong>Tex: Finance Intelligence Dashboard</strong></h1>
            <p style='font-size: 1.05em; color: #cccccc;'>
                Cognitive AGI fusion for hedge funds, volatility tracking, and market strategy.
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# === Sidebar
st.sidebar.markdown("## 💹 Tex Financial Cortex")
st.sidebar.caption("Navigate Tex’s financial reasoning, volatility response, and foresight loops.")
st.sidebar.markdown("---")

# === Module Map
module_map = {
    # Market Intelligence
    "📈 Market Awareness": market_awareness_dashboard.render_market_awareness_dashboard,
    "🌳 Strategic Foresight Tree": future_tree_dashboard.render_future_tree_dashboard,
    "🌌 Parallel World Futures": future_stream_dashboard.render_future_stream_dashboard,

    # Cognitive Engine
    "🧠 Real-Time Cognition": real_time_cognition_dashboard.render_real_time_cognition_dashboard,
    "🧠 Reasoning Engine": reasoning_dashboard.render_reasoning_dashboard,
    "⚖️ Internal Debate": internal_debate_dashboard.render_internal_debate_dashboard,

    # Memory Systems
    "🧠 Memory Dashboard": memory_dashboard.render_memory_dashboard,
    "📌 Memory Recall Flash": memory_recall_flash_dashboard.render_memory_recall_flash,

    # Evolution & Mutation
    "🧬 Mutation Monitor": mutation_dashboard.render_mutation_dashboard,
    "🧠 AeonDelta Core": aeondelta_dashboard.render_aeondelta_dashboard,

    # Infrastructure
    "🔹 Command Console": command_console_dashboard.render_command_console_dashboard,
    "🪱 Breathing Monitor": tex_breathing_cycle_dashboard.render_breathing_cycle,
    "🎧 Voice Feedback": voice_feedback_dashboard.render_voice_feedback
}

# === Sector Layered Navigation
with st.sidebar.expander("📊 Market Intelligence"):
    for label in ["📈 Market Awareness", "🌳 Strategic Foresight Tree", "🌌 Parallel World Futures"]:
        if st.button(label):
            select_module(label)

with st.sidebar.expander("🧠 AGI Cognitive Engine"):
    for label in ["🧠 Real-Time Cognition", "🧠 Reasoning Engine", "⚖️ Internal Debate"]:
        if st.button(label):
            select_module(label)

with st.sidebar.expander("🧠 Memory Systems"):
    for label in ["🧠 Memory Dashboard", "📌 Memory Recall Flash"]:
        if st.button(label):
            select_module(label)

with st.sidebar.expander("🧬 Evolution & Mutation"):
    for label in ["🧬 Mutation Monitor", "🧠 AeonDelta Core"]:
        if st.button(label):
            select_module(label)

with st.sidebar.expander("🚰 Infrastructure"):
    for label in ["🔹 Command Console", "🪱 Breathing Monitor", "🎧 Voice Feedback"]:
        if st.button(label):
            select_module(label)

# === Main Viewer
if st.session_state["selected_module"]:
    selected_fn = module_map[st.session_state["selected_module"]]
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        selected_fn()

# === Footer
st.sidebar.markdown("---")
st.sidebar.caption("🧠 Tex AGI | VortexBlack 2025 — All Rights Reserved")
st.markdown("---")
st.caption("💹 Financial Cognition • 🔁 Strategic Volatility Engine • 🧬 Recursive Forecast Network")