# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_voice/whisper_input_listener.py
# Purpose: Capture mic input, stream to Whisper, return clean text for Tex AGI
# ============================================================

import openai
import sounddevice as sd
import numpy as np
import tempfile
import scipy.io.wavfile
import os
from datetime import datetime, timezone

class WhisperInputListener:
    def __init__(self, is_speaking=lambda: False):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set.")
        openai.api_key = self.api_key

        self.samplerate = 16000
        self.duration = 3  # Default voice clip length
        self.channels = 1
        self.energy_threshold = 500  # Minimum mic energy to accept input
        self.is_speaking = is_speaking

    def listen_and_transcribe(self):
        if self.is_speaking():
            print("[WHISPER LISTENER] 🛑 Tex is currently speaking — suppressing mic input.")
            return None

        print("[WHISPER LISTENER] 🎙️ Listening...")

        try:
            # === Record audio ===
            recording = sd.rec(int(self.duration * self.samplerate), samplerate=self.samplerate, channels=self.channels, dtype='int16')
            sd.wait()

            # === Check audio energy ===
            energy = np.linalg.norm(recording)
            if energy < self.energy_threshold:
                print(f"[WHISPER LISTENER] ⚠️ Silence/noise detected (energy={energy:.2f}) — skipping.")
                return None

            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
                scipy.io.wavfile.write(temp_audio_file.name, self.samplerate, recording)
                temp_audio_file.flush()

                with open(temp_audio_file.name, "rb") as audio_file:
                    transcript = openai.Audio.transcribe("whisper-1", audio_file)

            os.unlink(temp_audio_file.name)  # Cleanup temp

            clean_text = transcript['text'].strip()
            if not clean_text or len(clean_text) < 3:
                print("[WHISPER LISTENER] ⚠️ Too short or unclear — ignoring.")
                return None

            timestamp = datetime.now(timezone.utc).isoformat()
            print(f"[WHISPER LISTENER] 🗣️ {timestamp} | You said: {clean_text}")

            # === Optional: Save raw transcript (stub for memory_engine) ===
            self._log_transcript(clean_text, timestamp)

            return clean_text

        except Exception as e:
            print(f"[WHISPER LISTENER ERROR] ❌ {e}")
            return None

    def _log_transcript(self, text, timestamp):
        try:
            log_entry = f"{timestamp} | {text}\n"
            with open("memory_archive/voice_transcripts.log", "a") as f:
                f.write(log_entry)
        except Exception as log_error:
            print(f"[TRANSCRIPT LOG ERROR] {log_error}")