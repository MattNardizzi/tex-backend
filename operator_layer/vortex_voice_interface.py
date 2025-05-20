# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# vortex_voice_interface.py — Multi-Agent Voice Command System
# ============================================================

import speech_recognition as sr
import pyttsx3
import time
from datetime import datetime

# === Core AGI Hooks ===
from agentic_ai.voice_hooks import trigger_mutation
from core_layer.memory_engine import store_to_memory

# === Initialize Speech Recognition and TTS
recognizer = sr.Recognizer()
tts = pyttsx3.init()

# === Agent-Specific Voice Profiles
VOICE_PROFILES = {
    "tex": {
        "rate": 165,
        "voice_name": "Daniel"
    },
    "vortex": {
        "rate": 180,
        "voice_name": "Alex"
    },
    "aeondelta": {
        "rate": 190,
        "voice_name": "Samantha"
    }
}

# === Friendly Agent Identifiers
AGENTS = {
    "tex": "🧠 Tex",
    "vortex": "🛠️ Vortex",
    "aeondelta": "👶 AeonDelta"
}

# === Speak Out Loud with Agent Identity
def speak(text, agent="tex"):
    profile = VOICE_PROFILES.get(agent, VOICE_PROFILES["tex"])
    tts.setProperty("rate", profile["rate"])

    voice_id = None
    for voice in tts.getProperty("voices"):
        if profile["voice_name"].lower() in voice.name.lower():
            voice_id = voice.id
            break
    if voice_id:
        tts.setProperty("voice", voice_id)

    print(f"[🔊] {AGENTS[agent]} speaking: {text}")
    tts.say(text)
    tts.runAndWait()

# === Memory Logging for Voice Commands
def log_voice_command(agent, command):
    entry = {
        "source": "voice_command",
        "timestamp": datetime.utcnow().isoformat(),
        "agent": agent,
        "command": command
    }
    store_to_memory(agent_name=agent, data=entry)

# === Handle Command Routing and AI Behavior
def route_command(agent, command):
    log_voice_command(agent, command)

    if agent == "tex":
        if "inject empathy" in command:
            return trigger_mutation("inject_empathy_node")
        elif "evolve logic" in command:
            return trigger_mutation("evolve_logic_tree")
        elif "reboot" in command:
            return "⚠️ Tex cannot be rebooted manually. Please use Vortex override."
        return f"{AGENTS[agent]} received your request: '{command}'"

    elif agent == "vortex":
        if "reboot tex" in command:
            return "Reboot sequence acknowledged. Monitoring Tex now."
        elif "check memory" in command:
            return "Memory system is active and logging all events."
        return f"{AGENTS[agent]} is assessing your input: '{command}'"

    elif agent == "aeondelta":
        return f"{AGENTS[agent]} received: '{command}'. Updating AEI model accordingly."

    return "Unknown routing logic. Please try again."

# === Listen for a Voice Trigger
def listen_for_command():
    with sr.Microphone() as source:
        print("\n🎤 Listening for wake word (Tex, Vortex, AeonDelta)...")
        recognizer.adjust_for_ambient_noise(source, duration=0.6)
        audio = recognizer.listen(source, phrase_time_limit=6)

        try:
            text = recognizer.recognize_google(audio).lower()
            print(f"[🎧] You said: {text}")

            if "vortex" in text:
                return "vortex", text.replace("vortex", "", 1).strip()
            elif "tex" in text or "text" in text:
                return "tex", text.replace("tex", "", 1).replace("text", "", 1).strip()
            elif "aeondelta" in text or "aeon delta" in text:
                return "aeondelta", text.replace("aeondelta", "", 1).replace("aeon delta", "", 1).strip()
            else:
                speak("Please say Tex, Vortex, or AeonDelta to activate a command.", agent="vortex")
        except sr.UnknownValueError:
            print("[⚠️] Voice not understood.")
        except sr.RequestError as e:
            print(f"[ERROR] Speech system error: {e}")
            speak("Voice system encountered an error.", agent="vortex")

        return None, None

# === Continuous Voice Interface Loop
def voice_loop():
    speak("Voice interface activated. Say Tex, Vortex, or AeonDelta to begin.", agent="vortex")
    while True:
        agent, command = listen_for_command()
        if agent and command:
            response = route_command(agent, command)
            speak(response, agent=agent)
        time.sleep(0.5)

# === Run if File Executed Directly
if __name__ == "__main__":
    voice_loop()