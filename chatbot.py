import json

def save_to_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

chat_history = []
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    bot_response = f"Echo: {user_input}"
    print(f"Bot: {bot_response}")
    chat_history.append({"user": user_input, "bot": bot_response})

save_to_json("chat_history.json", chat_history)
print("Chat history saved to chat_history.json")
