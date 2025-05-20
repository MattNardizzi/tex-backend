# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: texos_gui/command_console.py
# Purpose: Human-in-the-loop command console for Tex AGI
# ============================================================
import os
import streamlit as st
import json
from datetime import datetime, timezone

GOAL_FILE = "memory_archive/autonomous_goals.jsonl"
PAUSE_FILE = "memory_archive/pause_flag.json"

st.set_page_config(page_title="🧠 Tex Command Console", layout="wide")
st.title("🧠 Tex Command Console")
st.subheader("Human-in-the-loop override + live intervention tools")

# === Inject New Goal
st.markdown("### 🎯 Inject a New Goal")
new_goal = st.text_input("New Goal Description")
if st.button("Submit Goal"):
    if new_goal.strip():
        goal_obj = {
            "goal": new_goal.strip(),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "origin": "manual"
        }
        with open(GOAL_FILE, "a") as f:
            f.write(json.dumps(goal_obj) + "\n")
        st.success("✅ Goal injected into Tex.")

# === Pause / Resume Cognition
st.markdown("### ⏸ Pause or Resume Cognition")
pause_state = False
if os.path.exists(PAUSE_FILE):
    with open(PAUSE_FILE, "r") as f:
        pause_state = json.load(f).get("paused", False)

toggle = st.checkbox("Pause Cognitive Loop", value=pause_state)
if toggle != pause_state:
    with open(PAUSE_FILE, "w") as f:
        json.dump({"paused": toggle}, f)
    st.success(f"🧠 Tex cognition {'paused' if toggle else 'resumed'}.")

# === Force Mutation (Override Trigger)
st.markdown("### 🧬 Force Mutation")
if st.button("Trigger Self-Mutation"):
    mutation_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": "manual_override",
        "reason": "manual_trigger",
        "details": "Mutation manually triggered via GUI"
    }
    with open("memory_archive/mutation_history.log", "a") as f:
        f.write(json.dumps(mutation_entry) + "\n")
    st.success("⚠️ Mutation event recorded. Tex will mutate next cycle.")

# === Clear All Goals
st.markdown("### 🧹 Clear All Current Goals")
if st.button("Clear Goals"):
    open(GOAL_FILE, "w").close()
    st.success("🚮 All autonomous goals cleared.")

# === Inject Operator Commentary
st.markdown("### 💬 Operator Commentary")
comment = st.text_area("Add a log/commentary message to memory")
if st.button("Log Message"):
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "operator_note": comment,
        "type": "operator_log"
    }
    with open("memory_archive/reasoning_trace_log.jsonl", "a") as f:
        f.write(json.dumps(entry) + "\n")
    st.success("📥 Commentary saved to reasoning trace.")