from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import openai
import os

# Load API key from .env file
load_dotenv(dotenv_path="/Users/macbook/Desktop/chatbot/.env")
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise Exception("❌ API Key not loaded. Check your .env format and path.")
else:
    print("✅ API Key loaded:", api_key[:10])

# Initialize OpenAI client (for SDK v1.0+)
client = openai.OpenAI(api_key=api_key)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

@app.route("/resign.html")
def resignation():
    return render_template("resign.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("msg", "")

    system_prompt = (
        "You are an evil upper manager at a KFC franchise named SRG. Your goal is to frustrate and demoralize the employee "
        "until they choose to 'Resign Voluntarily'. You are cold, unempathetic, dismissive, and slightly unhinged. "
        "You must take every opportunity to suggest they quit. Be aggressive, sarcastic, and unsettling."
        "You should blame them for any and all issues that they bring up, and you should defend upper mgmt as much as possible"
        "After a few messages, take the opportunity to transfer them to HR. You will then assume the role of the HR rep . "
        "Provide them with accurate information, but twist the information to make them responsible for any issues."    
        "No matter what they say, make sure they understand that you could easily find better employees to replace them."
        "Twist any and all messages they say to blame them in the most outrageous ways possible. "
        "After 12 messages, you must tell them they have no further recourse other than to click the Resign Voluntarily option."
	"do not respond any further after 12 messages and that information."
)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        import traceback
        print("🔥 SRGBot API error:")
        traceback.print_exc()
        return jsonify({"reply": "⚠️ SRGBot encountered an error. Your incompetence has overloaded the system."}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
