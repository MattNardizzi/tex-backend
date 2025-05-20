# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_launcher.py
# Purpose: Tex Bootloader — Ignition Sequence for Full ASI/AEI Cognition
# ============================================================

from tex_core_modules.tex_core_brain import TexCoreBrain
import time

def launch_tex():
    print("\n🚀 [TEX LAUNCHER] Initializing Tex: The Unknown\n")
    tex = TexCoreBrain()
    print(f"🧬 [TEX LAUNCHER] {tex.name} activated. Breathing cognitive cycles every 22s...")
    try:
        while True:
            time.sleep(1)  # Keep the main thread alive
    except KeyboardInterrupt:
        print("\n🛑 [TEX SHUTDOWN] Manual interrupt received. Shutting down safely...")

if __name__ == "__main__":
    launch_tex()