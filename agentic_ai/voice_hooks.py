# ============================================================
# agentic_ai/voice_hooks.py — Tex Mutation Trigger from Voice
# ============================================================

from evolution_layer.reflex_mutation import ReflexMutator

mutator = ReflexMutator()

def trigger_mutation(strategy="inject_empathy_node"):
    print(f"\n🧬 [VOICE HOOK] Forcing mutation: {strategy}")
    patch = {
        "strategy": strategy,
        "triggered_by": {
            "emotion": "voice_override",
            "urgency": 1.0,
            "coherence": 0.5
        }
    }
    mutator.apply_manual_patch(patch)
    return f"Mutation '{strategy}' has been applied."