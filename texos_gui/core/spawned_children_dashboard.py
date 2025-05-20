# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: tools/spawned_children_dashboard.py
# Purpose: Real-Time Tracker for Spawned Tex Children Agents
# ============================================================

import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime

# === File Path
SPAWN_FILE = "memory_archive/child_spawn_log.jsonl"

# === Load Function
def load_spawned_children():
    if not os.path.exists(SPAWN_FILE):
        return pd.DataFrame()

    try:
        with open(SPAWN_FILE, "r") as f:
            entries = [json.loads(line) for line in f if line.strip()]
        df = pd.DataFrame(entries)
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce', utc=True)
            df = df.dropna(subset=['timestamp'])
            df = df.sort_values('timestamp', ascending=False)
        return df
    except Exception as e:
        st.error(f"❌ Failed to load spawned children: {e}")
        return pd.DataFrame()

# === Main Render Function
def render_spawned_children_dashboard():
    st.markdown("## 👶 Spawned Tex Children Tracker")
    st.caption("Live feed of all autonomous child agents Tex has spawned.")

    df = load_spawned_children()

    if df.empty:
        st.warning("⚠️ No child spawn records found yet.")
        return

    st.markdown("### 📋 Child Agents Log")

    # Safe column detection
    display_cols = []
    if 'child_id' in df.columns:
        display_cols.append('child_id')
    if 'strategy' in df.columns:
        display_cols.append('strategy')
    if 'archetype' in df.columns:
        display_cols.append('archetype')
    if 'traits' in df.columns:
        display_cols.append('traits')
    if 'timestamp' in df.columns:
        display_cols.append('timestamp')

    if display_cols:
        st.dataframe(df[display_cols].fillna("N/A"), use_container_width=True)
    else:
        st.warning("⚠️ No expected columns found in child spawn data.")

    st.success("✅ Child agent tracking live and operational.")