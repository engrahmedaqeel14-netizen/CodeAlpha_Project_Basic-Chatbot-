"""
Basic Rule-Based Chatbot
Concepts: if-elif, functions, loops, input/output
"""

def get_response(user_input):
    text = user_input.lower().strip()

    # Greetings
    if any(word in text for word in ["hello", "hi", "hey", "howdy", "sup"]):
        return "Hi there! 👋 How can I help you?"

    # How are you
    elif any(phrase in text for phrase in ["how are you", "how r you", "how are u", "hows it going", "how do you do"]):
        return "I'm doing great, thanks for asking! 😊 How about you?"

    # User says they're good
    elif any(word in text for word in ["good", "fine", "great", "awesome", "wonderful", "nice", "not bad"]):
        return "That's wonderful to hear! 🎉"

    # User says they're not good
    elif any(word in text for word in ["sad", "bad", "terrible", "awful", "not good", "not well", "upset"]):
        return "I'm sorry to hear that. 😔 I hope things get better soon!"

    # What is your name
    elif any(phrase in text for phrase in ["your name", "who are you", "what are you"]):
        return "I'm PyBot 🤖 — your friendly Python chatbot!"

    # What can you do
    elif any(phrase in text for phrase in ["what can you do", "help", "commands", "options"]):
        return (
            "I can chat with you! Try saying:\n"
            "  • hello / hi / hey\n"
            "  • how are you\n"
            "  • what is your name\n"
            "  • tell me a joke\n"
            "  • what time is it\n"
            "  • bye / goodbye"
        )

    # Tell a joke
    elif any(phrase in text for phrase in ["joke", "funny", "make me laugh", "tell me a joke"]):
        import random
        jokes = [
            "Why do programmers prefer dark mode?\n  Because light attracts bugs! 🐛",
            "Why did the Python programmer wear glasses?\n  Because he couldn't C! 👓",
            "What do you call a programmer from Finland?\n  Nerdic! 😄",
            "Why do Java developers wear glasses?\n  Because they don't C#! 🤓",
        ]
        return random.choice(jokes)

    # What time is it
    elif any(phrase in text for phrase in ["time", "what time", "current time"]):
        from datetime import datetime
        now = datetime.now().strftime("%I:%M %p")
        return f"The current time is {now} ⏰"

    # Today's date
    elif any(phrase in text for phrase in ["date", "today", "what day"]):
        from datetime import datetime
        today = datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {today} 📅"

    # Thank you
    elif any(phrase in text for phrase in ["thank", "thanks", "thank you", "thx"]):
        return "You're welcome! 😊 Always happy to help!"

    # Bye
    elif any(word in text for word in ["bye", "goodbye", "see you", "later", "exit", "quit", "cya"]):
        return "GOODBYE"

    # Unknown input
    else:
        return "Hmm, I didn't quite understand that 🤔 Type 'help' to see what I can do!"


def print_banner():
    print("=" * 50)
    print("        Welcome to PyBot 🤖")
    print("   A Simple Rule-Based Python Chatbot")
    print("=" * 50)
    print("  Type 'help' for commands")
    print("  Type 'bye' to exit")
    print("=" * 50)
    print()


def chat():
    print_banner()

    while True:
        try:
            user_input = input("You   : ").strip()

            if not user_input:
                print("PyBot : Please type something! 😊\n")
                continue

            response = get_response(user_input)

            if response == "GOODBYE":
                print("PyBot : Goodbye! 👋 Have a great day!")
                print("=" * 50)
                break

            print(f"PyBot : {response}\n")

        except (KeyboardInterrupt, EOFError):
            print("\nPyBot : Goodbye! 👋 (Exit detected)")
            break


if __name__ == "__main__":
    chat()
