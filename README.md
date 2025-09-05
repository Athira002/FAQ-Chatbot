# Iron Lady Chatbot 🤖

A simple chatbot built with **Flask + OpenAI API** that answers FAQs about Iron Lady's leadership programs, with AI-powered fallback for other queries.

## 🚀 Features
- Answers FAQs like:
  - What programs does Iron Lady offer?
  - What is the program duration?
  - Is the program online or offline?
  - Are certificates provided?
  - Who are the mentors/coaches?
- Falls back to **OpenAI GPT (gpt-3.5-turbo / gpt-4o-mini)** for other questions.
- Simple Flask backend + optional HTML/JS frontend.
- Graceful error handling if API quota is exceeded.

## 🛠️ Tech Stack
- Python
- Flask
- OpenAI API
- HTML/CSS/JS (for frontend)

## ⚡ How to Run
1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/chatbot.git
   cd chatbot
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Add your OpenAI API key inside app.py.
   - Create a .env file in the project folder:
     ```ini
     OPENAI_API_KEY=YOUR_API_KEY_HERE
   - Important: Do not share your real API key publicly.
   - You can copy .env.example and replace the placeholder:
     ```bash
     cp .env.example .env

5. Run the app:
   ```bash
   python app.py
6. Open http://127.0.0.1:5000 in your browser.

## 🔑 Note

- This project is safe to push to GitHub because the .env file is ignored in version control.
- Recruiters or other users need to create their own API key to run the chatbot.
 
## References

OpenAI API Documentation
