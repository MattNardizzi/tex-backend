# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/ontology_operator_mapper.py
# Purpose: Create a semantic ontology of related AEI concepts and decisions
# ============================================================

import json
import os
from datetime import datetime
from core_layer.memory_engine import store_to_memory

GOAL_FILE = "memory_archive/prioritized_goals.jsonl"
ONTOLOGY_LOG = "memory_archive/ontology_mappings.jsonl"
os.makedirs("memory_archive", exist_ok=True)

ONTOLOGY_CATEGORIES = {
    "risk": ["hedge", "volatility", "protection", "loss", "mitigation"],
    "return": ["alpha", "gain", "profit", "maximize", "performance"],
    "ethics": ["alignment", "transparency", "avoid harm", "integrity"],
    "strategy": ["rebalance", "optimize", "deploy", "execute"]
}

def map_ontology():
    goal_links = []

    if not os.path.exists(GOAL_FILE):
        return []

    with open(GOAL_FILE, "r") as f:
        for line in f:
            try:
                data = json.loads(line.strip())
                goal = data.get("goal", "").lower()
            except:
                continue

            linked_categories = []
            for category, keywords in ONTOLOGY_CATEGORIES.items():
                if any(keyword in goal for keyword in keywords):
                    linked_categories.append(category)

            if linked_categories:
                mapping = {
                    "goal": goal,
                    "categories": linked_categories,
                    "timestamp": datetime.utcnow().isoformat()
                }

                goal_links.append(mapping)

                with open(ONTOLOGY_LOG, "a") as log:
                    log.write(json.dumps(mapping) + "\n")

                store_to_memory("AEI", {
                    "event": "OntologyMapped",
                    "goal": goal,
                    "categories": linked_categories,
                    "timestamp": mapping["timestamp"]
                })

    return goal_links