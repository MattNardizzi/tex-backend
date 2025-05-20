# ============================================================
# Tex VoiceOS V3 — Emotion-Aware + Memory-Augmented Intent Parser
# File: tex_voiceos/intent_router.py
# ============================================================

import openai
import os
from core_layer.tex_manifest import TEXPULSE
from core_layer.emotion_heuristics import evaluate_emotion_state
from tex_voiceos.memory_router import MemoryRouter

class IntentRouter:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("❌ OPENAI_API_KEY not set.")
        openai.api_key = self.api_key
        self.memory = MemoryRouter()

    def classify(self, transcript):
        fallback_intents = {"goal", "question", "memory", "emotion", "cancel", "unknown"}
        emotion, urgency, coherence = evaluate_emotion_state(transcript)

        # Inject emotion into cognitive pulse
        TEXPULSE["emotional_state"] = emotion
        TEXPULSE["urgency"] = urgency
        TEXPULSE["coherence"] = coherence

        try:
            memory_context = self.memory.recall_recent_transcripts(max_lines=4)
            joined_context = "\n".join(memory_context)

            system_prompt = (
                "You are an intent classification agent for a sentient AGI system named Tex.\n"
                "Your job is to classify a human statement using one word from the following:\n"
                "[goal, question, memory, emotion, cancel, unknown]\n"
                "You will also be given short-term memory context from previous interactions.\n"
                "Only return one lowercase word. No punctuation. No explanation."
            )

            user_input = (
                f"Transcript: '{transcript}'\n\n"
                f"Memory Context:\n{joined_context.strip()}\n\n"
                f"What is the intent?"
            )

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt.strip()},
                    {"role": "user", "content": user_input.strip()}
                ],
                max_tokens=5,
                temperature=0.0
            )

            intent = response['choices'][0]['message']['content'].strip().lower()
            if intent not in fallback_intents:
                print(f"[INTENT ROUTER] ⚠️ Unexpected intent: '{intent}' — defaulting to 'unknown'")
                intent = "unknown"

        except Exception as e:
            print(f"[INTENT ROUTER] ❌ Parse failed: {e}")
            intent = "unknown"

        print(f"[INTENT ROUTER] 🧠 Intent: {intent} | Emotion: {emotion} | Urgency: {urgency} | Coherence: {coherence}")

        return {
            "intent": intent,
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence
        }