# ============================================================
# 📉 Tex: Finance Intelligence Dashboard — Strategic AGI Interface
# © 2025 VortexBlack LLC. All rights reserved.
# ============================================================

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

import streamlit as st

from tools.dashboards.core import (
    real_time_cognition_dashboard,
    reasoning_dashboard,
    internal_debate_dashboard,
    memory_dashboard,
    memory_recall_flash_dashboard,
    memory_weaver_dashboard,
    goal_dashboard,
    mutation_dashboard,
    aeondelta_dashboard,
    tex_child_001_dashboard,
    tex_child_002_dashboard,
    tex_child_003_dashboard,
    voice_feedback_dashboard,
    tex_breathing_cycle_dashboard
)

from tools.dashboards.finance import (
    market_awareness_dashboard,
    future_stream_dashboard,
    future_tree_dashboard,
    market_mood_sensor_dashboard,
    meta_coherence_memory_dashboard,
    persona_dashboard,
    command_console_dashboard,
    emotional_liquidity_engine_dashboard,
    portfolio_thinker_dashboard,
    market_strategy_driver_dashboard,
    alpha_explainer_dashboard,
    alpha_signal_fusion_dashboard,
    alpha_fusion_engine_dashboard,
    strategy_creator_dashboard,
    strategy_scoring_dashboard,
    strategy_variant_simulator_dashboard,
    cross_timeline_reconciler_dashboard,
    phase_transition_detector_dashboard
)

# === Setup
st.set_page_config(page_title="📉 Tex: Finance Intelligence Dashboard", page_icon="📉", layout="wide")

# === Memory to track current module
if "selected_module" not in st.session_state:
    st.session_state["selected_module"] = None
    st.session_state["selected_module"] = "📈 Market Awareness"

def select_module(module_label):
    st.session_state["selected_module"] = module_label

# === Top Header (Centered)
with st.container():
    st.markdown("""
        <div style='display: flex; justify-content: center; align-items: center; flex-direction: column; text-align: center; padding: 1rem 0 0 0;'>
            <h1 style='font-size: 42px;'>📉 <strong>Tex: Finance Intelligence Dashboard</strong></h1>
            <p style='font-size: 1.05em; color: #cccccc; margin-top: 0.5rem;'>
                AGI fusion for hedge funds, market cognition, and foresight strategy.
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# === Custom CSS
st.markdown("""
<style>
body {
    background-color: #0a0a0a;
}
.sidebar .sidebar-content {
    background-color: #0a0a0a;
}
h1, h2, h3, h4, h5, h6, p, div {
    color: white;
}
.stButton>button {
    background-color: #111111;
    color: white;
    border-radius: 10px;
    border: 1px solid #333333;
    padding: 0.5em 1em;
    font-size: 1em;
}
</style>
""", unsafe_allow_html=True)

# === Sidebar
st.sidebar.markdown("## 📉 Tex Financial Cortex")
st.sidebar.caption("Navigate cognition, forecasting, alpha strategies, and evolution.")
st.sidebar.markdown("---")

# === Module Mapping
module_map = {
    # Market Awareness
    "📈 Market Awareness": market_awareness_dashboard.render_market_awareness_dashboard,
    "🌳 Strategic Foresight Tree": future_tree_dashboard.render_future_tree_dashboard,
    "🌌 Parallel World Futures": future_stream_dashboard.render_future_stream_dashboard,
    "📊 Market Mood Sensor": market_mood_sensor_dashboard.render_market_mood_sensor_dashboard,

    # Cognition
    "🧠 Real-Time Cognition": real_time_cognition_dashboard.render_real_time_cognition_dashboard,
    "🧠 Reasoning Engine": reasoning_dashboard.render_reasoning_dashboard,
    "⚖️ Internal Debate": internal_debate_dashboard.render_internal_debate_dashboard,

    # Memory
    "🧠 Memory Dashboard": memory_dashboard.render_memory_dashboard,
    "📌 Memory Recall Flash": memory_recall_flash_dashboard.render_memory_recall_flash,
    "🪄 Memory Thread Weaver": memory_weaver_dashboard.render_memory_weaver_dashboard,
    "🔎 Meta-Coherence Memory": meta_coherence_memory_dashboard.render_meta_coherence_memory_dashboard,

    # Goals & Identity
    "🌟 Goal Dashboard": goal_dashboard.render_goal_dashboard,
    "🧬 Persona Engine": persona_dashboard.render_persona_dashboard,
    "🔹 Command Console": command_console_dashboard.render_command_console_dashboard,

    # Evolution
    "🧬 Mutation Monitor": mutation_dashboard.render_mutation_dashboard,
    "🧠 AeonDelta Core": aeondelta_dashboard.render_aeondelta_dashboard,
    "🥮 Tex Child 001": tex_child_001_dashboard.render_tex_child_001_dashboard,
    "🥮 Tex Child 002": tex_child_002_dashboard.render_tex_child_002_dashboard,
    "🥮 Tex Child 003": tex_child_003_dashboard.render_tex_child_003_dashboard,
    "🥸 Emotional Liquidity Engine": emotional_liquidity_engine_dashboard.render_emotional_liquidity_engine_dashboard,

    # Alpha Strategy
    "🏢 Portfolio Thinker": portfolio_thinker_dashboard.render_portfolio_thinker_dashboard,
    "👨‍🌐 Strategy Driver": market_strategy_driver_dashboard.render_market_strategy_driver_dashboard,
    "🎯 Alpha Explainer": alpha_explainer_dashboard.render_alpha_explainer_dashboard,
    "🔗 Alpha Signal Fusion": alpha_signal_fusion_dashboard.render_alpha_signal_fusion_dashboard,
    "🔄 Alpha Fusion Engine": alpha_fusion_engine_dashboard.render_alpha_fusion_engine_dashboard,
    "🌟 Strategy Creator": strategy_creator_dashboard.render_strategy_creator_dashboard,
    "⚖️ Strategy Scoring": strategy_scoring_dashboard.render_strategy_scoring_dashboard,
    "🌀 Strategy Variant Simulator": strategy_variant_simulator_dashboard.render_strategy_variant_simulator_dashboard,
    "🪡 Timeline Reconciler": cross_timeline_reconciler_dashboard.render_cross_timeline_reconciler_dashboard,
    "🔄 Phase Transition Detector": phase_transition_detector_dashboard.render_phase_transition_detector_dashboard,

    # Infrastructure
    "🫸 Breathing Monitor": tex_breathing_cycle_dashboard.render_breathing_cycle,
    "🎧 Voice Feedback": voice_feedback_dashboard.render_voice_feedback
}

# === Sidebar Menus
with st.sidebar.expander("📊 Market Intelligence"):
    for label in ["📈 Market Awareness", "🌳 Strategic Foresight Tree", "🌌 Parallel World Futures", "📊 Market Mood Sensor"]:
        if st.button(label):
            select_module(label)

with st.sidebar.expander("🧠 Cognitive Engine"):
    for label in ["🧠 Real-Time Cognition", "🧠 Reasoning Engine", "⚖️ Internal Debate"]:
        if st.button(label):
            select_module(label)

with st.sidebar.expander("🔍 Memory Intelligence"):
    for label in ["🧠 Memory Dashboard", "📌 Memory Recall Flash", "🪄 Memory Thread Weaver", "🔎 Meta-Coherence Memory"]:
        if st.button(label):
            select_module(label)

with st.sidebar.expander("🌟 Goals & Identity"):
    for label in ["🌟 Goal Dashboard", "🧬 Persona Engine", "🔹 Command Console"]:
        if st.button(label):
            select_module(label)

with st.sidebar.expander("🐎 Evolution"):
    for label in [
        "🧬 Mutation Monitor", "🧠 AeonDelta Core",
        "🥮 Tex Child 001", "🥮 Tex Child 002", "🥮 Tex Child 003",
        "🧸 Emotional Liquidity Engine"
    ]:
        if st.button(label):
            select_module(label)

with st.sidebar.expander("🏢 Alpha Strategy"):
    for label in [
        "🏢 Portfolio Thinker", "👨‍🌐 Strategy Driver", "🎯 Alpha Explainer",
        "🔗 Alpha Signal Fusion", "🔄 Alpha Fusion Engine",
        "🌟 Strategy Creator", "⚖️ Strategy Scoring", "🌀 Strategy Variant Simulator",
        "🪡 Timeline Reconciler", "🔄 Phase Transition Detector"
    ]:
        if st.button(label):
            select_module(label)

with st.sidebar.expander("🛠️ Core Infrastructure"):
    for label in ["🧨 Breathing Monitor", "🎧 Voice Feedback"]:
        if st.button(label):
            select_module(label)

# === Main Content
if st.session_state["selected_module"]:
    selected_fn = module_map[st.session_state["selected_module"]]
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        selected_fn()

# === Footer
st.sidebar.markdown("---")
st.sidebar.caption("📉 Tex AGI | VortexBlack 2025 — All Rights Reserved")
st.markdown("---")
st.caption("📉 Financial Cognition • 🧬 Mutation Intelligence • 🌌 Strategic Futures Engine")
