# Define a dictionary to store various responses for different queries
responses = {
    "hello": "Hi there! How can I assist you today?",
    "bye": "Goodbye! Have a great day!",
    "tell me about python": "Python is a popular programming language known for its simplicity and readability.",
    "tell me about yourself": "I am a Chatbot.",
    "default": "I'm sorry, I didn't quite understand that. Could you please clarify?"
}

# Function to process user input and provide the relevant response
def get_bot_response(user_message):
    # Convert user input to lowercase to ensure case-insensitive matching
    user_message = user_message.lower()
    
    # Check if the message exists in the responses dictionary
    if user_message in responses:
        return responses[user_message]
    else:
        return responses["default"]

# Main function to handle the interaction with the user
def main():
    print("Welcome to the chatbot! I can help you with some basic queries. Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check if user wants to exit
        if user_input.lower() == "bye":
            print("Bot: Goodbye! Have a great day.")
            break
        
        # Get bot response
        bot_response = get_bot_response(user_input)
        
        # Display the bot response
        print(f"Bot: {bot_response}")

    # After the loop exits, display a closing message
    print("Bot: The chat has ended. Farewell!")

# Call the main function to start the chatbot interaction
if __name__ == "__main__":
    main()
