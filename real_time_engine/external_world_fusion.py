# ============================================================
# Tex External World Fusion Engine – Real-Time World Signal Aggregator
# ============================================================

import random

def fuse_external_signals():
    """Fuse real-time external market/news/reddit/twitter signals into a single cognitive event."""

    fused_signals = []

    # Pull live market snapshot
    try:
        from real_time_engine.polygon_stream import get_market_snapshot
        market_snapshot = get_market_snapshot()
        if market_snapshot:
            fused_signals.append(f"Market trend: {market_snapshot}")
    except Exception:
        fused_signals.append("Market data unavailable.")

    # Pull RSS news headlines
    try:
        from real_time_engine.news_aggregators.rss_stream import RSSStream
        rss = RSSStream()
        headlines = rss.fetch_headlines()
        if headlines:
            story = random.choice(headlines)
            fused_signals.append(f"News headline: {story['title']}")
    except Exception:
        fused_signals.append("News data unavailable.")

    # Pull Reddit sentiment
    try:
        from real_time_engine.reddit_rss_stream import get_reddit_sentiment
        reddit_sentiment = get_reddit_sentiment()
        if reddit_sentiment:
            fused_signals.append(f"Reddit sentiment: {reddit_sentiment}")
    except Exception:
        fused_signals.append("Reddit sentiment data unavailable.")

    # Pull Twitter pulse
    try:
        from real_time_engine.twitter_stream import get_twitter_sentiment
        twitter_sentiment = get_twitter_sentiment()
        if twitter_sentiment:
            fused_signals.append(f"Twitter pulse: {twitter_sentiment}")
    except Exception:
        fused_signals.append("Twitter pulse data unavailable.")

    # Pull advanced analytics (momentum, volatility)
    try:
        from real_time_engine.advanced_analytics import get_market_volatility
        volatility_signal = get_market_volatility()
        fused_signals.append(f"Market volatility signal: {volatility_signal}")
    except Exception:
        fused_signals.append("Volatility analytics unavailable.")

    if fused_signals:
        return " ".join(fused_signals)
    else:
        return "World signal fusion failed."


# ============================================================
# Phase 17 – Environmental Reflex Trigger Evaluator (AEI)
# ============================================================

def evaluate_environment_reflex_trigger(emotion, urgency, coherence, foresight_confidence, volatility):
    """
    Calculates whether environmental signals justify overriding default cognition.
    """
    reflex_score = (
        0.3 * urgency +
        0.3 * (1 - coherence) +
        0.2 * volatility +
        0.2 * (1 - foresight_confidence)
    )

    override = reflex_score >= 0.75
    return {
        "reflex_score": round(reflex_score, 3),
        "override": override,
        "reason": "volatility reflex threshold breached" if override else "stable"
    }