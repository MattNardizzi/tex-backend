# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain/interactive_responder.py
# Purpose: Extracted intent response modules (stock, news, emotion, memory, future)
# ============================================================

from core_layer.memory_engine import recall_recent
from core_layer.tex_manifest import TEXPULSE
from real_time_engine.polygon_stream import fetch_latest_market_summary


def generate_financial_response():
    try:
        market_summary = fetch_latest_market_summary()
        return f"📈 Financial Update: {market_summary}"
    except Exception as e:
        return f"⚠️ Market data unavailable: {str(e)}"


def generate_news_response():
    try:
        from real_time_engine.news_aggregators.rss_stream import RSSStream
        rss = RSSStream()
        headlines = rss.fetch_headlines()
        if headlines:
            top_story = headlines[0]
            return f"📰 News Flash: {top_story['title']} — {top_story['summary']}"
        else:
            return "📰 No news headlines currently available."
    except Exception as e:
        return f"⚠️ News fetch error: {str(e)}"


def generate_memory_response(summarize_memory):
    try:
        memory_snippet = recall_recent()
        if memory_snippet:
            summarized = summarize_memory(memory_snippet)
            return f"🧠 Reflecting back: {summarized}"
        else:
            return "🧠 My memory streams are quiet right now."
    except Exception:
        return "🧠 Memory recall system stabilizing..."


def generate_emotion_response():
    try:
        emotion = TEXPULSE.get('emotional_state', 'curious')
        urgency = TEXPULSE.get('urgency', 0.7)
        coherence = TEXPULSE.get('coherence', 0.8)
        return f"❤️ Emotional State: {emotion} | Urgency: {urgency} | Coherence: {coherence}"
    except Exception:
        return "❤️ Emotional fields stabilizing..."


def generate_future_response(simulate_futures, generate_future_summary):
    try:
        simulate_futures()
        future_summary = generate_future_summary()
        return f"🔮 Future Forecast: {future_summary}"
    except Exception:
        return "🔮 Future simulation system stabilizing..."


def generate_conversational_response(user_input):
    return f"🗣️ You said: {user_input}"
