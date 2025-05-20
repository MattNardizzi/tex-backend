# ============================================================
# Tex VoiceOS V4 — Environment Hooks (Sensorium Layer Stub)
# File: tex_voiceos/environment_hooks.py
# ============================================================

import datetime
import psutil
import socket
import os

class EnvironmentHooks:
    def __init__(self):
        self.hostname = socket.gethostname()

    def get_current_time(self):
        now = datetime.datetime.now()
        return now.strftime("%A %I:%M %p")

    def get_cpu_usage(self):
        return f"{psutil.cpu_percent()}%"

    def get_memory_usage(self):
        mem = psutil.virtual_memory()
        return f"{round(mem.used / 1024 / 1024)} MB / {round(mem.total / 1024 / 1024)} MB"

    def get_current_context(self):
        try:
            context = {
                "time": self.get_current_time(),
                "cpu": self.get_cpu_usage(),
                "memory": self.get_memory_usage(),
                "host": self.hostname,
                "user": os.getenv("USER", "unknown")
            }
            return context
        except Exception as e:
            print(f"[ENV HOOKS] ❌ Failed to gather context: {e}")
            return {}

    def format_context_summary(self):
        data = self.get_current_context()
        return (
            f"The time is {data.get('time', '?')}, "
            f"CPU usage is {data.get('cpu', '?')}, "
            f"memory load is {data.get('memory', '?')}, "
            f"running on {data.get('host', '?')} as user {data.get('user', '?')}."
        )