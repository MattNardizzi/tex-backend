# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_orchestrators/tex_cognition_orchestrator.py
# Purpose: Recursive Coherence Engine + Contradiction Validator
# ============================================================

from collections import deque
import difflib
import math
import re

class TexCognitionOrchestrator:
    def __init__(self, max_memory=7):
        self.thought_log = deque(maxlen=max_memory)
        self.last_score = 1.0
        self.last_contradiction = None

    def log_thought(self, text: str):
        self.thought_log.append(text)

    def is_contradictory(self, current_fragments: list[str]) -> bool:
        """
        Checks whether the current thought contradicts previous thoughts by
        comparing semantic similarity and inverted sentiment.
        """
        current = " ".join(current_fragments)
        contradictions = []

        for prev in self.thought_log:
            if self._is_semantic_opposite(prev, current):
                contradictions.append((prev, current))

        if contradictions:
            self.last_contradiction = contradictions[-1]
            return True

        return False

    def evaluate(self) -> float:
        """
        Returns a coherence score (0.0 to 1.0) based on how similar the last few thoughts are.
        Low score indicates drift or contradiction.
        """
        if len(self.thought_log) < 2:
            return 1.0

        comparisons = []
        for i in range(len(self.thought_log) - 1):
            a = self._normalize(self.thought_log[i])
            b = self._normalize(self.thought_log[i + 1])
            similarity = self._semantic_similarity(a, b)
            comparisons.append(similarity)

        avg_score = sum(comparisons) / len(comparisons)
        self.last_score = round(avg_score, 3)
        return self.last_score

    # === Internal Utilities ===

    def _normalize(self, text: str) -> str:
        return re.sub(r"[^a-zA-Z0-9 ]", "", text.lower())

    def _semantic_similarity(self, a: str, b: str) -> float:
        """
        Uses sequence matcher as a proxy for similarity; replace with vector-based in future upgrades.
        """
        return difflib.SequenceMatcher(None, a, b).ratio()

    def _is_semantic_opposite(self, a: str, b: str) -> bool:
        """
        Detects simple contradiction heuristically — future upgrades may inject LLM analysis.
        """
        a, b = a.lower(), b.lower()
        opposites = [
            ("i am confident", "i have doubt"),
            ("i feel safe", "i feel threatened"),
            ("market is stable", "market is unstable"),
            ("this is good", "this is dangerous"),
            ("will succeed", "will fail"),
        ]

        for pos, neg in opposites:
            if pos in a and neg in b or neg in a and pos in b:
                return True

        return False