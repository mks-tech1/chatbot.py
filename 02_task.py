import datetime

# Small knowledge base
knowledge_base = {
    "what is ai": "AI stands for Artificial Intelligence. It is the simulation of human intelligence in machines.",
    "what is machine learning": "Machine Learning is a subset of AI that allows systems to learn from data.",
    "what is python": "Python is a popular programming language known for its simplicity.",
    "who are you": "I am a simple rule-based chatbot."
}

# Intent patterns
greetings = ["hi", "hello", "hey", "hii"]
help_intents = ["help", "support", "assist"]
small_talk = ["how are you", "what's up", "how is it going"]

# Function to log conversation
def log_conversation(user, bot):
    with open("chat_log.txt", "a") as file:
        time = datetime.datetime.now()
        file.write(f"[{time}] User: {user}\n")
        file.write(f"[{time}] Bot: {bot}\n")

# Function to generate chatbot response
def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in greetings:
        return "Hello! How can I help you?"

    elif user_input in help_intents:
        return "I can help with AI, Machine Learning, and Python related questions."

    elif user_input in small_talk:
        return "I'm doing great! Thanks for asking 😊"

    elif user_input in knowledge_base:
        return knowledge_base[user_input]

    elif user_input == "exit":
        return "Goodbye! Have a nice day 👋"

    else:
        return "Sorry, I didn't understand that."

# Main program loop
print("🤖 Chatbot started! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    bot_reply = chatbot_response(user_input)

    print("🤖 Chatbot:", bot_reply)
    log_conversation(user_input, bot_reply)

    if user_input.lower() == "exit":
        break
