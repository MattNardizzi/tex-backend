VOICE_LOG_PATH = "memory_archive/voice_metrics.jsonl"

def log_voice_emotion(entry: dict) -> None:
    """
    entry = { 'emotion': 'joy', 'score': 0.78 }
    This will be picked up by the DivergenceReporter.
    """
    import json, time, os
    os.makedirs("memory_archive", exist_ok=True)
    record = {
        "timestamp": time.time(),
        "channel":   "voice",
        **entry
    }
    with open(VOICE_LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
