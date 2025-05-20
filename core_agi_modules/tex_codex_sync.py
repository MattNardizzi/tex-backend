# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# License: Private Intellectual Property – Not for distribution.
# ============================================================
# ============================================
# Tex Codex Sync – Runtime Rebinding to Manifest
# ============================================

import os
import hashlib
import datetime

class TexCodexSync:
    def __init__(self, codex_path="tex_codex_manifest.txt", audit_log="memory_archive/codex_audit.log"):
        self.codex_path = codex_path
        self.audit_log = audit_log
        self.last_sync_state = {}

    def _hash_file(self, path):
        try:
            with open(path, "rb") as f:
                data = f.read()
                return hashlib.sha256(data).hexdigest()
        except Exception:
            return None

    def validate_codex(self):
        if not os.path.exists(self.codex_path):
            print("[CODEX SYNC] ❌ Codex manifest not found.")
            return []

        with open(self.codex_path, "r") as f:
            lines = f.readlines()

        modules = [line.strip() for line in lines if line.strip() and not line.startswith("#")]
        checked = []

        for module_path in modules:
            result = self._check_module(module_path)
            checked.append(result)

        self._log_audit(checked)
        return checked

    def _check_module(self, module_path):
        status = {"path": module_path, "exists": False, "hash": None, "status": "missing"}

        if os.path.exists(module_path):
            h = self._hash_file(module_path)
            status.update({"exists": True, "hash": h, "status": "verified"})

            # Compare with last known hash if available
            if module_path in self.last_sync_state:
                if h != self.last_sync_state[module_path]:
                    status["status"] = "changed"
        return status

    def _log_audit(self, checked_modules):
        timestamp = datetime.datetime.now().isoformat()
        try:
            os.makedirs(os.path.dirname(self.audit_log), exist_ok=True)
            with open(self.audit_log, "a") as log:
                for mod in checked_modules:
                    line = f"{timestamp} | {mod['status'].upper()} | {mod['path']} | hash={mod['hash']}\n"
                    log.write(line)
        except Exception as e:
            print(f"[CODEX SYNC] ⚠️ Audit logging failed: {e}")

    def bind_to_manifest(self, tex_manifest):
        print("[CODEX SYNC] 🔗 Rebinding to manifest...")

        codex_files = self.validate_codex()
        active_modules = [m["path"] for m in codex_files if m["status"] in ("verified", "changed")]

        tex_manifest["codex_files"] = active_modules
        tex_manifest["last_codex_sync"] = datetime.datetime.now().isoformat()
        print(f"[CODEX SYNC] ✅ Bound {len(active_modules)} modules to TEXPULSE.")
        return tex_manifest

    def refresh(self):
        print("[CODEX SYNC] ♻️ Refreshing sync state...")
        validated = self.validate_codex()
        self.last_sync_state = {entry["path"]: entry["hash"] for entry in validated if entry["exists"]}
        return self.last_sync_state
    
    def validate_codex(self):
        return {
            "original": "if x > y: pass",
            "mutated": "if x >= y: pass"
        }