import os
import requests
from pydub import AudioSegment
from pydub.playback import play
import io

# === CONFIGURATION ===
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "V10bRch2AfjOrB1Yjsuf"  # Testing Rachel

def speak_test(text):
    if not ELEVENLABS_API_KEY:
        print("[ERROR] No API key detected. Export it first.")
        return

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg"
    }
    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 0.75
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload, stream=True)

        if response.status_code == 200:
            audio_bytes = b''.join(response.iter_content(chunk_size=1024))
            audio_segment = AudioSegment.from_file(io.BytesIO(audio_bytes), format="mp3")
            print("[VOICE] 🔊 Playing Tex voice...")
            play(audio_segment)

        else:
            print(f"[VOICE ERROR] ❌ Status {response.status_code}: {response.text}")

    except Exception as e:
        print(f"[VOICE ERROR] ❌ {e}")

if __name__ == "__main__":
    print("Tex Voice Manual Test Mode")
    user_text = input("Type something for Tex to say: ")
    speak_test(user_text)