# backend/tex_core_api.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, request, jsonify
from tex_core import process_prompt  # This calls your brain function

app = Flask(__name__)

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