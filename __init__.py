from flask import Flask, request, jsonify
import openai
import os

def create_app():
    app = Flask(__name__)

    openai.api_key = os.getenv("OPENAI_API_KEY")

    @app.route("/", methods=["GET"])
    def index():
        return "ברוך הבא לצ'אטבוט!"

    @app.route("/chat", methods=["POST"])
    def chat():
        data = request.json
        prompt = data.get("prompt", "")
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            answer = response.choices[0].message["content"]
            return jsonify({"response": answer})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return app