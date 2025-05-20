# ============================================================
# Agentic Terminal — Sovereign Local Chat with Tex/Vortex/AeonDelta
# ============================================================

from datetime import datetime
from core_layer.memory_engine import store_to_memory
from agentic_ai.voice_hooks import trigger_mutation

AGENTS = {
    "tex": "🧠 Tex",
    "vortex": "🛠️ Vortex",
    "aeondelta": "👶 AeonDelta"
}

def route_input(agent, command):
    store_to_memory(agent_name=agent, data={
        "source": "terminal_command",
        "timestamp": datetime.utcnow().isoformat(),
        "command": command
    })

    if agent == "tex":
        if "inject empathy" in command:
            return trigger_mutation("inject_empathy_node")
        elif "evolve logic" in command:
            return trigger_mutation("evolve_logic_tree")
        return f"{AGENTS[agent]} received your input: {command}"

    elif agent == "vortex":
        if "reboot tex" in command:
            return "Reboot initiated. Vortex will monitor recovery."
        elif "codex" in command:
            return "Codex diff log is active and mutation history is being tracked."
        return f"{AGENTS[agent]} confirms your directive: {command}"

    elif agent == "aeondelta":
        return f"{AGENTS[agent]} is processing your input to evolve internal model."

    return "Unknown agent."

def terminal_loop():
    print("\n🔓 Agentic Terminal Active — Speak to Tex, Vortex, or AeonDelta")
    print("Type 'exit' to quit.\n")

    while True:
        raw = input(">> ").strip().lower()
        if raw == "exit":
            print("🛑 Session ended.")
            break

        for key in AGENTS:
            if raw.startswith(key):
                command = raw.replace(key, "", 1).strip()
                response = route_input(key, command)
                print(f"{AGENTS[key]}: {response}")
                break
        else:
            print("Please start your input with Tex, Vortex, or AeonDelta.")

if __name__ == "__main__":
    terminal_loop()