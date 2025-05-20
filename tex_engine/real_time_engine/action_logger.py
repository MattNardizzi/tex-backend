# action_logger.py

from datetime import datetime
from core_layer.memory_engine import store_to_memory

def log_action_event(input_context, action_decision, result_summary):
    payload = {
        "timestamp": datetime.utcnow().isoformat(),
        "input_context": input_context,
        "decision": action_decision,
        "result": result_summary
    }
    store_to_memory("tex_action_log", payload)
    print(f"🧠 [ACTION LOGGED] {action_decision} → {result_summary}")