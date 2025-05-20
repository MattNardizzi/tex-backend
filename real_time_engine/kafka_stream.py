# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: real_time_engine/kafka_stream.py
# Purpose: Real-Time Kafka Stream Integration for Tex AGI
# ============================================================

from kafka import KafkaConsumer
import json
from datetime import datetime
from core_layer.memory_engine import store_to_memory

# === Kafka Configuration ===
KAFKA_TOPIC = "tex_realtime_data"
KAFKA_BOOTSTRAP_SERVERS = ["localhost:9092"]
GROUP_ID = "tex_realtime_consumer"

# === Stream Listener ===
def listen_to_kafka_stream():
    try:
        consumer = KafkaConsumer(
            KAFKA_TOPIC,
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            group_id=GROUP_ID,
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
            auto_offset_reset="latest",
            enable_auto_commit=True
        )

        print(f"[KAFKA] 🔌 Connected to Kafka topic '{KAFKA_TOPIC}'")

        for msg in consumer:
            data = msg.value
            enriched = {
                "timestamp": datetime.utcnow().isoformat(),
                "source": "kafka_stream",
                "topic": KAFKA_TOPIC,
                "payload": data
            }
            print(f"[KAFKA] 📡 New message received: {data.get('title', str(data)[:50])}")
            store_to_memory("kafka_stream_log", enriched)

    except Exception as e:
        print(f"[KAFKA ERROR] ❌ Failed to consume Kafka stream: {type(e).__name__} — {e}")


# === Kafka Stream Launcher ===
def launch_kafka_stream():
    print("[✅ KAFKA STREAM STARTED]")
    listen_to_kafka_stream()