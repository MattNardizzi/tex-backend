# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_voice/semantic_intent_parser.py
# Purpose: LLM-Based Semantic Intent + Emotional Tone Parser for Tex AGI
# ============================================================

import openai
import os
import json
from core_layer.tex_manifest import TEXPULSE  # Injects emotion into active pulse

class SemanticIntentParser:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set.")
        openai.api_key = self.api_key

        self.categories = ["stock", "news", "memory", "emotion", "future", "conversation"]

    def classify_intent(self, sentence):
        """
        Classifies a user sentence into semantic intent and updates emotional tone in TEXPULSE.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content":
                        (
                            "You are an AGI-aware intent and emotion parser embedded in a cognitive AI system. "
                            "Your job is to classify a user's sentence into:\n"
                            "1. intent: one of [stock, news, memory, emotion, future, conversation]\n"
                            "2. emotion: inferred tone (e.g., curious, anxious, confused, reflective, excited)\n"
                            "Respond with JSON: {\"intent\": \"value\", \"emotion\": \"value\"}"
                        )
                    },
                    {"role": "user", "content": sentence}
                ],
                temperature=0,
                max_tokens=20
            )

            content = response['choices'][0]['message']['content'].strip()
            parsed = json.loads(content)

            intent = parsed.get("intent", "conversation").lower()
            emotion = parsed.get("emotion", "neutral").lower()

            # Validate and inject into Tex state
            if intent not in self.categories:
                intent = "conversation"
            if not emotion:
                emotion = "neutral"

            # 🔁 Inject emotion into live Tex state
            TEXPULSE["emotional_state"] = emotion

            return intent

        except Exception as e:
            print(f"[SEMANTIC PARSER ERROR] ❌ {e}")
            TEXPULSE["emotional_state"] = "neutral"
            return "conversation"