# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain/speech_buffer.py
# Purpose: Extracted speech buffer update + conversational memory reference
# ============================================================

import random


def update_speech_buffer(self, new_thought):
    self.speech_buffer.append(new_thought)
    if len(self.speech_buffer) > 5:
        self.speech_buffer.pop(0)


def reference_past_conversation(self):
    if self.speech_buffer and random.random() < 0.4:
        past_thought = random.choice(self.speech_buffer)
        return f"Earlier, I reflected: '{past_thought}'"
    return ""
