import dnd_ai


class GamePreferences:
    def __init__(self):
        self.name = self.user_input("Enter your name: ")
        self.time_period = self.user_input(
            "Enter the time period you would like to play in (e.g., Futuristic): ")
        self.location = self.user_input(
            "Enter the location you would like to play in (e.g., Space): ")

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
        prompt_instructions = f"Create a Dungeons & Dragons campaign introduction for a player named {self.preferences.name}, " \
            f"set in a {self.preferences.time_period} time period, located in {self.preferences.location}. " \
            f"Include a quest for the player to embark on."

        self.initial_game_prompt = dnd_ai.generate_dnd_game_prompt(
            prompt_instructions)

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
                # Process the user input and generate game responses here
                # Placeholder for processing user input
                print("Game Master: [Your response based on user input]")


def main():
    preferences = GamePreferences()
    game = DnDGame(preferences)
    game.start_game()


if __name__ == "__main__":
    main()
