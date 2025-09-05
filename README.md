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
