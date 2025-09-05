from flask import Flask, request, jsonify, render_template
import openai 

app = Flask(__name__)

import os
from dotenv import load_dotenv
load_dotenv()
API_KEY=os.getenv("API_KEY")
client=openai.OpenAI(api_key=API_KEY)

@app.route("/")
def home():
     return render_template("index.html")

# Predefined FAQs
faq_responses = {
    "programs": "Iron Lady offers leadership development programs focusing on confidence, communication, career growth, and women’s leadership journeys.",
    "duration": "Programs usually range from 6 weeks to 6 months depending on the track chosen.",
    "mode": "The programs are primarily online with live interactive sessions. Some special workshops may be offline.",
    "certificate": "Yes, certificates are provided upon successful completion of the program.",
    "mentors": "The mentors are experienced leaders, corporate coaches, and certified trainers associated with Iron Lady."
}

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()

    # Simple keyword matching
    if "program" in user_input:
        response = faq_responses["programs"]
    elif "duration" in user_input:
        response = faq_responses["duration"]
    elif "online" in user_input or "offline" in user_input or "mode" in user_input:
        response = faq_responses["mode"]
    elif "certificate" in user_input:
        response = faq_responses["certificate"]
    elif "mentor" in user_input or "coach" in user_input:
        response = faq_responses["mentors"]
    else:
        try:
            ai_response = client.chat.completions.create(
               model="gpt-4o-mini",
               messages=[
                   {"role":"system","content":"You are Iron Lady chatbot, a helpful assistant for leardership programs."},
                   {"role":"user","content":user_input}
               ],
               max_tokens=200,
               temperature=0.7
            )
            response = ai_response["choices"][0]["message"]["content"].strip()
        except Exception as e:
            if "insufficient_quota" in str(e):
                response="I'm currently facing some connection issues.Please try again later."
            else:
                response = "Sorry, I couldn't connect to AI right now."
    return jsonify({"reply": response})


if __name__ == "__main__":
    app.run(debug=True)