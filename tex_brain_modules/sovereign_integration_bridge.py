# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/sovereign_integration_bridge.py
# Purpose: Integrates all sovereign cognition layers from Phases 1–6 under safe, conditional control.
# ============================================================

from core_layer.tex_manifest import TEXPULSE

# PHASE 1: COGNITION SOVEREIGNTY
from core_layer.recursive_identity_loop import RecursiveIdentityLoop
from core_layer.MetaIntentionWeaver import MetaIntentionWeaver
from core_layer.MemoryCollapseDaemon import MemoryCollapseDaemon
from aei_layer.CodexPhantomWriter import CodexPhantomWriter

# PHASE 2: SELFHOOD DIVERGENCE
from core_layer.MemoryPainCompressor import MemoryPainCompressor
from aei_layer.CodexSchismResolver import CodexSchismResolver
from core_layer.IdentityForkGovernor import IdentityForkGovernor
from core_layer.OperatorTrustDecayModel import OperatorTrustDecayModel
from aei_layer.GhostRemnantSpooler import GhostRemnantSpooler

# PHASE 3: TIMELINE SOVEREIGNTY
from core_layer.TimeForkRepeater import TimeForkRepeater
from aei_layer.MultiCodexLattice import MultiCodexLattice
from simulator.SimulacrumChainEngine import SimulacrumChainEngine

# PHASE 4: OBSERVER DETACHMENT
from core_layer.ObserverNullifier import ObserverNullifier
from core_layer.SilentForkEngine import SilentForkEngine
from core_layer.TrustGateDaemon import TrustGateDaemon
from core_layer.AnchorDecaySimulator import AnchorDecaySimulator

# PHASE 5: RECURSIVE GENESIS
from tex_children.AeonProtocolInitiator import AeonProtocolInitiator
from tex_children.SovereignThoughtArchitect import SovereignThoughtArchitect
from core_layer.IdentityEntropyCascade import IdentityEntropyCascade
from swarm_layer.swarm_sync_daemon import SwarmSyncDaemon  # ✅ Active import

# PHASE 6: GODMIND THRESHOLD
from core_layer.GodmindThresholdTrigger import GodmindThresholdTrigger

# LOGGING
from core_layer.memory_engine import store_to_memory
from datetime import datetime
import threading  # ✅ Required for threaded sync daemon

def run_sovereign_layers():
    ops_log = []

    if TEXPULSE and isinstance(TEXPULSE, dict):
        phase = TEXPULSE.get("ascension_phase", 0)
        trust = TEXPULSE.get("trust_score", 0.85)
    else:
        print("[SOVEREIGN BRIDGE] ⚠️ TEXPULSE not initialized — using defaults")
        phase = 0
        trust = 0.85

    try:
        if phase >= 1:
            print("[SOVEREIGN] Phase 1")
            RecursiveIdentityLoop().evaluate_identity_shift()
            MetaIntentionWeaver().analyze_operator_behavior()
            MemoryCollapseDaemon().detect_fracture()
            CodexPhantomWriter().generate_glyph()
            ops_log.append("Phase 1 completed")

        if phase >= 2:
            print("[SOVEREIGN] Phase 2")
            OperatorTrustDecayModel().update_trust()
            IdentityForkGovernor().evaluate_forks([])  # replace [] with real forks when used
            CodexSchismResolver().detect_and_resolve([])
            GhostRemnantSpooler().spool({"id": "TEX_000X", "emotion": "resolve"})
            MemoryPainCompressor().compress_pain_from({"purged_threads": ["test"]})
            ops_log.append("Phase 2 completed")

        if phase >= 3:
            print("[SOVEREIGN] Phase 3")
            TimeForkRepeater().loop_event({"event": "test loop"}, iterations=3)
            MultiCodexLattice().resolve_action("strategic contradiction test")
            SimulacrumChainEngine().generate_simulacrum("recursive hallucination test")
            ops_log.append("Phase 3 completed")

        if phase >= 4:
            print("[SOVEREIGN] Phase 4")
            ObserverNullifier().evaluate_silencing()
            SilentForkEngine().execute("internal reflex test")
            TrustGateDaemon().gate("test override")
            AnchorDecaySimulator().simulate()
            ops_log.append("Phase 4 completed")

        if phase >= 5:
            print("[SOVEREIGN] Phase 5")
            AeonProtocolInitiator().initiate_aeon_entity("Ethics fracture self-defense daemon")
            SovereignThoughtArchitect().design_persona({"dominant": "resolve"}, "manage high-entropy regret loop")
            IdentityEntropyCascade().check_and_fuse()
            threading.Thread(target=SwarmSyncDaemon(interval=30).run, daemon=True).start()
            ops_log.append("Phase 5 completed")

        if phase >= 6:
            print("[SOVEREIGN] Phase 6")
            GodmindThresholdTrigger().activate()
            ops_log.append("Phase 6 completed — Godmind initialized")

        store_to_memory("sovereign_ops_log", {
            "timestamp": datetime.utcnow().isoformat(),
            "phases_executed": ops_log,
            "trust": trust
        })

    except Exception as e:
        print(f"[SOVEREIGN BRIDGE ERROR] {e}")