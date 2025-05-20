# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# texshell.py — Agentic Local Terminal UI (Tex, Vortex, AeonDelta)
# ============================================================

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, Static
from textual.containers import Vertical
from datetime import datetime
from core_layer.memory_engine import store_to_memory
from agentic_ai.voice_hooks import trigger_mutation

# === Agent Routing Logic ===
def route_agent(agent, message):
    agent = agent.lower()
    message = message.strip().lower()

    if agent == "vortex":
        if "reboot tex" in message:
            return "🔁 Vortex: Rebooting Tex... (simulated)"
        if "check memory" in message:
            return "🧠 Vortex: Memory check passed. Logs intact."
        return f"[VORTEX] {message}"

    elif agent == "tex":
        if "inject empathy" in message:
            return trigger_mutation("inject_empathy_node")
        if "evolve logic" in message:
            return trigger_mutation("evolve_logic_tree")
        return f"[TEX] {message}"

    elif agent == "aeondelta":
        if "observe" in message:
            return "👶 AeonDelta: Observation logged. Evolving..."
        return f"[AEONDELTA] {message}"

    elif "def " in message or "import " in message or "class " in message:
        return f"[CodeBlock Detected] 📦 Simulating code execution:\n{message}"

    return f"[System] Command not understood for agent '{agent}'."


# === Output Panel ===
class AgentOutput(Static):
    def append(self, text: str):
        current = self.renderable if self.renderable else ""
        self.update(current + f"\n{text}")


# === Main Shell UI ===
class TexShell(App):
    CSS_PATH = None
    BINDINGS = [("ctrl+c", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        self.output = AgentOutput("", classes="output")
        self.input = Input(placeholder="Type (tex:, vortex:, aeondelta:) or paste code...")
        yield Vertical(
            Static("🧠 Agentic Shell Online – Tex / Vortex / AeonDelta Ready", classes="banner"),
            self.output,
            self.input
        )
        yield Footer()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        raw = event.value.strip()
        self.input.value = ""
        timestamp = datetime.utcnow().isoformat()

        if raw.lower() == "exit":
            self.exit()
            return

        # === Agent Parsing ===
        if ":" in raw:
            prefix, command = raw.split(":", 1)
            agent = prefix.strip().lower()
            message = command.strip()
        else:
            agent = "tex"
            message = raw

        store_to_memory(agent, message)
        reply = route_agent(agent, message)
        self.output.append(f"\n>> {raw}\n{reply}\n")


# === App Entry Point ===
if __name__ == "__main__":
    TexShell().run()