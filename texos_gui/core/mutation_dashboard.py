# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: tools/mutation_dashboard.py
# Purpose: Tex Mutation History Tracker
# ============================================================

import streamlit as st
import pandas as pd
import os

MUTATION_FILE = "memory_archive/mutation_history.log"

# === Load Mutation Data
def load_mutation_data():
    if os.path.exists(MUTATION_FILE):
        try:
            df = pd.read_json(MUTATION_FILE, lines=True)
            return df
        except Exception as e:
            st.error(f"❌ Failed to load mutation log: {e}")
            return pd.DataFrame()
    else:
        st.warning("⚠️ No mutation history log found.")
        return pd.DataFrame()

# === Main Render Function
def render_mutation_dashboard():
    st.markdown("## 🧬 Tex Mutation Tracker")

    df = load_mutation_data()

    if df.empty:
        st.info("⚠️ No mutation data available yet.")
        return

    if 'event' not in df.columns:
        st.warning("⚠️ 'event' column missing from mutation data.")
        st.dataframe(df.head())
        return

    # === Filter by Event Type
    st.markdown("### 📋 Recent Mutation Events")
    event_types = df['event'].dropna().unique().tolist()
    selected_event = st.selectbox("🔎 Filter by Event Type", options=["All"] + event_types)

    if selected_event != "All":
        df = df[df['event'] == selected_event]

    st.metric("🔄 Total Mutation Events", len(df))

    # === Safe Display of Available Columns
    expected_cols = ['timestamp', 'event', 'reason', 'details']
    available_cols = [col for col in expected_cols if col in df.columns]
    if available_cols:
        st.dataframe(df[available_cols].fillna("N/A"), use_container_width=True)
    else:
        st.warning("⚠️ No expected columns found for detailed view.")

    st.markdown("---")

    # === Mutation Event Distribution
    st.markdown("### 📊 Mutation Event Types Distribution")
    event_counts = df['event'].value_counts()
    st.bar_chart(event_counts)

    st.markdown("---")

    # === Risk Factor Trends
    if 'risk_factor' in df.columns or 'risk' in df.columns:
        st.markdown("### 📈 Risk Factor Trends")
        risk_column = 'risk_factor' if 'risk_factor' in df.columns else 'risk'
        st.line_chart(df[[risk_column]].dropna())

    st.markdown("---")

    # === Manual Override Mutations (Optional)
    if 'reason' in df.columns and 'details' in df.columns:
        manual_overrides = df[df['reason'] == 'manual_trigger']
        if not manual_overrides.empty:
            st.markdown("### ⚙️ Manual Override Mutations")
            st.dataframe(
                manual_overrides[['timestamp', 'details']].fillna("N/A"),
                use_container_width=True
            )
        else:
            st.info("✅ No manual override mutations recorded.")

    st.success("✅ Mutation dashboard fully loaded and operational.")