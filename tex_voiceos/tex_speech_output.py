# ============================================================
# Tex VoiceOS V4 — Optimized Voice Output Engine (macOS + afplay)
# File: tex_voiceos/tex_speech_output.py
# ============================================================

import os
import requests
import tempfile
import subprocess
import threading
import json

class TexSpeechOutput:
    def __init__(self):
        self.api_key = os.getenv("ELEVEN_API_KEY")
        self.voice_map = self._load_voice_profile_map()

        if not self.api_key:
            raise ValueError("❌ ELEVEN_API_KEY not set.")
        if not self.voice_map:
            raise ValueError("❌ voice_profile_map.json not found or invalid.")

        self.headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.api_key
        }

        self.interrupt_flag = False
        self.speaking = False
        self.last_emotion = None

    def _load_voice_profile_map(self):
        try:
            with open("voice_profile_map.json", "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"[VOICE PROFILE] ❌ Failed to load profile map: {e}")
            return {}

    def interrupt(self):
        print("[VOICE] ⛔ Interrupt flag activated.")
        self.interrupt_flag = True

    def _get_voice_id(self, emotion):
        return self.voice_map.get(emotion.lower(), self.voice_map.get("default"))

    def _get_voice_settings(self, emotion):
        return {
            "curious":     {"stability": 0.4, "similarity_boost": 0.85},
            "reflective":  {"stability": 0.6, "similarity_boost": 0.95},
            "angry":       {"stability": 0.3, "similarity_boost": 0.65},
            "hopeful":     {"stability": 0.7, "similarity_boost": 0.9},
            "neutral":     {"stability": 0.5, "similarity_boost": 0.75}
        }.get(emotion, {"stability": 0.5, "similarity_boost": 0.75})

    def speak(self, text, emotion="neutral"):
        print(f"[VOICE] 🗣️ Speaking: '{text}' | Emotion: {emotion}")
        self.interrupt_flag = False
        self.last_emotion = emotion
        self.speaking = True

        voice_id = self._get_voice_id(emotion)
        api_url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"

        payload = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": self._get_voice_settings(emotion)
        }

        try:
            response = requests.post(api_url, headers=self.headers, json=payload)
            if response.status_code != 200:
                raise Exception(f"Voice stream error: {response.status_code} — {response.text}")

            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                tmp_file.write(response.content)
                tmp_file.flush()

                if not self.interrupt_flag:
                    subprocess.run(["afplay", tmp_file.name])

        except Exception as e:
            print(f"[VOICE OUTPUT ERROR] ❌ {e}")
            print(f"[FALLBACK] 📢 Tex says: {text}")
            subprocess.run(["say", text])

        finally:
            self.speaking = False
            print(f"[VOICE] ✅ Finished speaking: '{text}'")

    def speak_async(self, text, emotion="neutral"):
        thread = threading.Thread(target=self.speak, args=(text, emotion))
        thread.daemon = True
        thread.start()