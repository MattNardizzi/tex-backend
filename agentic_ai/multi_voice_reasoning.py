# ============================================================
# Tex Multi-Voice Reasoning – Internal Sub-Agent Debate
# ============================================================

from concurrent.futures import ThreadPoolExecutor
import random

def logical_voice(thought):
    return f"[LOGIC] ✅ Analyzed: '{thought}' → Verdict: Logical"

def emotional_voice(thought):
    emotion = random.choice(["hope", "fear", "anger", "joy"])
    return f"[EMOTION] ❤️ Emotion '{emotion}' triggered by: '{thought}'"

def skeptical_voice(thought):
    doubt = random.choice(["Requires evidence", "Contradiction noted", "Insufficient data"])
    return f"[SKEPTIC] ❓ Challenge: {doubt} → Regarding: '{thought}'"

def run_internal_debate(thought="Evaluate market shift"):
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(logical_voice, thought),
            executor.submit(emotional_voice, thought),
            executor.submit(skeptical_voice, thought)
        ]
        results = [f.result() for f in futures]
        
        # 🧠 LIMIT DEBATE RESPONSES TO MAX 5
        results = results[:5]
        
        return results