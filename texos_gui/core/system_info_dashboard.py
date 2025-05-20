# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: tools/system_info_dashboard.py
# Purpose: Tex AGI System Overview Dashboard
# ============================================================

import streamlit as st
from datetime import datetime
import platform
import psutil

# === Main Render Function
def render_system_info_dashboard():
    st.markdown("## ⚙️ Tex System Info — Runtime Metrics")

    # === System Specifications
    st.markdown("### 🖥️ System Specifications")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("OS", platform.system())
        st.metric("Machine", platform.machine())
        st.metric("Processor", platform.processor())
    with col2:
        st.metric("Python Version", platform.python_version())
        st.metric("CPU Cores", psutil.cpu_count(logical=True))
        st.metric("Memory (RAM)", f"{round(psutil.virtual_memory().total / 1e9, 2)} GB")

    st.markdown("---")

    # === Runtime Environment Metrics
    st.markdown("### 📈 Runtime Environment Status")
    memory = psutil.virtual_memory()
    st.metric("Memory Usage", f"{memory.percent}% used")

    cpu = psutil.cpu_percent(interval=1)
    st.metric("CPU Usage", f"{cpu}% load")

    boot_time = datetime.utcfromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S UTC")
    st.metric("System Boot Time", boot_time)

    st.markdown("---")

    # === Tex Core Information
    st.markdown("### 🧠 Tex Core Meta")
    st.markdown("**Version:** `v2.0.0 – Full Cognition + Evolution Layer`")
    st.markdown("**Status:** ✅ Cognitive Engine Online")
    st.markdown("**Components Running:** Cognition Loop, Mutation Engine, Swarm Spawning, Memory Drift Tracking")
    st.markdown(f"**Time Now (UTC):** {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}")

    st.success("✅ System metrics loaded successfully.")