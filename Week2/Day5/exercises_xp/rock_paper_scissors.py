from game import Game
# Key Python Topics:
# OOP (Classes, Methods)
# Modules (Importing)
# Random Number Generation (random.choice())
# User Input and Validation
# Conditional Logic
# Loops (while)
# Data Structures (Dictionaries)
# Game Logic

# What You Will Create:
# A Rock Paper Scissors game where the user plays against the computer, with a menu, game logic, and score tracking.

# Instructions:
# Create a directory for the game.
# Create rock-paper-scissors.py (for menu, input, and summary).
# Create game.py (for game logic).


# Part II - rock-paper-scissors.py

# Step 6: Implement get_user_menu_choice Function
# Create a function called get_user_menu_choice().
# Display the menu options (“Play a new game”, “Show scores”, “Quit”).
# Get the user’s choice.
# Validate the input (e.g., check if it’s one of the valid options).
# Return the user’s choice.

def get_user_menu_choice():
    menu_options = {
        'g': "Play a new game",
        's': "Show scores",
        'q': "Quit"
    }

    while True:
        print("\n--- Main Menu ---")
        for key, value in menu_options.items():
            print(f"({key}) {value}")
        
        user_choice = input("Select an option: ").lower().strip()

        if user_choice in menu_options:
            return user_choice
        
        print("Invalid selection. Please choose g, s, or q.")

# Step 7: Implement print_results Function
# Create a function called print_results(results).
# Take a dictionary called results as a parameter (e.g., {"win": 2, "loss": 4, "draw": 3}).
# Print the results in a user-friendly format (e.g., “Wins: 2, Losses: 4, Draws: 3”).
# Thank the user for playing.

def print_results(results):
    print("\n--- Final Game Summary ---")
    print(f"Wins:   {results.get('win', 0)}")
    print(f"Losses:     {results.get('loss', 0)}")
    print(f"Draws:      {results.get('draw', 0)}")

    print("\nThank you for playing!")


# Step 8: Implement main Function
# Create a function called main().
# Pepeatedly show the menu until the user chooses to exit.
# Call get_user_menu_choice() to get the user’s choice.
# If the user chooses to play a game:
# Create a Game object.
# Call the play() method of the Game object.
# Store the result of the game in a dictionary (e.g., results).
# If the user chooses to exit:
# Call print_results() to display the game summary.
# Exit the program.

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == 'g':
            game_instance = Game()
            outcome = game_instance.play()
            results[outcome] +=1

        elif choice == 'q' or choice == 's':
            print_results(results)
            if choice == 'q':
                break

if __name__ == "__main__":
    main()
