# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/memory_weaver.py
# Purpose: Tier 5 AGI Narrative Memory Engine — Strategic Threading of Cognitive Episodes
# ============================================================

from core_layer.memory_engine import recall_all
from core_layer.tex_manifest import TEXPULSE
from sentence_transformers import SentenceTransformer, util
from datetime import datetime
from collections import defaultdict
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def weave_narrative_threads(memory_key="tex", top_k=3, similarity_threshold=0.75):
    all_entries = recall_all(memory_key)
    if not all_entries:
        print("[WEAVER] ⚠️ No memory entries found.")
        return []

    explanations, timestamps, emotions, urgencies, coherences = [], [], [], [], []
    for entry in all_entries:
        if "explanation" in entry.get("data", {}):
            explanations.append(entry["data"]["explanation"])
            timestamps.append(entry.get("timestamp", ""))
            emotions.append(entry.get("data", {}).get("emotion", TEXPULSE.get("emotional_state")))
            urgencies.append(entry.get("data", {}).get("urgency", TEXPULSE.get("urgency")))
            coherences.append(entry.get("data", {}).get("coherence", TEXPULSE.get("coherence")))

    if not explanations:
        print("[WEAVER] ⚠️ No explanations found in memory.")
        return []

    embeddings = model.encode(explanations, convert_to_tensor=True)
    similarity_matrix = util.pytorch_cos_sim(embeddings, embeddings).cpu().numpy()

    threads = defaultdict(list)
    visited = set()
    for idx, sim_row in enumerate(similarity_matrix):
        if idx in visited:
            continue
        thread = [idx]
        for jdx, score in enumerate(sim_row):
            if score > similarity_threshold and jdx != idx and jdx not in visited:
                thread.append(jdx)
                visited.add(jdx)
        visited.add(idx)

        threads[f"thread_{len(threads)+1}"] = [{
            "text": explanations[i],
            "timestamp": timestamps[i],
            "emotion": emotions[i],
            "urgency": urgencies[i],
            "coherence": coherences[i],
            "score": round(similarity_matrix[idx][i], 3)
        } for i in thread]

    # Score threads by weighted coherence × urgency × size
    def thread_weight(entries):
        if not entries: return 0
        total = 0
        for e in entries:
            coherence = e.get("coherence", 0.6)
            urgency = e.get("urgency", 0.6)
            total += (coherence * 0.5 + urgency * 0.5)
        return total * len(entries)

    sorted_threads = sorted(threads.items(), key=lambda x: thread_weight(x[1]), reverse=True)

    top_threads = []
    for tid, entries in sorted_threads[:top_k]:
        top_threads.append({
            "thread_id": tid,
            "emotional_pulse": _summarize_emotion(entries),
            "urgency_avg": round(np.mean([e["urgency"] for e in entries]), 2),
            "coherence_avg": round(np.mean([e["coherence"] for e in entries]), 2),
            "entries": entries
        })

    return top_threads

def _summarize_emotion(entries):
    """Determine dominant emotion and volatility of a memory thread."""
    emotion_count = defaultdict(int)
    for e in entries:
        emotion_count[e["emotion"]] += 1
    if not emotion_count:
        return {"dominant": "neutral", "volatility": 0}
    dominant = max(emotion_count, key=emotion_count.get)
    volatility = round(len(set([e["emotion"] for e in entries])) / len(entries), 2)
    return {"dominant": dominant, "volatility": volatility}

# === Usage Example
if __name__ == "__main__":
    print("[WEAVER] 🧵 Generating memory threads...")
    threads = weave_narrative_threads(top_k=3)
    for thread in threads:
        print(f"\n🧵 {thread['thread_id']} | Dominant Emotion: {thread['emotional_pulse']['dominant']} | Volatility: {thread['emotional_pulse']['volatility']}")
        for entry in thread["entries"]:
            print(f"   → {entry['timestamp']} | {entry['emotion']} | {entry['text']}")