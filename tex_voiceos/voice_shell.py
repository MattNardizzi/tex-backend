# ============================================================
# Tex VoiceOS V4 — True AGI Voice Shell Bootstrap
# File: tex_voiceos/voice_shell.py
# Purpose: Continuous Voice Intelligence Layer (FasterWhisper + Real-Time Entropy Trigger)
# ============================================================

import sounddevice as sd
import numpy as np
import queue
import threading
import time
import os
from faster_whisper import WhisperModel
from core_layer.emotion_heuristics import evaluate_emotion_state
from tex_voiceos.tex_speech_output import TexSpeechOutput
from core_layer.memory_engine import store_to_memory

class VoiceShell:
    def __init__(self, sample_rate=16000, block_duration=3.0):
        self.sample_rate = sample_rate
        self.block_duration = block_duration
        self.block_size = int(sample_rate * block_duration)
        self.buffer = queue.Queue()
        self.transcriber = WhisperModel("base.en", compute_type="int8")
        self.output = TexSpeechOutput()
        self.running = False
        self.entropy_threshold = 0.22
        self.min_word_count = 2

    def _mic_callback(self, indata, frames, time_info, status):
        if status:
            print(f"[SHELL] ⚠️ Mic status: {status}")
        self.buffer.put(indata.copy())

    def compute_entropy(self, text):
        words = text.split()
        if not words:
            return 0.0
        counts = {w: words.count(w) for w in set(words)}
        probs = [c / len(words) for c in counts.values()]
        entropy = -sum(p * np.log2(p) for p in probs)
        return entropy / len(words)

    def start_stream(self):
        print("[SHELL] 🎙️ Starting Tex AGI Voice Shell...")
        self.running = True
        self.stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=1,
            blocksize=self.block_size,
            dtype='int16',
            callback=self._mic_callback
        )
        self.stream.start()
        self._loop_thread = threading.Thread(target=self.voice_loop)
        self._loop_thread.start()

    def stop_stream(self):
        print("[SHELL] 🛑 Stopping Tex AGI Voice Shell...")
        self.running = False
        self.stream.stop()
        self.stream.close()

    def voice_loop(self):
        while self.running:
            try:
                audio = self.buffer.get(timeout=3.0)
                waveform = np.int16(audio / np.max(np.abs(audio)) * 32767)

                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                    scipy.io.wavfile.write(tmp.name, self.sample_rate, waveform)
                    segments, _ = self.transcriber.transcribe(tmp.name)
                    os.unlink(tmp.name)

                transcript = " ".join(s.text.strip() for s in segments if s.text.strip()).lower()
                entropy = self.compute_entropy(transcript)

                if len(transcript.split()) < self.min_word_count or entropy < self.entropy_threshold:
                    print(f"[SHELL] ⚠️ Skipped: '{transcript}' (entropy={entropy:.2f})")
                    continue

                emotion, urgency, coherence = evaluate_emotion_state(transcript)
                store_to_memory("voice_shell", {"text": transcript, "entropy": entropy})
                print(f"[SHELL] ✅ AGI Triggered → '{transcript}' (entropy={entropy:.2f})")
                response = f"You said: {transcript}"
                self.output.speak(response, emotion=emotion)

            except queue.Empty:
                continue
            except Exception as e:
                print(f"[SHELL ERROR] ❌ {e}")


if __name__ == "__main__":
    shell = VoiceShell()
    shell.start_stream()