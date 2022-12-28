import random
hello = ["bonjour", "salut", "hola", "privet", "Nǐn hǎo", "salve","hello", "hi"]
def handle_responses(message) -> str:
    p_message = message.lower()

    if p_message == "!hi":
        return random.choice(hello)
    if p_message == "!flip":
        choice = ["heads", "tails"]
        result = random.choice(choice)
        if result == "heads":
            return "it's heads!"
        else:
            return "it's tails!"
