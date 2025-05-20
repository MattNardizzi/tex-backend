# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/strategy/tex_master_orchestrator.py
# Purpose: Master controller to execute Part A + B of Tex AGI Brain
# ============================================================

from finance.strategy.tex_orchestrator_part_a import FinanceOrchestrator as OrchestratorPartA
from finance.strategy.tex_orchestrator_part_b import FinanceOrchestrator as OrchestratorPartB
class MasterTexOrchestrator:
    def __init__(self, brain):
        self.brain = brain  # ✅ Tex will pass himself in
        self.last_future_report = {}
        # Now pass brain to whatever orchestrators need it
        self.orch = OrchestratorPartA()

        # ✅ Inject Part B logic into Part A instance
        self.orch.run_cycle_part_b = OrchestratorPartB(self.brain).run_cycle_part_b.__get__(self.orch)

    def run_cycle(self):
        # Run part A (forecasting, alpha, branch selection)
        part_a_report, alpha, foresight, portfolio, ranked, futures = self.orch.run_cycle_part_a()

        # Run part B (reflex, reasoning, output)
        part_b_report = self.orch.run_cycle_part_b(alpha, foresight, portfolio, ranked, futures)

        # Merge both reports
        full_report = {**part_a_report, **part_b_report}
        return full_report

if __name__ == "__main__":
    tex = MasterTexOrchestrator()
    full = tex.run_cycle()
    for k, v in full.items():
        print(f"\n=== {k.upper()} ===\n{v}")