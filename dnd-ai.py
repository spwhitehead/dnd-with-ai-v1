from openai import OpenAI

client = OpenAI(api_key=input("Enter your OpenAI API key: "))

# Function to interact with ChatGPT and play the DND game


def play_dnd_game():
    initial_game_prompt = """
    You are a knight in the kingdom of Larion. 
    You are on a quest to find the magical Sword of Larion, which is said to be hidden in the Cave of Wonders. 
    You have been traveling for days and finally arrive at the cave. 
    
    When you wish to quit, type 'quit'."
    """
    print("Welcome to the Dungeons & Dragons game!")
    print()
    print(initial_game_prompt)
    print()
    game_history = [
        {"role": "system", "content": f"""
         You are a DND Game Master. You are narrating the game for the user. The user is talking to you.
         The user received this prompt at the beginning of the game {initial_game_prompt}. Keep your responses in the context of the game.
         Include unexpected occurances, such as getting attacked by animals or beasts, or other people. Introduce new characters periodically.
         Subtilly push the user to keep going. At the end of each response, ask the user what they would like to do next.
         Keep the responses interesting, engaging, and as consise as possible."""},
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
