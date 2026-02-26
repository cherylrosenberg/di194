import random

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

# Part I - game.py
# Step 1: Create the Game Class

class Game:
    def __init__(self):
        self.valid_moves = ['rock', 'paper', 'scissors']

# Step 2: Implement get_user_item Method
# Create a method called get_user_item(self).
# Ask the user to select an item (rock/paper/scissors).

    def get_user_item(self):
        while True:
            user_input = input(f"Select an item ({', '.join(self.valid_moves)}): ").lower().strip()

            if user_input in self.valid_moves:
                return user_input
 
            print("Invalid choice. Please try again.")

# Step 3: Implement get_computer_item Method
# Create a method called get_computer_item(self).
# Randomly select an item (rock/paper/scissors).
# Return the computer’s item.

    def get_computer_item(self):
        computer_item = random.choice(self.valid_moves)
        return computer_item


# Step 4: Implement get_game_result Method
# Create a method called get_game_result(self, user_item, computer_item).
# Take user_item and computer_item as parameters.
# Determine the result of the game based on the rules of Rock Paper Scissors.
# Return “win”, “draw”, or “loss”.

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        
        user_wins = (
            (user_item == 'rock' and computer_item == 'scissors') or
            (user_item == 'scissors' and computer_item == 'paper') or 
            (user_item == 'paper' and computer_item == 'rock')
        )

        if user_wins:
            return "win"
        else:
            return "loss"

# Step 5: Implement play Method
# Create a method called play(self).
# Call get_user_item() to get the user’s choice.
# Call get_computer_item() to get the computer’s choice.
# Call get_game_result() to determine the result.
# Print the outcome of the game (user’s choice, computer’s choice, result).
# Return the result (“win”, “draw”, or “loss”) as a string.

    def play(self):
        user_choice = self.get_user_item()
        computer_choice = self.get_computer_item()
        result = self.get_game_result(user_choice, computer_choice)
        print(f"User Choice: {user_choice} | Computer Choice: {computer_choice} | {result}")
        return result
