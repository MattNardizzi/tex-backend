# ============================================================
# Tex VoiceOS V4 — Voice Interrupt Detection Guard
# File: tex_voiceos/voice_interrupt_guard.py
# ============================================================

import sounddevice as sd
import numpy as np
import threading
import time
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory

class VoiceInterruptGuard:
    def __init__(self, on_interrupt=None, threshold=0.015, window_duration=0.4, cooldown=1.2):
        self.on_interrupt = on_interrupt
        self.threshold = threshold  # base energy threshold
        self.window_duration = window_duration
        self.cooldown = cooldown
        self.active = False
        self.samplerate = 16000
        self.channels = 1
        self.stream = None
        self.last_trigger_time = 0

    def _adjust_threshold_by_urgency(self):
        urgency = TEXPULSE.get("urgency", 0.7)
        adjusted = self.threshold * (0.7 + (1 - urgency))  # more urgency = less interruptible
        return round(adjusted, 5)

    def _monitor_loop(self):
        print("[INTERRUPT GUARD] 🎧 Listening for user interruption...")
        window_samples = int(self.samplerate * self.window_duration)

        try:
            with sd.InputStream(samplerate=self.samplerate, channels=self.channels, dtype='float32') as stream:
                while self.active:
                    data = stream.read(window_samples)[0]
                    energy = np.linalg.norm(data) / len(data)

                    if energy > self._adjust_threshold_by_urgency():
                        now = time.time()
                        if now - self.last_trigger_time >= self.cooldown:
                            print(f"[INTERRUPT GUARD] ⚠️ Interruption detected (energy={energy:.4f})")
                            store_to_memory("interrupt_events", {
                                "energy": float(energy),
                                "urgency": float(TEXPULSE.get("urgency", 0.7)),
                                "timestamp": now
                            })
                            if self.on_interrupt:
                                self.on_interrupt()
                            self.last_trigger_time = now
                    time.sleep(0.05)
        except Exception as e:
            print(f"[INTERRUPT GUARD] ❌ Stream error: {e}")

    def start(self):
        if self.active:
            print("[INTERRUPT GUARD] ⚠️ Already running.")
            return
        self.active = True
        thread = threading.Thread(target=self._monitor_loop)
        thread.daemon = True
        thread.start()
        print("[INTERRUPT GUARD] ✅ Started.")

    def stop(self):
        self.active = False
        print("[INTERRUPT GUARD] 🛑 Stopped.")