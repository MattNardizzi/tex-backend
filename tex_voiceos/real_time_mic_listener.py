# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_voice/real_time_mic_listener.py
# Purpose: Asynchronous Whisper Mic Listener for Tex AGI
# ============================================================

import openai
import sounddevice as sd
import numpy as np
import tempfile
import scipy.io.wavfile
import os
import threading

class RealTimeMicListener:
    def __init__(self, callback_function):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set.")
        openai.api_key = self.api_key
        self.samplerate = 16000
        self.duration = 3  # Record 3 seconds
        self.channels = 1
        self.running = False
        self.callback_function = callback_function

    def listen_loop(self):
        while self.running:
            try:
                recording = sd.rec(int(self.duration * self.samplerate), samplerate=self.samplerate, channels=self.channels, dtype='int16')
                sd.wait()

                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
                    scipy.io.wavfile.write(temp_audio_file.name, self.samplerate, recording)
                    temp_audio_file.flush()

                    with open(temp_audio_file.name, "rb") as audio_file:
                        transcript = openai.Audio.transcribe("whisper-1", audio_file)

                os.unlink(temp_audio_file.name)

                clean_text = transcript['text'].strip()

                if not clean_text or len(clean_text) < 5:
                    print("[REALTIME MIC] ⚠️ Silence or noise — ignored.")
                else:
                    print(f"[REALTIME MIC] 🗣️ Heard: {clean_text}")
                    self.callback_function(clean_text)

            except Exception as e:
                print(f"[REALTIME MIC ERROR] ❌ {e}")
                continue

    def start_listening(self):
        self.running = True
        listener_thread = threading.Thread(target=self.listen_loop)
        listener_thread.start()

    def stop_listening(self):
        self.running = False