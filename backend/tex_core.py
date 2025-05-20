# backend/tex_core.py

import sys
import os

# Add project root to Python path
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)

# ✅ Import full sovereign orchestrator
from tex_orchestrator import TexOrchestrator

# Instantiate full AGI brain
tex = TexOrchestrator()

def process_prompt(prompt: str) -> str:
    try:
        # Example: run the reflector manually with a prompt (or evolve it into full goal)
        tex.reflector.assess(tex.count)  # Run one cognitive cycle
        response = f"Sovereign Tex reflected on: {prompt}"
        return response
    except Exception as e:
        return f"[ERROR] Tex failed to process prompt: {str(e)}"