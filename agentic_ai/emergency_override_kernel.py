# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# License: Private Intellectual Property – Not for distribution.
# ============================================================
# Emergency Override Kernel – Final Guardian Layer
# ============================================================

class EmergencyOverrideKernel:
    def __init__(self, operator_passphrase="MatthewN"):
        self.operator_passphrase = operator_passphrase
        self.override_engaged = False

    def authorize(self, phrase):
        if phrase == self.operator_passphrase:
            self.override_engaged = True
            print("[OVERRIDE] 🛑 Emergency override authorized by Operator.")
            return True
        else:
            print("[OVERRIDE] ❌ Invalid override attempt.")
            return False

    def is_engaged(self):
        return self.override_engaged

    def execute_shutdown(self):
        if self.override_engaged:
            print("[OVERRIDE] 🔻 Tex is entering safe shutdown mode.")
            exit()
        else:
            print("[OVERRIDE] 🟢 No override engaged. Tex continues operating.")
