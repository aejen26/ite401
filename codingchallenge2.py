responses = {
    "hello": "Hi there! How can I assist you today?",
    "bye": "Goodbye! Have a great day!",
    "tell me about python": "Python is a popular programming language known for its simplicity and readability.",
    "tell me about yourself": "I am a Chatbot.",
    "default": "I'm sorry, I didn't quite understand that. Could you please clarify?"
}

def get_bot_response(user_message):
    user_message = user_message.lower()
    
    if user_message in responses:
        return responses[user_message]
    else:
        return responses["default"]

def main():
    print("Welcome to the chatbot! I can help you with some basic queries. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "bye":
            print("Bot: Goodbye! Have a great day.")
            break
        
        bot_response = get_bot_response(user_input)
        
        print(f"Bot: {bot_response}")

    print("Bot: The chat has ended. Farewell!")

if __name__ == "__main__":
    main()
