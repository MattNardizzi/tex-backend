# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain/future_forecaster.py
# Purpose: Extracted future simulation, causal prediction summary, and future response
# ============================================================

def simulate_futures(self):
    self.last_future_report = self.future_engine.predict_all_futures()


def generate_future_summary(self):
    if not self.last_future_report:
        return "My future pathways are still forming..."
    parts = []
    if 'future_trees' in self.last_future_report:
        for branch in self.last_future_report['future_trees']:
            parts.append(f"If {branch['cause']}, then {branch['effect']} (confidence {branch['confidence']})")
    if 'emotional_paths' in self.last_future_report:
        for emo in self.last_future_report['emotional_paths']:
            mutation = "(Mutation)" if emo['mutation_triggered'] else "(Stable)"
            parts.append(f"Emotion '{emo['emotion']}' may cause {emo['swarm_projection']} {mutation} [Confidence: {emo['confidence']}]")
    if 'causal_worlds' in self.last_future_report:
        for node in self.last_future_report['causal_worlds']:
            parts.append(f"Causal Path: {node['cause']} → {node['effect']}")
    if 'optimized_branches' in self.last_future_report:
        for opt in self.last_future_report['optimized_branches']:
            parts.append(f"Optimized: {opt['future_title']} [{opt['confidence']}]")
    if parts:
        return " | ".join(parts)
    else:
        return "Future possibilities are currently undefined."


def generate_future_response(self):
    try:
        self.simulate_futures()
        future_summary = self.generate_future_summary()
        return f"🔮 Future Forecast: {future_summary}"
    except Exception:
        return "🔮 Future simulation system stabilizing..."
