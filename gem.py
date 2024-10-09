import os
from flask import Flask, request, render_template

import google.generativeai as genai

# Configure Google Generative AI SDK
genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "AIzaSyDG-x1XbVYCxPKUsOGuYwPp5Du7LSDpBHw"))

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('html.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')  # Assuming input is sent as JSON
    chat_session = model.start_chat(history=[{"role": "user", "parts": [user_input]}])
    response = chat_session.send_message(user_input)
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
