import streamlit as st
import pandas as pd
import json
from pathlib import Path

def render_mutation_lineage_dashboard():
    st.markdown("### 🧬 Mutation Lineage Tracker")
    st.caption("Visualizing Tex’s mutation ancestry across AGI cognition cycles.")

    # Load from memory archive
    log_path = Path("memory_archive/mutation_history.jsonl")
    
    if not log_path.exists():
        st.warning("No mutation history found.")
        return

    mutations = []
    with open(log_path, "r") as f:
        for line in f:
            try:
                mutations.append(json.loads(line))
            except:
                continue

    if not mutations:
        st.info("No mutation entries to display yet.")
        return

    df = pd.DataFrame(mutations)

    # Display recent 25 mutations sorted by latest
    df = df.sort_values(by="timestamp", ascending=False).head(25)
    
    st.dataframe(df[[
        "cycle", "parent_agent", "mutation_type", "status", "hash", "timestamp"
    ]], use_container_width=True)

    # Optional: Trend summary
    recent_status = df["status"].value_counts()
    st.markdown("### 📊 Mutation Status Summary")
    st.write(recent_status.to_dict())