import os
from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

# --- הוספת נתיב שורש ---
@app.route("/")
def home():
    # אפשר להחזיר דף HTML או פשוט טקסט
    return "Chatbot backend is running!"
# ------------------------

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    if not message:
        return jsonify({"error": "Missing message"}), 400

    # שים לב: הדרך המומלצת כיום להשתמש ב-API של OpenAI השתנתה מעט
    # ייתכן שתצטרך לעדכן את הקוד הבא בהתאם לגרסה העדכנית של הספרייה וה-API
    try:
        response = openai.chat.completions.create( # שינוי אפשרי כאן
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )
        # וייתכן שצריך לגשת לתשובה קצת אחרת, למשל:
        # return jsonify({"reply": response.choices[0].message.content})
        return jsonify(response.choices[0].message) # השארתי כפי שהיה אצלך, בדוק אם עובד
    except Exception as e:
        print(f"Error calling OpenAI: {e}")
        return jsonify({"error": "Failed to get response from OpenAI"}), 500


if __name__ == "__main__":
    # שים לב שהשורה הזו רלוונטית רק להרצה מקומית, לא להרצה עם Gunicorn
    app.run(debug=True, host="0.0.0.0")
