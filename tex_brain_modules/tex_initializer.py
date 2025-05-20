# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/tex_initializer.py
# Purpose: Initialization of Core Tex Cognitive Modules
# ============================================================

from evolution_layer.self_mutator import SelfMutator
from agentic_ai.self_reflective_loop import SelfReflectiveLoop
from agentic_ai.tex_awareness_sync import TexAwarenessSync
from operator_layer.vortex_operator import VortexRuntime
from quantum_layer.tex_quantum_spawn import QuantumTexSpawn
from tex_children.child_manager import TexChildren
from agentic_ai.agent_scorer import AgentScorer

# === Initialize Cognitive Systems ===

def initialize_mutator():
    return SelfMutator()

def initialize_reflector():
    return SelfReflectiveLoop()

def initialize_awareness():
    return TexAwarenessSync(operator_name="Vortex")

def initialize_vortex():
    return VortexRuntime(fingerprint="Vortex")

def initialize_spawner():
    return QuantumTexSpawn(num_clones=3)

def initialize_children():
    tex_children = TexChildren()
    child_id, aeondelta = tex_children.spawn_child(archetype="AeonDelta")
    return tex_children, child_id, aeondelta

def initialize_scorer():
    return AgentScorer()
