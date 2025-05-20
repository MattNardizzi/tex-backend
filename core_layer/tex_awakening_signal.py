# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_voiceos/wakeword_guard.py
# Purpose: Fast Wakeword Detector using OpenWakeWord ("Tex")
# ============================================================

from openwakeword.model import Model
import sounddevice as sd
import numpy as np
import threading
import time

class WakewordGuard:
    def __init__(self, callback=None, trigger_word="tex"):
        self.model = Model()
        self.model.load_triggers([trigger_word])
        self.stream = None
        self.running = False
        self.samplerate = 16000
        self.blocksize = 512
        self.callback = callback

    def _callback(self, indata, frames, time_info, status):
        if status:
            print(f"[WAKEWORD] ⚠️ Audio status: {status}")
            return

        audio = np.squeeze(indata)
        predictions = self.model.predict(audio)

        if predictions.get("tex", 0.0) > 0.5:
            print("[WAKEWORD] ✅ Wakeword 'Tex' detected!")
            if self.callback:
                self.callback()
            time.sleep(1.0)  # cooldown

    def start(self):
        print("[WAKEWORD] 🚀 Wakeword listening started...")
        self.running = True
        self.stream = sd.InputStream(
            samplerate=self.samplerate,
            blocksize=self.blocksize,
            channels=1,
            dtype='float32',
            callback=self._callback
        )
        self.stream.start()

    def stop(self):
        print("[WAKEWORD] 🛑 Wakeword listening stopped.")
        self.running = False
        if self.stream:
            self.stream.stop()
            self.stream.close()