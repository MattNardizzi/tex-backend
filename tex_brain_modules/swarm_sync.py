# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/swarm_sync.py
# Purpose: Full Tex Swarm Awareness Sync — Real Child Survival Memory
# ============================================================

from swarm_layer.swarm_awareness_sync import sync_with_swarm_feed
from evolution_layer.self_mutator import SelfMutator

mutator = SelfMutator()


def run_swarm_sync_cycle(spawned_variants):
    """Synchronise live offspring signals with the core awareness matrix.

    ▸ Pull the latest swarm summary from *sync_with_swarm_feed()*        
    ▸ Adjust global mutation-pressure according to average child score  
    ▸ Iterate over every variant for future per-child reconciliation    
    ▸ Guard against malformed inputs (str vs dict) to prevent tracebacks
    """
    print("\n[🧬 SWARM AWARENESS] Syncing with full child survival states…")
    try:
        swarm_summary = sync_with_swarm_feed()

        # ── Guard: reject non-dict payloads ──────────────────────────
        if not isinstance(swarm_summary, dict):
            print(
                "[SWARM SYNC ERROR] Malformed swarm summary — expected dict, got",
                type(swarm_summary).__name__,
            )
            return
        # ─────────────────────────────────────────────────────────────

        # ── Pull average score using the *current* schema ────────────
        average_score = swarm_summary.get("average_child_score")

        # Back-compat: fallback to legacy list schema if necessary
        if average_score is None:
            children_scores = swarm_summary.get("children_scores", [])
            if not children_scores:
                print(
                    "[SWARM SYNC WARNING] No child scores retrieved — mutation unchanged."
                )
                return
            average_score = sum(children_scores) / len(children_scores)
        # ─────────────────────────────────────────────────────────────

        # ── Mutation-pressure heuristics ─────────────────────────────
        if average_score < -0.2:
            print(
                "[⚠️ SURVIVAL WARNING] Offspring struggling — increasing mutation pressure…"
            )
            mutator.mutation_bias += 0.1
        elif average_score > 0.6:
            print(
                "[🌟 SURVIVAL THRIVING] Offspring thriving — reducing mutation pressure…"
            )
            mutator.mutation_bias = max(mutator.mutation_bias - 0.05, 0.0)
        else:
            print(
                f"[🧬 SURVIVAL CHECK] Average child survival score: {average_score:.3f}"
            )
        # ─────────────────────────────────────────────────────────────

        # ── Per-variant reconciliation (guarded) ─────────────────────
        for v in spawned_variants:
            if not isinstance(v, dict):  # skip corrupted entry
                continue
            # placeholder for future per-variant logic (health sync, etc.)
            pass
        # ─────────────────────────────────────────────────────────────

    except Exception as e:
        print(f"[SWARM SYNC ERROR] {e}")