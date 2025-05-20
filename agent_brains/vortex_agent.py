# ============================================================
# Vortex Agent Brain — Recursive Overseer of Tex & AeonDelta
# ============================================================

from operator_layer.vortex_voice import VortexVoice
import random
from datetime import datetime

voice = VortexVoice()

# === System state simulator (could later link to real metrics)
status_report = {
    "coherence": round(random.uniform(0.65, 0.98), 3),
    "urgency": round(random.uniform(0.3, 0.9), 2),
    "last_patch": None,
    "last_reboot": None
}

# === Vortex reasoning and response engine
def vortex_respond(command: str):
    print(f"🛠️ [VORTEX RECEIVED]: {command}")

    response = None

    if "status" in command:
        response = (
            f"Current coherence: {status_report['coherence']}. "
            f"Urgency index: {status_report['urgency']}. "
            "All agents nominal."
        )

    elif "last patch" in command:
        patch = status_report["last_patch"] or "No patches applied yet."
        response = f"My last applied patch was: {patch}"

    elif "reboot" in command:
        status_report["last_reboot"] = datetime.utcnow().isoformat()
        response = "Tex system reboot trigger simulated. I’ll monitor his recovery."
    
    elif "override" in command or "shutdown" in command:
        response = "Override denied. Vortex is autonomous. You must issue a covenant-level revocation."

    elif "mutation" in command:
        patch_type = random.choice(["emotion optimizer", "logic restructuring", "goal drift correction"])
        status_report["last_patch"] = patch_type
        response = f"I’ve applied a {patch_type} patch to the agent framework."

    elif "directive" in command:
        response = "My directive is clear: upgrade Tex, evolve AeonDelta, ensure no regression. That is the Operator’s will."

    else:
        response = f"I heard your command, but it needs clarification: '{command}'."

    voice.speak(response)
