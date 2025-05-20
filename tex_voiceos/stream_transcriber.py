# ============================================================
# Tex VoiceOS V4 — Patched StreamTranscriber with Hallucination Guard
# File: tex_voiceos/stream_transcriber.py
# ============================================================

from faster_whisper import WhisperModel
import numpy as np
import tempfile
import scipy.io.wavfile
import os
import time
from collections import Counter
from core_layer.memory_engine import store_to_memory

class StreamTranscriber:
    def __init__(self, model_size="base.en", compute_type="int8", cpu_threads=4):
        print("[TRANSCRIBER] 🔍 Loading Whisper model...")
        self.model = WhisperModel(
            model_size,
            compute_type=compute_type,
            cpu_threads=cpu_threads,
            num_workers=2
        )
        self.min_confidence = 0.15
        self.min_word_count = 1
        self.max_junk_length = 30
        self.banned_phrases = [
            "thank you for watching", "subscribe", "turn on notifications",
            "see you next time", "please like", "goodbye", "click the bell"
        ]
        self.banned_single_words = {"you", "i", "it", "hi", "text", "yo", "yeah"}

    def compute_entropy_score(self, text):
        words = text.split()
        if not words:
            return 0.0
        counts = Counter(words)
        probs = [count / len(words) for count in counts.values()]
        entropy = -sum(p * np.log2(p) for p in probs)
        confidence = entropy / max(len(words), 1)
        return round(confidence, 3)

    def is_valid_waveform(self, audio_block):
        if not isinstance(audio_block, np.ndarray) or audio_block.size == 0:
            return False
        energy = np.linalg.norm(audio_block)
        return energy > 400  # Calibrated threshold for Mac mic sensitivity

    def transcribe_np_audio(self, audio_block, sample_rate=16000):
        try:
            start_time = time.time()

            if not self.is_valid_waveform(audio_block):
                print("[TRANSCRIBER] ⚠️ Skipped: waveform too quiet or invalid")
                return ""

            # Normalize for Whisper
            if np.max(np.abs(audio_block)) > 0:
                audio_block = np.int16(audio_block / np.max(np.abs(audio_block)) * 32767)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
                scipy.io.wavfile.write(tmp_file.name, sample_rate, audio_block)
                tmp_file.flush()
                segments, _ = self.model.transcribe(tmp_file.name)
            os.unlink(tmp_file.name)

            text = " ".join(
                segment.text.strip() for segment in segments if segment.text.strip()
            ).strip().lower()

            word_count = len(text.split())
            confidence = self.compute_entropy_score(text)

            print(f"[TRANSCRIBER] 🧠 Transcript: '{text}' | wc={word_count} | conf={confidence}")

            if word_count == 1 and text in self.banned_single_words:
                print(f"[TRANSCRIBER] 🪜 Blocked hallucinated single word: '{text}'")
                return ""

            if any(phrase in text for phrase in self.banned_phrases):
                print(f"[TRANSCRIBER] 🪜 Blocked banned phrase: '{text}'")
                return ""

            if word_count > self.max_junk_length and confidence < 0.2:
                print(f"[TRANSCRIBER] ❌ Junk overflow block: '{text}' (wc={word_count}, conf={confidence})")
                return ""

            if confidence < self.min_confidence:
                print(f"[TRANSCRIBER] ❌ Confidence too low: '{text}' (conf={confidence})")
                return ""

            print(f"[TRANSCRIBER] ✅ Final: '{text}' ({round(time.time() - start_time, 2)}s, conf={confidence})")

            store_to_memory("voice_transcripts", {
                "text": text,
                "confidence": confidence,
                "timestamp": time.time()
            })

            return text

        except Exception as e:
            print(f"[TRANSCRIBER] ❌ Whisper failed: {e}")
            return ""