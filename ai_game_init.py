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
        self.generate_initial_game_prompt

    def generate_initial_game_prompt(self):
        prompt_instructions = f"Create a Dungeons & Dragons style campaign introduction for a player named {self.preferences.name}, " \
            f"set in a {self.preferences.time_period} time period, located in {self.preferences.location}. " \
            f"Include a quest for the player to embark on."
        self.initial_game_prompt = prompt_instructions

        self.game_history = [
            {"role": "system", "content": f"""
         You are a DND Game Master. You are narrating the game for the user. The user is talking to you.
         You are to narrate and {self.initial_game_prompt}. Keep your responses in the context of the game.
         Include unexpected occurances, such as getting attacked by animals or beasts, or other people. Introduce new characters periodically.
         Subtilly push the user to keep going. At the end of each response, ask the user what they would like to do next.
         Keep the responses interesting, engaging, and as consise as possible."""},
            {"role": "user", "content": self.initial_game_prompt}
        ]

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
