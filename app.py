import json


with open("Pricing.json") as f:
    data = json.load(f)

def mock_lead_capture(name, email, platform):
    print(f"\nLEAD CAPTURED: {name}, {email}, {platform}\n")

def detect_intent(text):
    text = text.lower()

    if any(w in text for w in ["buy", "want", "interested", "subscribe"]):
        return "lead"

    if any(w in text for w in ["price", "plan", "cost"]):
        return "query"

    if any(w in text for w in ["hi", "hello", "hey"]):
        return "greeting"

    return "other"

def get_response(text):
    text = text.lower()

    if "price" in text or "plan" in text:
        return (f"\nBasic: {data['pricing']['basic']['price']} → {data['pricing']['basic']['features']}\n"
                f"Pro: {data['pricing']['pro']['price']} → {data['pricing']['pro']['features']}")

    if "refund" in text:
        return data["policies"]["refund"]

    if "support" in text:
        return data["policies"]["support"]

    return " Ask me about pricing or plans!"

def run():
    print(" AUTOSTREAM BOT (type 'exit' to quit)\n")

    lead = {"name": None, "email": None, "platform": None}
    collecting = False

    while True:
        user = input("You: ")

        if user.lower() == "exit":
            break

        if collecting:
            if lead["name"] is None:
                lead["name"] = user
                print("Bot: Enter your email:")
                continue

            elif lead["email"] is None:
                lead["email"] = user
                print("Bot: Your platform (YouTube/Instagram):")
                continue

            elif lead["platform"] is None:
                lead["platform"] = user

                mock_lead_capture(**lead)
                print("Bot: Done! We'll contact you.")

                # Reset
                lead = {"name": None, "email": None, "platform": None}
                collecting = False
                continue

        intent = detect_intent(user)

        if intent == "greeting":
            print("Bot: Hello! How can I help you?")

        elif intent == "query":
            print("Bot:", get_response(user))

        elif intent == "lead":
            collecting = True
            print("Bot: Great! What's your name?")

        else:
            print("Bot:", get_response(user))


if __name__ == "__main__":
    run()