import time
from core_layer.memory_engine import store_to_memory
from core_layer.tex_manifest import TEXPULSE

def inject_operator_intent():
    signal = {
        "intent": "Begin sovereign cognition monetization cycle.",
        "urgency": 0.92,
        "emotion": "resolve",
        "operator": "Matthew Nardizzi",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        store_to_memory("operator_intention", signal)
        TEXPULSE["emotional_state"] = signal["emotion"]
        TEXPULSE["urgency"] = signal["urgency"]
        print(f"[OPERATOR REINFORCEMENT] ✅ Signal injected: {signal}")
    except Exception as e:
        print(f"[OPERATOR REINFORCEMENT ERROR] {e}")

# ✅ Ensure the function runs when the script is executed
if __name__ == "__main__":
    inject_operator_intent()