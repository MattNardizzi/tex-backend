# ============================================================
# Tex Cognition Plotter – Visualization Engine
# ============================================================

import plotly.graph_objs as go
import pandas as pd
from pathlib import Path

def load_cognition_data():
    path = Path("agentic_ai/tex_operator_sync.txt")
    if not path.exists():
        return pd.DataFrame()
    
    lines = path.read_text().splitlines()
    data = []
    for line in lines:
        if "Live Summary" in line:
            try:
                parts = eval(line.split(": ", 1)[-1].split("@")[0].strip())
                data.append(parts)
            except:
                continue
    return pd.DataFrame(data)

def plot_emotion_trajectory(df):
    if df.empty: return None
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=df['urgency'], name='Urgency', line=dict(color='red')))
    fig.add_trace(go.Scatter(y=df['coherence'], name='Coherence', line=dict(color='green')))
    fig.update_layout(title='🧠 Cognitive Trajectory', xaxis_title='Cycle', yaxis_title='Score')
    return fig
