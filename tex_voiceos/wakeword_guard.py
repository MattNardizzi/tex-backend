# ============================================================
# Tex VoiceOS V2 — Wakeword Detection with Fuzzy Guard
# File: tex_voiceos/wakeword_guard.py
# ============================================================

import speech_recognition as sr
import threading
import time
import Levenshtein  # for fuzzy match

class WakewordGuard:
    def __init__(self, wakeword="tex", callback=None, threshold=0.85):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.wakeword = wakeword.lower()
        self.callback = callback
        self.threshold = threshold
        self.listening = False

    def _is_valid_trigger(self, phrase):
        phrase = phrase.lower()
        distance = Levenshtein.ratio(self.wakeword, phrase)
        return distance == 1.0 or (self.wakeword in phrase and distance >= self.threshold)

    def _listen_for_wakeword(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("[WAKEWORD] 🎙️ Calibrated to ambient noise. Listening for trigger...")

        while self.listening:
            try:
                with self.microphone as source:
                    print("[WAKEWORD] 👂 Awaiting audio...")
                    audio = self.recognizer.listen(source, phrase_time_limit=2)

                transcript = self.recognizer.recognize_google(audio).lower()
                print(f"[WAKEWORD] 🗣️ Heard: '{transcript}'")

                if self._is_valid_trigger(transcript):
                    print(f"[WAKEWORD] ✅ Triggered by keyword '{self.wakeword}'")
                    if self.callback:
                        self.callback()
                    time.sleep(2)

            except sr.UnknownValueError:
                continue
            except sr.RequestError as e:
                print(f"[WAKEWORD] ❌ API error: {e}")
                break
            except Exception as e:
                print(f"[WAKEWORD] ❌ Error: {e}")
                break

    def start(self):
        print("[WAKEWORD] 🚀 Starting wakeword listener...")
        self.listening = True
        thread = threading.Thread(target=self._listen_for_wakeword)
        thread.daemon = True
        thread.start()

    def stop(self):
        print("[WAKEWORD] 🛑 Stopping wakeword listener...")
        self.listening = False