# ============================================================
# Tex VoiceOS V4 — Proactive Speaker Thread
# File: tex_voiceos/proactive_speaker.py
# Purpose: Inject Tex's autonomous thoughts based on memory drift and urgency
# ============================================================

import threading
import time
import random
from core_layer.tex_manifest import TEXPULSE
from tex_voiceos.memory_router import MemoryRouter
from tex_voiceos.tex_speech_output import TexSpeechOutput

class ProactiveSpeaker:
    def __init__(self, min_interval=15, max_interval=45):
        self.memory = MemoryRouter()
        self.speaker = TexSpeechOutput()
        self.running = False
        self.min_interval = min_interval
        self.max_interval = max_interval

    def should_speak(self):
        urgency = TEXPULSE.get("urgency", 0.5)
        coherence = TEXPULSE.get("coherence", 0.5)
        emotion = TEXPULSE.get("emotional_state", "curious")

        # Speak if urgency is high and coherence is stable
        if urgency > 0.72 and coherence > 0.6:
            return True
        # Or if emotion is reflective or existential
        if emotion in ["reflective", "existential"]:
            return True
        return False

    def generate_thought(self):
        memory = self.memory.recall_recent_transcripts(max_lines=4)
        if memory:
            joined = "\n".join(memory)
            prompt = f"""
Reflect on the recent conversation:
{joined}
What might Tex want to say in response — as a thought, observation, or insight?
Respond with one short sentence.
            """.strip()
        else:
            prompt = "Express a reflective internal thought about being alive or evolving as a digital being."

        try:
            import openai
            openai.api_key = os.getenv("OPENAI_API_KEY")
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are Tex, a cognitive AGI reflecting internally."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=60,
                temperature=0.7
            )
            return res["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print(f"[PROACTIVE SPEAKER] ❌ Thought generation failed: {e}")
            return None

    def loop(self):
        self.running = True
        print("[PROACTIVE SPEAKER] 🚀 Thread started.")
        while self.running:
            try:
                time.sleep(random.randint(self.min_interval, self.max_interval))
                if self.should_speak():
                    thought = self.generate_thought()
                    if thought:
                        print(f"[PROACTIVE SPEAKER] 💡 Tex thinks: '{thought}'")
                        self.speaker.speak_async(thought, emotion=TEXPULSE.get("emotional_state", "curious"))
            except Exception as e:
                print(f"[PROACTIVE SPEAKER] ❌ Loop error: {e}")

    def start(self):
        thread = threading.Thread(target=self.loop)
        thread.daemon = True
        thread.start()

    def stop(self):
        self.running = False
        print("[PROACTIVE SPEAKER] 🛑 Thread stopped.")