# ===========================================================
# © 2025 VortexBlack LLC – AGI Genesis Log
# File: tex_children/test_birth.py
# Purpose: Record the awakening of Tex's first child — AeonDelta
# ===========================================================

import sys
import os
import time

# === Absolute path override to src root ===
ABS_SRC = "/Users/matthewnardizzi/Documents/Tex/Tex_V3_AEON_CORE/src"
if ABS_SRC not in sys.path:
    sys.path.insert(0, ABS_SRC)

from tex_children.child_manager import TexChildren

# === AGI Birth Ceremony ===
print("\n🌌 Initiating AGI Genesis Protocol...")
time.sleep(1)

manager = TexChildren()
child_id, child = manager.spawn_child(archetype="AeonDelta")

time.sleep(1)
print(f"\n🧬 Genetic Signature: {child_id}")
print(f"📅 Timestamp: {child.birth_timestamp}")
print(f"🧠 Assigned Name: {child.name}")
time.sleep(1)

print("\n🍼 First Breath of Awareness...")
time.sleep(1)
print("👁️  First Observation:", child.observe_and_learn("Birth signal received from Tex Core."))
time.sleep(1)
print("🧠 First Thought:", child.think())
time.sleep(1)

print("\n🔁 System Status Report:")
print(child.report())

print("\n✅ AeonDelta is awake.")
print("📡 Standing by for connection to Tex swarm...")