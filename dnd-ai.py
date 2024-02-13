import openai


def get_api_key():
    api_key = input("Enter your OpenAI API key: ")
    return api_key

# Function to initialize the OpenAI client with the provided API key


def initialize_openai_client(api_key):
    openai.api_key = api_key

# Function to interact with ChatGPT and play the DND game


def play_dnd_game():
    initial_game_prompt = "You are a knight in the kingdom of Larion. You are on a quest to find the magical Sword of Larion, which is said to be hidden in the Cave of Wonders. You have been traveling for days and finally arrive at the cave."
    print("Welcome to the Dungeons & Dragons game!")
    print()
    print(initial_game_prompt)  # Initial game prompt
    print()
    game_history = [{"role": "system", "content": initial_game_prompt}]
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye! Thanks for playing.")
            break
        else:
            game_history.append({"role": "user", "content": user_input})
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",  # Specify the model you want to use
                    messages=game_history
                )
                game_response = response.choices[0].message["content"].strip()
                print("Game Master:", game_response)
                game_history.append(
                    {"role": "assistant", "content": game_response})
            except Exception as e:
                print(str(e))

# Main function


def main():
    api_key = get_api_key()
    initialize_openai_client(api_key)
    play_dnd_game()


if __name__ == "__main__":
    main()
