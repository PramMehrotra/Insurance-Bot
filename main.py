from flask import Flask, request, render_template_string
import openai

# Initialize Flask app
app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = "your_openai_api_key_here"

# Define the chatbot's behavior
def chatbot_response(user_input):
    # Define a prompt for the chatbot
    prompt = f"""
    You are an insurance policy assistant. Your job is to help users find the best insurance policy based on their needs.
    Ask relevant questions to understand their requirements and provide accurate information about available policies.

    User: {user_input}
    Assistant:
    """
    
    # Call OpenAI's GPT API
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use GPT-3.5 model
        prompt=prompt,
        max_tokens=150,  # Limit response length
        temperature=0.7,  # Control creativity (0 = strict, 1 = creative)
    )
    
    return response.choices[0].text.strip()

# Define the web interface
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form["user_input"]
        bot_response = chatbot_response(user_input)
        return render_template_string(
            """
            <h1>Insurance Policy Chatbot</h1>
            <form method="POST">
                <input type="text" name="user_input" placeholder="Ask me anything..." required>
                <button type="submit">Send</button>
            </form>
            <h2>Chatbot Response:</h2>
            <p>{{ bot_response }}</p>
            """,
            bot_response=bot_response
        )
    return render_template_string(
        """
        <h1>Insurance Policy Chatbot</h1>
        <form method="POST">
            <input type="text" name="user_input" placeholder="Ask me anything..." required>
            <button type="submit">Send</button>
        </form>
        """
    )

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
    
prompt = f"""
You are an insurance policy assistant. Here are some available policies:
- Health Insurance: Covers medical expenses. Premiums start at $50/month.
- Auto Insurance: Covers car accidents. Premiums start at $30/month.
- Life Insurance: Provides financial security for family. Premiums start at $20/month.

Ask relevant questions to understand the user's needs and recommend the best policy.

User: {user_input}
Assistant:
"""    

import requests

def get_insurance_data():
    url = "https://api.insurify.com/policies"  # Replace with actual API endpoint
    response = requests.get(url)
    return response.json()    