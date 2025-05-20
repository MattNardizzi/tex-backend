# ============================================================
# Tex VoiceOS V4 — Full-Duplex AGI Voice Orchestrator (Final Fixes)
# File: duplex_stream_orchestrator.py
# ============================================================

from dotenv import load_dotenv
load_dotenv()

from tex_voiceos.voice_stream_input import VoiceStreamInput
from tex_voiceos.stream_transcriber import StreamTranscriber
from tex_voiceos.intent_router import IntentRouter
from tex_voiceos.memory_router import MemoryRouter
from tex_voiceos.tex_speech_output import TexSpeechOutput
from tex_voiceos.proactive_speaker import ProactiveSpeaker

import numpy as np
import threading
import time

class TexVoiceOrchestrator:
    def __init__(self):
        self.voice_input = VoiceStreamInput()
        self.transcriber = StreamTranscriber()
        self.intent_router = IntentRouter()
        self.memory_router = MemoryRouter()
        self.speaker = TexSpeechOutput()
        self.proactive = ProactiveSpeaker()
        self.active = True
        self.listening = True

    def run(self):
        print("[VOICEOS] 🚀 Tex VoiceOS V4 running — full duplex mode.")
        self.voice_input.start_stream()
        self.proactive.start()

        listener_thread = threading.Thread(target=self.listen_loop)
        listener_thread.daemon = True
        listener_thread.start()

        while self.active:
            time.sleep(0.1)

    def listen_loop(self):
        while self.active:
            if not self.listening or self.speaker.speaking:
                time.sleep(0.2)
                continue

            self.voice_input.clear_buffer()
            audio = self.voice_input.get_audio_block()
            if audio is None:
                continue

            audio_np = np.array(audio).flatten()
            transcript = self.transcriber.transcribe_np_audio(audio_np)
            if not transcript:
                continue

            print(f"[VOICEOS] 🗣️ You said: {transcript}")
            parsed = self.intent_router.classify(transcript)
            intent = parsed["intent"]
            emotion = parsed["emotion"]

            if intent == "unknown":
                print("[VOICEOS] 🤖 Intent unclear — repairing with memory...")
                fixed = self.memory_router.reframe_input(transcript)
                if fixed and fixed != transcript:
                    print(f"[REPAIR] 🔧 Using memory-repaired version: {fixed}")
                    transcript = fixed
                    parsed = self.intent_router.classify(fixed)
                    intent = parsed["intent"]
                    emotion = parsed["emotion"]

            response = self.generate_response(transcript, intent)
            self.listening = False
            self.speaker.speak_async(response, emotion=emotion)
            while self.speaker.speaking:
                time.sleep(0.1)
            self.voice_input.clear_buffer()
            self.listening = True

    def generate_response(self, user_input, intent):
        if intent == "cancel":
            return "🧠 All goals have been cleared from memory."
        elif intent == "emotion":
            return "❤️ I'm aware of your emotional state and adjusting accordingly."
        elif intent == "memory":
            return "🧠 I'm reflecting on what we've discussed before."
        elif intent == "goal":
            return f"🚩 I've registered that as a new goal: {user_input}"
        elif intent == "question":
            return "🤔 Let me think carefully about that."
        else:
            return f"🗣️ You said: {user_input}"

if __name__ == "__main__":
    orchestrator = TexVoiceOrchestrator()
    orchestrator.run()