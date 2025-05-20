# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: tex_voice/voice_input_listener.py
# Purpose: Listen to user's microphone input for Tex voice interface
# ============================================================

import speech_recognition as sr

class VoiceInputListener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self):
        """Capture voice input and return text."""
        with self.microphone as source:
            print("🎙️ Listening for user input...")
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio)
            print(f"🧠 Heard: {text}")
            return text
        except sr.UnknownValueError:
            print("❓ Couldn't understand audio.")
            return ""
        except sr.RequestError:
            print("⚠️ Speech recognition service failed.")
            return ""