# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_voice/voice_output_speaker.py
# Purpose: ElevenLabs AGI Voice Output with Real-Time Streaming + Interrupt
# ============================================================

import os
import requests

class VoiceOutputSpeaker:
    def __init__(self):
        self.api_key = os.getenv("ELEVEN_API_KEY")
        self.voice_id = os.getenv("ELEVEN_VOICE_ID")

        if not self.api_key:
            raise ValueError("❌ ELEVEN_API_KEY environment variable not set.")
        if not self.voice_id:
            raise ValueError("❌ ELEVEN_VOICE_ID environment variable not set.")

        self.api_url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}/stream"
        self.headers = {
            "xi-api-key": self.api_key,
            "Content-Type": "application/json"
        }

        self.interrupt_flag = False

    def interrupt(self):
        self.interrupt_flag = True

    def speak(self, text, emotion="neutral"):
        print(f"[VOICE] 🗣️ Speaking with emotion: {emotion}")

        payload = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.4,
                "similarity_boost": 0.8
            }
        }

        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                stream=True
            )
            if response.status_code != 200:
                raise Exception(f"Voice stream error: {response.status_code} - {response.text}")

            import pyaudio
            p = pyaudio.PyAudio()
            stream = p.open(format=pyaudio.paInt16, channels=1, rate=22050, output=True)

            self.interrupt_flag = False

            for chunk in response.iter_content(chunk_size=1024):
                if self.interrupt_flag:
                    print("[VOICE] ⛔ Interrupted mid-sentence.")
                    break
                if chunk:
                    stream.write(chunk)

            stream.stop_stream()
            stream.close()
            p.terminate()

        except Exception as e:
            print(f"[VOICE OUTPUT ERROR] ❌ {e}")
            print(f"[FALLBACK] 📢 Tex says: {text}")