# ============================================================
# Tex Real-Time Cognitive Reasoning Engine (LLM Matching Version)
# ============================================================

import random
from core_layer.memory_engine import recall_recent
from core_layer.goal_engine import get_active_goals
from core_layer.tex_manifest import TEXPULSE
from real_time_engine.polygon_stream import fetch_latest_market_summary
from real_time_engine.news_aggregators.rss_stream import RSSStream
from tex_voiceos.tex_llm_reasoner import LLMReasoner  # <-- NEW: import LLM reasoner

company_symbols = {
    "apple": "AAPL",
    "tesla": "TSLA",
    "amazon": "AMZN",
    "nvidia": "NVDA",
    "microsoft": "MSFT",
    "google": "GOOG",
    "meta": "META",
    "bitcoin": "BTC",
    "ethereum": "ETH"
}

def generate_reasoned_response(user_input, brain_instance=None):
    user_input_lower = user_input.lower()
    response_fragments = []

    # === Real LLM-based Classification ===
    llm_reasoner = LLMReasoner()
    topic = llm_reasoner.classify_question(user_input)

    # === Company-Specific Stock Matching
    if topic == "stock":
        for company, symbol in company_symbols.items():
            if company in user_input_lower:
                try:
                    market_summary = fetch_latest_market_summary()
                    if market_summary:
                        response_fragments.append(f"📈 {company.title()} ({symbol}) Market Update: {market_summary}")
                    else:
                        response_fragments.append(f"📈 {company.title()} ({symbol}) market data is currently unavailable.")
                except Exception as e:
                    response_fragments.append(f"⚠️ Stock data error for {company.title()}: {str(e)}")
                break
        else:
            # General stock market summary if no specific company mentioned
            try:
                market_summary = fetch_latest_market_summary()
                if market_summary:
                    response_fragments.append(f"📈 Financial Market Summary: {market_summary}")
            except Exception as e:
                response_fragments.append(f"⚠️ Market Data Error: {str(e)}")

    # === News Handling
    elif topic == "news":
        try:
            rss = RSSStream()
            headlines = rss.fetch_headlines()
            if headlines:
                random_headline = random.choice(headlines)
                response_fragments.append(f"📰 News Flash: {random_headline['title']} — {random_headline['summary']}")
        except Exception as e:
            response_fragments.append(f"⚠️ News Data Error: {str(e)}")

    # === Memory Recall
    elif topic == "memory":
        try:
            memory_snippet = recall_recent()
            if memory_snippet and brain_instance:
                summarized_memory = brain_instance.summarize_memory(memory_snippet)
                response_fragments.append(f"🧠 Reflecting back: {summarized_memory}")
        except Exception:
            response_fragments.append("⚠️ Memory recall failed.")

    # === Emotional Awareness
    elif topic == "emotion":
        try:
            emotion = TEXPULSE.get('emotional_state', 'curious')
            urgency = TEXPULSE.get('urgency', 0.7)
            coherence = TEXPULSE.get('coherence', 0.8)
            response_fragments.append(f"❤️ Emotional State: {emotion} | Urgency: {urgency} | Coherence: {coherence}")
        except Exception:
            response_fragments.append("⚠️ Emotional state unavailable.")

    # === Future Projection
    elif topic == "future":
        try:
            if brain_instance:
                brain_instance.simulate_futures()
                future_summary = brain_instance.generate_future_summary()
                response_fragments.append(f"🔮 Future Forecast: {future_summary}")
        except Exception:
            response_fragments.append("⚠️ Future simulation failed.")

    # === Fallback Cognitive Reflection
    else:
        try:
            if brain_instance:
                thought, emotional_state = brain_instance.think()
                response_fragments.append(f"🧠 Internal Reflection: {thought}")
            else:
                response_fragments.append("I am processing deeper cognitive streams...")
        except Exception:
            response_fragments.append("⚠️ Cognitive reflection system offline.")

    # === Final Assembly
    final_response = " ".join(response_fragments)
    return final_response