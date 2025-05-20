# ============================================================
# 🧵 Memory Weaver Dashboard — Tex AGI Narrative Thread Visualizer
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# ============================================================

import streamlit as st
from core_layer.memory_weaver import weave_narrative_threads

def render_memory_weaver_dashboard():
    st.markdown("## 🧵 Tex: Memory Weaver")
    st.caption("Cognitive threading of memory fragments into coherent narratives.")

    with st.spinner("Weaving memory threads..."):
        threads = weave_narrative_threads()

    if not threads:
        st.warning("No memory threads found.")
        return

    for thread in threads:
        st.markdown(f"### 🧠 {thread['thread_id']}")
        for entry in thread["entries"]:
            st.markdown(f"- `{entry['timestamp']}` — {entry['text']}")