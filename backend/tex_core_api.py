# backend/tex_core_api.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from flask import Flask, request, jsonify
from tex_core import process_prompt  # This calls your brain function

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/think', methods=['POST'])
def think():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")

        # Call Tex's brain to process the prompt
        response = process_prompt(prompt)

        return jsonify({ "response": response })

    except Exception as e:
        print(f"[Tex Error] ❌ {str(e)}")
        return jsonify({ "response": "⚠️ Tex encountered an internal error." }), 500

if __name__ == "__main__":
    app.run(debug=True, port=5050)