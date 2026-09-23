import os
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

chat = client.chats.create(model="gemini-2.5-flash")

print("AI Chatbox shuru ho gaya hai! Baatcheet khatam karne ke liye 'exit' likhein.\n")

while True:
    user_input = input("Aap: ")
    if user_input.lower() == "exit":
        print("Alvida!")
        break
    response = chat.send_message(user_input)
    print(f"\nAI: {response.text}\n")