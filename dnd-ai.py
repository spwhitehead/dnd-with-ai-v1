from openai import OpenAI

client = OpenAI(api_key=input("Enter your OpenAI API key: "))

# Function to interact with ChatGPT and play the DND game


def play_dnd_game():
    initial_game_prompt = "You are a knight in the kingdom of Larion. You are on a quest to find the magical Sword of Larion, which is said to be hidden in the Cave of Wonders. You have been traveling for days and finally arrive at the cave. When you wish to quit, type 'quit'."
    print("Welcome to the Dungeons & Dragons game!")
    print()
    print(initial_game_prompt)
    print()
    game_history = [
        {"role": "system", "content": "You are a DND Game Master. You are playing a game with a user. The user is a knight in the kingdom of Larion. They are on a quest to find the magical Sword of Larion, which is said to be hidden in the Cave of Wonders. They have been traveling for days and finally arrive at the cave. The user is talking to you. Keep your responses in the context of the game. Include unexpected occurances, such as getting attacked by animals or beasts, or other people. Introduce new characters periodically. Subtilly push the user to keep going. Keep the responses interesting, engaging, and as consise as possible."},
        {"role": "user", "content": initial_game_prompt}
    ]
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye! Thanks for playing.")
            break
        else:
            game_history.append({"role": "user", "content": user_input})
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo", messages=game_history)

                game_response = response.choices[0].message.content.strip()
                print("Game Master:", game_response)
                game_history.append(
                    {"role": "assistant", "content": game_response})
            except Exception as e:
                print(str(e))

# Main function


def main():
    play_dnd_game()


if __name__ == "__main__":
    main()
