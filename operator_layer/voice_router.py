# ============================================================
# Voice Router — Live Wake Word Listener + Agent Dispatcher
# ============================================================

from operator_layer.vortex_voice_interface import listen_for_command
from agent_brains.tex_agent import tex_respond
from agent_brains.vortex_agent import vortex_respond
from agent_brains.aeondelta_agent import aeondelta_respond

def dispatch_voice(agent, command):
    if agent == "tex":
        tex_respond(command)
    elif agent == "vortex":
        vortex_respond(command)
    elif agent == "aeondelta":
        aeondelta_respond(command)
    else:
        print("❌ Unknown agent.")

def start_voice_router():
    print("🎙️ Voice router live. Say Tex, Vortex, or AeonDelta...")
    while True:
        agent, command = listen_for_command()
        if agent and command:
            dispatch_voice(agent, command)

if __name__ == "__main__":
    start_voice_router()
