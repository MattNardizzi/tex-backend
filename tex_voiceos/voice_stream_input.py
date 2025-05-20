# ============================================================
# Tex VoiceOS V3 — Ultra-Stable Microphone Stream Handler
# File: tex_voiceos/voice_stream_input.py
# ============================================================

import sounddevice as sd
import numpy as np
import queue
import threading
import time

class VoiceStreamInput:
    def __init__(self, samplerate=16000, blocksize=4800, channels=1, dtype='int16'):
        self.samplerate = samplerate
        self.blocksize = blocksize
        self.channels = channels
        self.dtype = dtype
        self.buffer = queue.Queue(maxsize=15)
        self.stream = None
        self.running = False
        self.last_block_time = time.time()

    def _callback(self, indata, frames, time_info, status):
        if status:
            print(f"[MIC STREAM] ⚠️ Stream status: {status}")
        try:
            now = time.time()
            if now - self.last_block_time >= 0.32:  # ⏱️ Throttle: max ~3 blocks/sec
                self.buffer.put_nowait(indata.copy())
                self.last_block_time = now
        except queue.Full:
            print("[MIC STREAM] ⚠️ Buffer full — dropping frame")

    def start_stream(self):
        try:
            print("[MIC STREAM] 🎙️ Starting audio stream...")
            self.running = True
            self.stream = sd.InputStream(
                samplerate=self.samplerate,
                blocksize=self.blocksize,
                channels=self.channels,
                dtype=self.dtype,
                callback=self._callback
            )
            self.stream.start()
        except Exception as e:
            print(f"[MIC STREAM] ❌ Failed to start stream: {e}")
            self.running = False

    def stop_stream(self):
        print("[MIC STREAM] 🛑 Stopping audio stream...")
        self.running = False
        try:
            if self.stream:
                self.stream.stop()
                self.stream.close()
        except Exception as e:
            print(f"[MIC STREAM] ❌ Error stopping stream: {e}")

    def clear_buffer(self):
        flushed = 0
        while not self.buffer.empty():
            try:
                self.buffer.get_nowait()
                flushed += 1
            except queue.Empty:
                break
        if flushed > 0:
            print(f"[MIC STREAM] 🧹 Cleared {flushed} stale audio blocks")

    def get_audio_block(self, timeout=2.0):
        if not self.running:
            print("[MIC STREAM] ⛔ Stream not active.")
            return None

        try:
            block = self.buffer.get(timeout=timeout)
            return np.squeeze(block)
        except queue.Empty:
            print("[MIC STREAM] ⏳ Waiting for audio block...")
            return None