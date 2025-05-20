# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_voice/tex_llm_reasoner.py
# Purpose: Tiny LLM Reasoner for Tex Voice Understanding
# ============================================================

import openai
import os

class LLMReasoner:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set.")
        openai.api_key = self.api_key

    def classify_question(self, question_text):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a classification engine. Given a user's question, classify it into one of the following categories: [stock, news, memory, emotion, future, unknown]. Only output the category name. Nothing else."},
                    {"role": "user", "content": f"Classify: {question_text}"}
                ],
                temperature=0,
                max_tokens=10
            )
            classification = response['choices'][0]['message']['content'].strip().lower()
            return classification
        except Exception as e:
            print(f"[LLM Reasoner ERROR] ❌ {e}")
            return "unknown"