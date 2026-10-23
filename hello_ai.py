# Nolan
# Date: 2026-10-20


from datetime import datetime


AI_FACTS = [
    "The term 'artificial intelligence' was coined at the 1956 Dartmouth workshop.",
    "Deep Blue, an IBM computer, beat world chess champion Garry Kasparov in 1997.",
    "AlphaGo defeated Go champion Lee Sedol in 2016.",
    "A simple reflex agent chooses actions based only on the current percept.",
    "Alan Turing proposed the Turing Test in 1950 to ask whether machines can think.",
    "ELIZA, built in 1966, was one of the first chatbots and used simple pattern-matching rules.",
]


POSITIVE_WORDS = ["happy", "great", "good", "excited", "awesome"]
NEGATIVE_WORDS = ["sad", "tired", "stressed", "bad", "angry"]
CALM_WORDS = ["fine", "okay", "ok", "meh"]




def greeting_for_hour(hour):
    """Rule: pick a greeting based on the time of day."""
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    return "Good evening"




def respond_to_mood(text):
    """Rule: check the input for mood keywords."""
    text = text.lower()
    if any(word in text for word in POSITIVE_WORDS):
        return "Glad to hear it! Keep that energy going."
    if any(word in text for word in NEGATIVE_WORDS):
        return "Sorry to hear that. Take a break, you've got this."
    if any(word in text for word in CALM_WORDS):
        return "Steady is good. Let's learn something today."
    return "Thanks for sharing."




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


