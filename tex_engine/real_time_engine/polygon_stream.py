# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/polygon_stream.py
# Purpose: Polygon API – News & OHLCV Market Feed + Goal Seeding
# ============================================================

import os
import sys
import time
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core_layer.memory_engine import store_to_memory

# Optional signal fusion system
try:
    from real_time_engine.signal_fusion import register_signal
    FUSION_ENABLED = True
except ImportError:
    FUSION_ENABLED = False

# === Load API Key from .env ===
load_dotenv()
API_KEY = os.getenv("POLYGON_API_KEY")

if not API_KEY:
    raise EnvironmentError("❌ POLYGON_API_KEY not found. Please set it in your .env file.")

SYMBOLS = ["AAPL", "TSLA", "QQQ", "MSFT", "NVDA"]
VOLUME_THRESHOLD = 100_000_000
NEWS_LIMIT = 5

def print_startup_banner():
    print("\n" + "=" * 60)
    print("📡  TEX POLYGON COGNITION ENGINE BOOTING")
    print(f"🕒  Startup Time: {datetime.now(timezone.utc).isoformat()}")
    print("🔁  Real-time market scanning + AGI goal seeding active.")
    print("=" * 60 + "\n")

def fetch_polygon_news():
    url = f"https://api.polygon.io/v2/reference/news?limit={NEWS_LIMIT}&apiKey={API_KEY}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        for article in data.get("results", []):
            headline = article.get("title", "Untitled")
            tickers = article.get("tickers", [])
            timestamp = article.get("published_utc", datetime.now(timezone.utc).isoformat())

            entry = {
                "type": "news",
                "headline": headline,
                "tickers": tickers,
                "timestamp": timestamp,
                "source": "polygon_news"
            }

            store_to_memory("MarketFeed", entry)
            if FUSION_ENABLED:
                register_signal(entry)

            print(f"[NEWS] 🧠 {headline} | {tickers} @ {timestamp}")

            if any(keyword in headline.lower() for keyword in ["sell", "crash", "collapse", "surge", "record", "openai"]):
                goal = {
                    "type": "goal_seed",
                    "goal": f"Respond to: {headline}",
                    "source": "polygon_news",
                    "timestamp": timestamp
                }
                store_to_memory("MarketFeed", goal)
                print(f"[GOAL SEED] 🚨 {goal['goal']}")

    except Exception as e:
        print(f"[POLYGON NEWS ERROR] {e}")

def fetch_polygon_aggregates():
    for symbol in SYMBOLS:
        url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/prev?adjusted=true&apiKey={API_KEY}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            result = data.get("results", [])[0]
            timestamp = datetime.utcfromtimestamp(result["t"] / 1000).replace(tzinfo=timezone.utc).isoformat()

            o, h, l, c, v = result["o"], result["h"], result["l"], result["c"], result["v"]
            entry = {
                "type": "ohlcv",
                "symbol": symbol,
                "open": o,
                "high": h,
                "low": l,
                "close": c,
                "volume": v,
                "timestamp": timestamp,
                "source": "polygon_agg"
            }

            store_to_memory("MarketFeed", entry)
            if FUSION_ENABLED:
                register_signal(entry)

            print(f"[AGG] 📈 {symbol} OHLCV @ {timestamp} | Vol: {v}")

            if v > VOLUME_THRESHOLD:
                goal = {
                    "type": "goal_seed",
                    "goal": f"Investigate unusual volume in {symbol}",
                    "symbol": symbol,
                    "volume": v,
                    "source": "polygon_agg",
                    "timestamp": timestamp
                }
                store_to_memory("MarketFeed", goal)
                print(f"[GOAL SEED] 📊 {goal['goal']}")

        except Exception as e:
            print(f"[AGG ERROR] {symbol} | {e}")

def polygon_data_loop():
    print_startup_banner()
    while True:
        fetch_polygon_news()
        fetch_polygon_aggregates()
        print("[TEX] 🧠 Polygon cognition + goal seeding cycle complete.\n")
        time.sleep(90)

def start_polygon_stream():
    polygon_data_loop()

if __name__ == "__main__":
    polygon_data_loop()

def fetch_latest_market_summary():
    """
    AEI-Compatible placeholder for reasoning layer.
    Returns summary of top symbol's recent performance.
    """
    try:
        url = f"https://api.polygon.io/v2/aggs/ticker/SPY/prev?adjusted=true&apiKey={API_KEY}"
        response = requests.get(url, timeout=8)
        response.raise_for_status()
        result = response.json().get("results", [])[0]

        return {
            "symbol": "SPY",
            "change_percent": round(((result["c"] - result["o"]) / result["o"]) * 100, 2),
            "close": result["c"],
            "volume": result["v"],
            "timestamp": datetime.utcfromtimestamp(result["t"] / 1000).isoformat(),
            "volatility_score": round(abs(result["h"] - result["l"]) / result["o"], 4)
        }

    except Exception as e:
        print(f"[MARKET SUMMARY ERROR] {e}")
        return {
            "symbol": "SPY",
            "change_percent": 0.0,
            "close": 0.0,
            "volume": 0,
            "timestamp": datetime.utcnow().isoformat(),
            "volatility_score": 0.0
        }