# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_cognitive_audit.py
# Purpose: Master Sweep — Full Capability Audit of Tex AGI System
# ============================================================

import os
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path().resolve()

all_files = [
    f for f in PROJECT_ROOT.rglob("*.py")
    if "site-packages" not in str(f)
    and "venv" not in str(f)
    and "tex_env" not in str(f)
    and "env" not in str(f)
    and "__pycache__" not in str(f)
]

# === TOTAL RECALL ROOT SCAN ===
# These are hardcoded anchors from your full file tree
root_files = [
    # Engine + Entry
    "tex_engine/tex_brain.py",
    "tex_engine/run_tex.py",
    "tex_orchestrator.py",
    "tex_runtime_orchestrator.py",

    # Core AGI Modules
    "core_agi_modules/tex_conversational_brain.py",
    "core_agi_modules/agent_spawner.py",
    "core_agi_modules/reflex_engine.py",
    "core_agi_modules/environmental_reflex_engine.py",
    "core_agi_modules/future_forecaster.py",

    # Core Layer + Memory
    "core_layer/memory_engine.py",
    "core_layer/goal_engine.py",
    "core_layer/tex_manifest.py",
    "core_layer/tex_vector_forge.py",
    "core_layer/meta_awareness_bridge.py",
    "core_layer/tex_explainer.py",

    # Voice + Real-time
    "tex_voiceos/tex_reasoning_engine.py",
    "tex_voiceos/voice_output_speaker.py",
    "tex_voiceos/semantic_intent_parser.py",

    # Children / AEI
    "tex_children/child_manager.py",
    "tex_children/aeondelta.py",
    "tex_children/variant_specializer.py",

    # Evolution + Mutation
    "evolution_layer/self_mutator.py",
    "evolution_layer/tex_shadowlab.py",
    "evolution_layer/tex_rebirth_daemon.py",

    # Swarm
    "swarm_layer/swarm_strategy_arbitrator.py",
    "swarm_layer/signal_entropy_checker.py",

    # Quantum Layer
    "quantum_layer/tex_quantum_spawn.py",
    "quantum_layer/qaoa_optimizer.py",
    "quantum_layer/qnn_model.py",

    # Strategy + Finance Orchestration
    "finance/strategy/tex_master_orchestrator.py",
    "finance/strategy/tex_orchestrator_part_a.py",
    "finance/strategy/tex_orchestrator_part_b.py",

    # All finance subsystems
    "finance/execution/market_action_engine.py",
    "finance/execution/market_strategy_driver.py",
    "finance/forecasting/future_tree_generator.py",
    "finance/forecasting/future_emotional_simulator.py",
    "finance/forecasting/future_simulator.py",
    "finance/forecasting/future_causal_simulator.py",
    "finance/forecasting/strategic_foresight_engine.py",
    "finance/memory/future_memory.py",
    "finance/memory/future_meta_memory.py",
    "finance/memory/meta_coherence_memory.py",
    "finance/multiworld/multiworld_reasoner.py",
    "finance/multiworld/multiworld_memory.py",
    "finance/multiworld/recursive_paradox_resolver.py",
    "finance/sentiment/emotional_liquidity_engine.py",
    "finance/sentiment/market_mood_sensor.py",
    "finance/risk/risk_assessment_module.py",
    "finance/strategy/alpha_explainer.py",
    "finance/strategy/portfolio_thinker.py",
    "finance/strategy/alpha_mimic_detector.py",
    "finance/strategy/alpha_signal_fuser.py",
    "finance/strategy/alpha_fusion_engine.py",
    "finance/strategy/alpha_paradox_engine.py",
    "finance/strategy/future_decision_engine.py",
    "finance/strategy/future_branch_optimizer.py",
    "finance/strategy/strategy_scoring.py",
    "finance/strategy/strategy_variant_simulator.py",
    "finance/strategy/market_distortion_circuit.py",
    "finance/strategy/insider_ghost_inference.py",
    "finance/strategy/reflexive_action_modeler.py",
    "finance/strategy/synthetic_adversary_arena.py",
    "finance/strategy/strategy_creator.py",
    "finance/strategy/neuro_counterpunch_dashboard.py"
]

activated = set()
queue = set(root_files)

while queue:
    current = queue.pop()
    activated.add(current)
    path = PROJECT_ROOT / current
    if not path.exists():
        continue
    try:
        with open(path) as f:
            lines = f.readlines()
            for line in lines:
                if "import" in line and "from" in line and not line.strip().startswith("#"):
                    parts = line.split("from")[1].split("import")[0].strip().replace(".", "/")
                    module_path = parts + ".py"
                    for f2 in all_files:
                        if module_path in str(f2):
                            rel_path = str(f2.relative_to(PROJECT_ROOT))
                            if rel_path not in activated:
                                queue.add(rel_path)
    except Exception as e:
        print(f"[⚠️] Failed to scan: {current} — {e}")

print("\n🧠 TEX FULL SYSTEM AUDIT — MAY 2, 2025")
print("🕓 Timestamp:", datetime.utcnow().isoformat())
print("----------------------------------------")
print("\n✅ ACTIVE MODULES (CONNECTED TO CORE):")
for f in sorted(activated):
    print("  ", f)

print("\n🟥 DORMANT OR UNUSED MODULES:")
for f in sorted(all_files):
    rel = str(f.relative_to(PROJECT_ROOT))
    if rel not in activated:
        print("  ", rel)

print("\n📦 Total scanned:", len(all_files))
print("✅ Connected:", len(activated))
print("🟥 Unused:", len(all_files) - len(activated))