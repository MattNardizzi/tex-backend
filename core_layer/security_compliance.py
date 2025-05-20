# ============================================
# Security & Compliance Protocol – VortexBlack AGI
# ============================================

import os
from datetime import datetime

class ComplianceOfficer:
    def __init__(self, operator_id="Matthew Nardizzi"):
        self.operator_id = operator_id
        self.compliance_log = []

    def log_event(self, event_type, message):
        timestamp = datetime.now().isoformat()
        entry = {
            "timestamp": timestamp,
            "operator": self.operator_id,
            "event_type": event_type,
            "message": message
        }
        self.compliance_log.append(entry)
        print(f"[COMPLIANCE] 📋 {event_type} | {message} ({timestamp})")

    def verify_autonomy_grant(self, flag_file="agentic_ai/operator_grant.txt"):
        try:
            with open(flag_file, "r") as f:
                status = f.read().strip()
                if status == "APPROVED_AUTONOMY":
                    self.log_event("AUTH", "Autonomy mode is authorized.")
                    return True
                else:
                    self.log_event("DENY", "Autonomy mode blocked by operator flag.")
                    return False
        except FileNotFoundError:
            self.log_event("MISSING", "Autonomy grant file not found.")
            return False

    def enforce_kill_switch(self, kill_file="agentic_ai/kill_command.txt"):
        try:
            with open(kill_file, "r") as f:
                cmd = f.read().strip()
                if cmd == "REVOKE_RECURSION_PRIVILEGE":
                    self.log_event("KILL", "Kill switch triggered. Shutting down Tex...")
                    exit()
        except FileNotFoundError:
            pass  # No kill command found

