def chatbot():
    print("🤖 Chatbot: Hello! I am a simple chatbot.")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello" or user == "hi":
            print("🤖 Chatbot: Hello! How can I help you?")

        elif user == "how are you":
            print("🤖 Chatbot: I am doing great. Thank you for asking!")

        elif user == "what is your name":
            print("🤖 Chatbot: My name is athili sathibabu.")

        elif user == "who created you":
            print("🤖 Chatbot: I was created using siddardha.")

        elif user == "help":
            print("🤖 Chatbot: You can ask me about my name, how I am, or say hello.")

        elif user == "bye":
            print("🤖 Chatbot: Goodbye! Have a nice day.")
            break

        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")

def main():
    chatbot()

if __name__ == "__main__":
    main()