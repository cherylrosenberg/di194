# Mini-Project #2 - Hangman

# What you will learn
# Conditionals
# Loops
# Functions
# Modules


# What you will create
# Use python to create a Hangman game.

# Instructions
# The computer choose a random word and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.

import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 

## Setup the hidden word
hidden_word = []
for char in word:
    if char == ' ':
        hidden_word.append(' ')
    else: 
        hidden_word.append('*')

## Set up tracking variables 
guessed_letters = []
wrong_guesses = 0
max_guesses = 6
body_parts = ["head", "body", "left arm", "right arm", "left leg", "right leg"]

print("".join(hidden_word))

def letter_guess(word, hidden_word, wrong_guesses, guessed_letters):
    guess = input("Guess a letter: ").lower()

    # check if they already guessed the letter
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'")
        return wrong_guesses, guessed_letters
    
    guessed_letters.append(guess)
    
# loop through the word and compare letters in the word to the guess
    if guess in word:
        for i, char in enumerate(word): 
            if char == guess: 
                hidden_word[i] = guess
        print("Good guess!")
    else: 
        wrong_guesses += 1
        print("Guess again!")
    
    return wrong_guesses, guessed_letters

while '*' in hidden_word and wrong_guesses < max_guesses:
    wrong_guesses, guessed_letters = letter_guess(word, hidden_word, wrong_guesses, guessed_letters)

    print("".join(hidden_word))
    print(f"Wrong count: {wrong_guesses}")   
    print(f"Letters used: {guessed_letters}")

    if wrong_guesses > 0:
        print(f"Gallows status: {body_parts[0:wrong_guesses]}")

if '*' not in hidden_word:
    print(f"You won! The word was '{word}'")
else:
    print(f"Game over! You got hung. The word was '{word}'")
