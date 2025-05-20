import streamlit as st
import os
import json

def render_voice_feedback():
    st.markdown("### 🎙️ Voice Feedback Monitor")
    st.markdown("Displays the most recent transcript, intent, and emotion.")

    voice_file = "memory_archive/latest_voice.json"
    if os.path.exists(voice_file):
        with open(voice_file, "r") as f:
            try:
                data = json.load(f)
                st.success(f"🧠 Transcript: **{data.get('transcript', 'N/A')}**")
                st.write(f"Intent: `{data.get('intent', 'unknown')}`")
                st.write(f"Emotion: `{data.get('emotion', 'neutral')}`")
            except Exception as e:
                st.error(f"Error reading voice file: {e}")
    else:
        st.info("No voice feedback available yet.")