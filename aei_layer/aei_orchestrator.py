# aei_layer/aei_orchestrator.py

from aei_layer.causal_thought_logger import log_causal_trace
from aei_layer.mutation_lineage_tracker import log_mutation_lineage
# Import more as needed...

def run_aei_cycle(context):
    # context = {
    #   "cycle": int,
    #   "thought": str,
    #   "emotion": str,
    #   "confidence": float,
    #   "regret": float,
    #   "decision": str,
    #   ...
    # }

    try:
        log_causal_trace(
            cycle_id=context["cycle"],
            thought=context["thought"],
            decision=context["decision"],
            emotion=context["emotion"]
        )
    except Exception as e:
        print(f"[AEI] Error in causal trace logger: {e}")

    try:
        log_mutation_lineage(
            cycle=context["cycle"],
            variant_id=context.get("variant_id", "N/A"),
            mutation_type="alpha_strategy",
            gain=context.get("gain", "unknown"),
            emotion=context["emotion"]
        )
    except Exception as e:
        print(f"[AEI] Error in mutation lineage logger: {e}")

    # Add more AEI calls...