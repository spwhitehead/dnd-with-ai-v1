import openai

# Function to prompt the user for their OpenAI API key


def get_api_key():
    openai.api_key = input("Enter your OpenAI API key: ")
    return openai.api_key

# Function to initialize the ChatGPT model


def initialize_chatgpt(api_key):
    openai.api_key = api_key
    model = "gpt-3.5-turbo"  # Choose the ChatGPT model
    return model

# Function to interact with ChatGPT and play the DND game


def play_dnd_game(model):
    print("Welcome to the Dungeons & Dragons game!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye! Thanks for playing.")
            break
        else:
            response = openai.ChatCompletion.create(
                engine=model,
                prompt=user_input + "\n",
                max_tokens=50
            )
        print("Game Master:", response.choices[0].text.strip())

# Main function


def main():
    api_key = get_api_key()
    model = initialize_chatgpt(api_key)
    play_dnd_game(model)


if __name__ == "__main__":
    main()
