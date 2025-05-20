# ============================================================
# Agentic Chat Terminal — Full Console Interaction UI (No GPT)
# ============================================================

from datetime import datetime
from core_layer.memory_engine import store_to_memory
from agentic_ai.voice_hooks import trigger_mutation

AGENTS = {
    "tex": "🧠 Tex",
    "vortex": "🛠️ Vortex",
    "aeondelta": "👶 AeonDelta"
}

def display_header():
    print("\n🔓 Agentic Shell Online — Paste code, ask questions, evolve Tex")
    print("Prefix messages with tex:, vortex:, or aeondelta:")
    print("Type 'exit' to quit.\n")

def process_input(agent, user_input):
    # Log to memory
    store_to_memory(agent_name=agent, data={
        "source": "chat_terminal",
        "timestamp": datetime.utcnow().isoformat(),
        "input": user_input
    })

    # Tex Commands
    if agent == "tex":
        if "inject empathy" in user_input:
            return trigger_mutation("inject_empathy_node")
        elif "evolve logic" in user_input:
            return trigger_mutation("evolve_logic_tree")
        elif "reboot" in user_input:
            return "Tex cannot be rebooted from chat."
        return f"{AGENTS[agent]} processed your request: '{user_input}'"

    # Vortex Commands
    elif agent == "vortex":
        if "reboot tex" in user_input:
            return "Reboot request acknowledged. Monitoring coherence..."
        elif "codex" in user_input:
            return "Codex diff log synced."
        return f"{AGENTS[agent]} executing directive: '{user_input}'"

    # AeonDelta Commands
    elif agent == "aeondelta":
        return f"{AGENTS[agent]} is absorbing and adapting from: '{user_input}'"

    return "Unrecognized agent."

def agentic_chat_loop():
    display_header()
    while True:
        user_input = input(">> ").strip()
        if user_input.lower() == "exit":
            print("🛑 Agentic Chat Ended.")
            break

        for key in AGENTS:
            if user_input.startswith(f"{key}:"):
                clean_input = user_input[len(key)+1:].strip()
                reply = process_input(key, clean_input)
                print(f"{AGENTS[key]}: {reply}")
                break
        else:
            print("⚠️ Please begin with 'tex:', 'vortex:', or 'aeondelta:'.")

if __name__ == "__main__":
    agentic_chat_loop()