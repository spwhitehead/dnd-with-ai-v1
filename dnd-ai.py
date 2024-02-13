from openai import OpenAI

client = OpenAI(api_key=input("Enter your OpenAI API key: "),
api_key=api_key)

# Function to prompt the user for their OpenAI API key


def get_api_key():
    return openai.api_key

# Function to initialize the ChatGPT model


def initialize_chatgpt(api_key):
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
            try:
                response = client.chat.completions.create(model=model,  # Specify the model you want to use
                messages=[
                    {"role": "system", "content": "You are a knight in the kingdom of Larion. You are on a quest to find the magical Sword of Larion, which is said to be hidden in the Cave of Wonders. You have been traveling for days and finally arrive at the cave."},
                    {"role": "user", "content": user_input},
                ])
                print("Game Master:",
                      response.choices[0].message.content.strip())
            except Exception as e:
                print(str(e))

# Main function


def main():
    api_key = get_api_key()
    model = initialize_chatgpt(api_key)
    play_dnd_game(model)


if __name__ == "__main__":
    main()
