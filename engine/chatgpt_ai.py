# engine/chatgpt_ai.py
from openai import OpenAI
import os

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_chatgpt(prompt):
    """
    Send a user prompt to ChatGPT and return the response.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-5",  # fast + smart
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful and intelligent AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        answer = response.choices[0].message.content
        return answer

    except Exception as e:
        return f"Error: {e}"

# chat bot 
# def chatBot(query):
#     user_input = query.lower()
#     chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
#     id = chatbot.new_conversation()
#     chatbot.change_conversation(id)
#     response =  chatbot.chat(user_input)
#     print(response)
#     speak(response)
#     return response