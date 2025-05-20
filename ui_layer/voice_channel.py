# ui_layer/voice_channel.py
from textblob import TextBlob

# crude mapping  ─────────────────────────────────────────────
def _blob_to_emotion(polarity: float) -> str:
    if polarity >  0.4:  return "joy"
    if polarity >  0.1:  return "hope"
    if polarity < -0.4:  return "anger"
    if polarity < -0.1:  return "fear"
    return "neutral"

def analyze_voice_emotion(text: str) -> dict:
    """Return {'emotion': <tag>, 'score': <|polarity|>}"""
    polarity = TextBlob(text).sentiment.polarity         # −1 … +1
    return {
        "emotion": _blob_to_emotion(polarity),
        "score":   round(abs(polarity), 3)
    }
