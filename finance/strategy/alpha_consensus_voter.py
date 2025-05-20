class AlphaConsensusVoter:
    def vote(self, variants):
        return max(variants, key=lambda v: v.get("confidence", 0.5))