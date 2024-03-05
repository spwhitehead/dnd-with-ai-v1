import dnd_ai
from openai import OpenAI

# get the api key from the openai-api-key.txt file
with open("openai-api-key.txt", "r") as f:
    api_key = f.read().strip()

client = OpenAI(api_key=api_key)


class GamePreferences:
    def __init__(self):
        self.name = self.user_input("Enter your name: ")
        self.time_period = self.user_input(
            "Enter the time period you would like to play in (e.g., Futuristic, Mid-evil, etc.): ")
        self.location = self.user_input(
            "Enter the location you would like to play in (e.g., Space, Ancient Rome): ")

    @staticmethod
    def user_input(prompt):
        print()
        return input(prompt)

    def __str__(self):
        return f"""
        Welcome to this Dungeons & Dragons campaign, {self.name}!
        Based on your preferences, this campaign will take place in a {self.time_period} time period, in {self.location}.
        Let's get started!

        Campaign Loading...
        """


class DnDGame:
    def __init__(self, preferences):
        self.preferences = preferences
        self.initial_game_prompt = ""
        self.game_history = []

    def generate_initial_game_prompt(self):
        instruction_message = {
            "role": "system",
            "content": f"Generate a Dungeons & Dragons campaign introduction for a player named {self.preferences.name}, set in a '{self.preferences.time_period}' time period, in '{self.preferences.location}'. Include a quest for the player to embark on."
        }

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo", messages=instruction_message)
            self.initial_game_prompt = response.choices[0].message["content"].strip(
            )
        except Exception as e:
            print(f"An error occured: {str(e)}")
            self.initial_game_prompt = "An unexpected adventure awaits in a world beyond imagination. What will you find?"

        self.game_history.append(
            {"role": "system", "content": self.initial_game_prompt})

    def start_game(self):
        print(str(self.preferences))
        print(self.initial_game_prompt)
        self.game_loop()

    def game_loop(self):
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'quit':
                print("Goodbye! Thanks for playing.")
                break
            else:
                self.game_history.append(
                    {"role": "user", "content": user_input})
                try:
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo", messages=self.game_history)

                    game_response = response.choices[0].message.content.strip()
                    print()
                    print("Game Master:", game_response)
                    print()
                    self.game_history.append(
                        {"role": "assistant", "content": game_response})
                except Exception as e:
                    print(str(e))


def main():
    preferences = GamePreferences()
    game = DnDGame(preferences)
    game.start_game()


if __name__ == "__main__":
    main()
