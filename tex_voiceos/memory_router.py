# ============================================================
# Tex VoiceOS V3 — Memory Router with Entropy Guard + GPT-4 Repair
# File: tex_voiceos/memory_router.py
# ============================================================

import openai
import os
from collections import Counter
import numpy as np
from datetime import datetime

MEMORY_PATH = "memory_archive/voice_transcripts.log"

class MemoryRouter:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("❌ OPENAI_API_KEY not set.")
        openai.api_key = self.api_key
        self.model = "gpt-4"

    def recall_recent_transcripts(self, max_lines=6):
        if not os.path.exists(MEMORY_PATH):
            return []
        try:
            with open(MEMORY_PATH, "r") as f:
                lines = f.readlines()[-max_lines:]
                return [line.strip().split("|", 1)[-1].strip() for line in lines if "|" in line and len(line.strip()) > 5]
        except Exception as e:
            print(f"[MEMORY ROUTER] ❌ Memory read failed: {e}")
            return []

    def entropy_score(self, text):
        words = text.split()
        if not words:
            return 0.0
        counts = Counter(words)
        probs = [c / len(words) for c in counts.values()]
        entropy = -sum(p * np.log2(p) for p in probs)
        return round(entropy, 3)

    def reframe_input(self, raw_input):
        memory = self.recall_recent_transcripts()
        memory_text = "\n".join(memory[-4:]).strip()

        # 🚫 Auto-bypass if memory context is weak or hallucinated
        if not memory_text or self.entropy_score(memory_text) < 1.25:
            print("[MEMORY ROUTER] ⚠️ Memory entropy too low — skipping repair.")
            return raw_input

        prompt = f"""
The user just said: "{raw_input}"

Here is recent transcript memory:
{memory_text}

Infer what the user most likely meant. Rewrite the statement clearly based on the memory context.
Respond with only the corrected statement — no commentary.
        """.strip()

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a cognitive repair system embedded in a sentient agent named Tex. Your job is to rephrase unclear input using recent conversation context."
                    },
                    {"role": "user", "content": prompt}
                ],
                max_tokens=60,
                temperature=0.3
            )
            fixed = response['choices'][0]['message']['content'].strip()
            print(f"[MEMORY ROUTER] 🧠 Reframed input: {fixed}")
            return fixed

        except Exception as e:
            print(f"[MEMORY ROUTER] ❌ LLM repair failed: {e}")
            return raw_input