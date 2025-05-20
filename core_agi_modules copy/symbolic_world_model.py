# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/symbolic_world_model.py
# Purpose: AGI-grade Symbolic World Model (Visual, Spatial, and Semantic Reasoning)
# ============================================================

from collections import defaultdict
import uuid
import datetime

class SymbolicWorldModel:
    def __init__(self):
        self.entities = {}  # e.g. {'Tex': {'type': 'agent', 'location': 'lab'}}
        self.relations = defaultdict(list)  # e.g. {'Tex': [('inside', 'lab')]}
        self.history = []  # Temporal log of changes

    def register_entity(self, name, properties=None):
        if name not in self.entities:
            self.entities[name] = properties or {}
            self._log(f"Entity registered: {name} | Properties: {self.entities[name]}")

    def add_relation(self, subject, relation, obj):
        self.relations[subject].append((relation, obj))
        # Handle symmetrical spatial reasoning
        if relation == "north_of":
            self.relations[obj].append(("south_of", subject))
        elif relation == "south_of":
            self.relations[obj].append(("north_of", subject))
        elif relation == "east_of":
            self.relations[obj].append(("west_of", subject))
        elif relation == "west_of":
            self.relations[obj].append(("east_of", subject))
        self._log(f"Relation added: {subject} {relation} {obj}")

    def move_entity(self, name, new_location):
        old_location = self.entities.get(name, {}).get("location")
        self.entities[name]["location"] = new_location
        self._log(f"{name} moved from {old_location} to {new_location}")

    def describe_entity(self, name):
        props = self.entities.get(name, {})
        rels = self.relations.get(name, [])
        desc = [f"{name} is a {props.get('type', 'thing')}."]
        if "location" in props:
            desc.append(f"Located in {props['location']}.")
        for r, o in rels:
            desc.append(f"{name} is {r} {o}.")
        return " ".join(desc)

    def explain_world(self):
        lines = []
        for entity in self.entities:
            lines.append(self.describe_entity(entity))
        return " ".join(lines)

    def query_relations(self, subject):
        return self.relations.get(subject, [])

    def _log(self, event):
        self.history.append({
            "id": str(uuid.uuid4()),
            "timestamp": str(datetime.datetime.utcnow()),
            "event": event
        })

    def get_change_history(self, limit=10):
        return self.history[-limit:]

    def reset_world(self):
        self.entities = {}
        self.relations = defaultdict(list)
        self.history = []
        self._log("World model reset.")
