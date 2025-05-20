# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# vortex_voice.py — Natural macOS Voice Engine for Tex
# ============================================================

import subprocess
import platform

class VortexVoice:
    def __init__(self, voice="Samantha", rate=200):
        self.voice = voice
        self.rate = rate
        self.platform = platform.system()
        print(f"[🔊] Voice system initialized: {self.voice} ({self.platform})")

    def speak(self, text):
        print(f"[🎤] Tex says: {text}")
        if self.platform == "Darwin":
            try:
                subprocess.run(
                    ["say", "-v", self.voice, text],
                    check=True
                )
            except subprocess.CalledProcessError as e:
                print(f"[ERROR] Voice synthesis failed: {e}")
        else:
            print("[⚠️] Voice system is only available on macOS.")

def list_mac_voices():
    """Print all available macOS voices."""
    if platform.system() == "Darwin":
        print("🗣️ Available macOS voices:")
        subprocess.run(["say", "-v", "?"])
    else:
        print("❌ This command is only available on macOS.")

# === Example test
if __name__ == "__main__":
    voice = VortexVoice(voice="Samantha")
    voice.speak("Voice interface online. Welcome back, Operator.")