print("Welcome to ChatBot! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you today?")
    elif "your name" in user_input:
        print("Bot: I'm a simple rule-based chatbot.")
    elif "how are you" in user_input:
        print("Bot: I'm just code, but I'm functioning as expected!")
    elif "weather" in user_input:
        print("Bot: I can't check the weather right now, but it's always sunny in the code world.")
    elif "bye" in user_input:
        print("Bot: Goodbye! Have a great day.")
        break
    else:
        print("Bot: I'm not sure how to respond to that. Can you rephrase?")
