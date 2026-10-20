# nolan 
# date 10-20-2026

from datetime import datetime  
AI_FACTS = [
    "AI can analyze large datasets quickly and accurately.",
    "AI can automate repetitive tasks and improve efficiency.",
    "AI can learn from data and improve its performance over time."
]


POSITIVE_WORDS = ["happy", "fine", "good", "excited", "awesome"]
NEGATIVE_WORDS = ["sad", "tired", "stressed", "pissed off", "angry"]
CALM_WORDS = ["fine", "okay", "ok", "meh"]


def greeting_for_hour(hour):
    if 5 <= hour < 12:
        return "Good afternoon!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    elif 18 <= hour < 22:
        return "Good evening!"
    else:
        return "Good night!"

def respond_to_mood(text):
    text_lower = text.lower()
    if any(word in text_lower for word in POSITIVE_WORDS):
        return "I'm glad to hear that!"
    elif any(word in text_lower for word in NEGATIVE_WORDS):
        return "why are you pissed."
    elif any(word in text_lower for word in CALM_WORDS):
        return "I see. Thanks for sharing."
    else:
        return "Thanks for sharing your mood!"



def main():
    now = datetime.now()
    print(f"{greeting_for_hour(now.hour)}! It is {now.strftime('%I:%M %p')}.")
    name = input("What is your name? ").strip() or "friend"
    print(f"Nice to meet you, {name}.")

    print("Type 'fact' for an AI fact, tell me how you feel, or 'quit' to exit.")
    fact_index = 0
    while True:
        user_input = input("> ").strip()
        if user_input.lower() in ("quit", "exit", "bye"):
            print(f"Goodbye, {name}!")
            break
        if "fact" in user_input.lower():
            print(AI_FACTS[fact_index % len(AI_FACTS)])
            fact_index += 1
        else:
            print(respond_to_mood(user_input))


if __name__ == "__main__":
    main()  




