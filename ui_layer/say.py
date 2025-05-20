from ui_layer.voice_channel import analyze_voice_emotion
from swarm_layer.swarm_log    import log_voice_emotion    # new function, see below

def say(text: str) -> None:
    # ① existing TTS or print logic …
    tts_engine.speak(text)            # ← or print()

    # ② NEW: auto‑label “voice” channel
    voice_metrics = analyze_voice_emotion(text)
    log_voice_emotion(voice_metrics)  # {'emotion': 'hope', 'score': 0.23}
