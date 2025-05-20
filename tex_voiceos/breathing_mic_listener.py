# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_voice/breathing_mic_listener.py
# Purpose: Real-Time Breathing Mic Listener with VAD + Interrupt Sync (VoiceOS v2)
# ============================================================

import openai
import sounddevice as sd
import numpy as np
import tempfile
import scipy.io.wavfile
import os
import threading
import time
from datetime import datetime

class BreathingMicListener:
    def __init__(self, callback_function, is_speaking=lambda: False, interrupter=None):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set.")
        openai.api_key = self.api_key

        self.samplerate = 16000
        self.channels = 1
        self.running = False
        self.callback_function = callback_function
        self.vad_threshold = 0.005  # Sensitive, calibrated for natural voice
        self.is_speaking = is_speaking
        self.interrupter = interrupter

    def detect_voice(self, recording):
        energy = np.linalg.norm(recording) / len(recording)
        return energy > self.vad_threshold

    def record_audio_clip(self, duration=1.4):
        print(f"[LATENCY] 🎙️ Started recording at: {datetime.now().isoformat()}")
        try:
            recording = sd.rec(
                int(duration * self.samplerate),
                samplerate=self.samplerate,
                channels=self.channels,
                dtype='int16'
            )
            sd.wait()
            return recording
        except Exception as e:
            print(f"[BREATHING MIC] ❌ Mic recording error: {e}")
            return None

    def transcribe_clip(self, recording):
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
                scipy.io.wavfile.write(temp_audio_file.name, self.samplerate, recording)
                temp_audio_file.flush()

                with open(temp_audio_file.name, "rb") as audio_file:
                    transcript = openai.Audio.transcribe("whisper-1", audio_file)

            os.unlink(temp_audio_file.name)
            clean_text = transcript['text'].strip()

            # 🧼 Filter hallucinated phrases (LLM noise)
            junk_phrases = [
                "thank you for watching", "subscribe", "goodbye",
                "see you next time", "please like", "for watching"
            ]
            if any(junk in clean_text.lower() for junk in junk_phrases):
                print(f"[BREATHING MIC] 🧼 Blocked hallucinated phrase: '{clean_text}'")
                return None

            if len(clean_text.split()) < 2:
                print("[BREATHING MIC] ⚠️ Transcript too short — skipping.")
                return None

            print(f"[LATENCY] ⏱️ Final transcript returned at: {datetime.now().isoformat()}")
            return clean_text

        except Exception as e:
            print(f"[BREATHING MIC] ❌ Whisper transcription error: {e}")
            return None

    def mic_heartbeat(self):
        while self.running:
            try:
                if self.is_speaking():
                    print("[BREATHING MIC] 🛑 Tex is speaking — mic paused.")
                    if self.interrupter:
                        print("[BREATHING MIC] ⛔ Interrupting Tex...")
                        self.interrupter()
                    time.sleep(1.25)
                    continue

                print("[BREATHING MIC] 🎙️ Breathing... checking for voice...")
                recording = self.record_audio_clip()

                if recording is None:
                    print("[BREATHING MIC] ⚠️ No valid recording — skipping.")
                    continue

                if not self.detect_voice(recording):
                    print("[BREATHING MIC] 🤫 No real voice detected — silent breathing.")
                    continue

                transcript = self.transcribe_clip(recording)

                if not transcript:
                    print("[BREATHING MIC] ⚠️ Detected silence or junk — ignoring.")
                    continue

                print(f"[BREATHING MIC] 🗣️ Heard: {transcript}")
                print(f"[DEBUG] Tex is responding to: '{transcript}'")
                self.callback_function(transcript)

            except Exception as e:
                print(f"[BREATHING MIC] ❌ Heartbeat error: {e}")
                time.sleep(1)

    def start_listening(self):
        print("[BREATHING MIC] 🚀 Starting breathing mic engine with VAD...")
        self.running = True
        heartbeat_thread = threading.Thread(target=self.mic_heartbeat)
        heartbeat_thread.start()

    def stop_listening(self):
        print("[BREATHING MIC] 🛑 Stopping breathing mic engine...")
        self.running = False