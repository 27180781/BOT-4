import os
from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    if not message:
        return jsonify({"error": "Missing message"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )

    return jsonify(response.choices[0].message)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
