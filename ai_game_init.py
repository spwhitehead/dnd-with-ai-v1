def initial_game_prompt():
    return """
    You are a knight in the kingdom of Larion. 
    You are on a quest to find the magical Sword of Larion, which is said to be hidden in the Cave of Wonders. 
    You have been traveling for days and finally arrive at the cave. 
    When you wish to quit, type 'quit'."
    """


def user_name():
    return input("Enter your name: ")


def user_time_period():
    return input("Enter the time period you would like to play in (e.g. Futuristic): ")


def user_location():
    return input("Enter the location you would like to play in (e.g. Space): ")
