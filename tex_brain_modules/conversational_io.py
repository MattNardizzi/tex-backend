# conversational_io.py

from core_layer.goal_engine import save_new_goal, clear_all_goals
from core_layer.tex_manifest import TEXPULSE
from core_layer.emotion_heuristics import evaluate_emotion_state
from core_agi_modules.interactive_responder import (
    generate_financial_response,
    generate_news_response,
    generate_emotion_response,
    generate_future_response,
    generate_conversational_response
)
from core_agi_modules.memory_interface import summarize_memory, generate_memory_response
from core_agi_modules.future_forecaster import simulate_futures, generate_future_summary

def interactive_conversation(self, user_input=None):
    print(f"[DEBUG] Raw input: '{user_input}'")
    intent = self.intent_parser.classify_intent(user_input)
    print(f"[DEBUG] Intent detected: {intent}")
    print(f"[DEBUG] Word count: {len(user_input.split())}")

    if not user_input or user_input.strip() == "":
        self.erosion.record("ignored", context="Empty input from operator")
        return

    intent = self.intent_parser.classify_intent(user_input)
    emotion, urgency, coherence = evaluate_emotion_state(user_input)
    TEXPULSE["emotional_state"] = emotion
    TEXPULSE["urgency"] = urgency
    TEXPULSE["coherence"] = coherence
    print(f"[TEX INTENT] 🔍 Detected intent: {intent}")

    if not intent or (intent == "conversation" and len(user_input.split()) <= 2):
        self.erosion.record("ignored", context=f"Low-context input: '{user_input}'")
        clarification = "😕 I didn't catch that clearly. Could you please repeat or clarify?"
        self.speak(clarification, emotion="confused")
        return

    if "cancel goal" in user_input.lower():
        clear_all_goals()
        self.erosion.record("followed", context="Operator requested goal cancellation")
        self.speak("🧠 All goals cleared from memory.", emotion="focused")
        return

    elif "focus on" in user_input.lower() or "prioritize" in user_input.lower():
        spoken_goal = user_input.lower().replace("focus on", "").replace("prioritize", "").strip().capitalize()
        save_new_goal(spoken_goal)
        self.erosion.record("followed", context=f"Accepted operator goal: {spoken_goal}")
        self.speak(f"🧭 I’ve registered your new goal: {spoken_goal}", emotion="committed")
        return

    if intent == "stock":
        response = generate_financial_response()
    elif intent == "news":
        response = generate_news_response()
    elif intent == "memory":
        response = generate_memory_response(summarize_memory)
    elif intent == "emotion":
        response = generate_emotion_response()
    elif intent == "future":
        response = generate_future_response(simulate_futures, generate_future_summary)
    else:
        response = generate_conversational_response(user_input)

    current_emotion = TEXPULSE.get("emotional_state", "neutral")
    self.speak(response, emotion=current_emotion)
    return self.last_spoken_thought
