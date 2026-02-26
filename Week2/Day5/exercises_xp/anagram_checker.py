# What You’ll learn
# OOP (Classes, Methods)
# Python Files I/O (Reading Files)
# String Manipulation
# Algorithm Design (Anagram Checking)

# Key Python Topics:
# OOP (Classes, Methods)
# File I/O (Reading Files)
# String Manipulation (strip(), split(), isalpha())
# Algorithm Design (Anagram Checking)
# User Input and Validation
# Conditional Logic
# Loops

#  What you will create
# An anagram checker program that takes user input, validates it, and finds anagrams from a word list.

# Instructions:
# Download the provided text file (word list).
# Create anagram_checker.py with the AnagramChecker class.
# Create anagrams.py for the user interface.


# anagram_checker.py:
# Step 1: Create the AnagramChecker Class
# Create a class called AnagramChecker.
# Implement the __init__ method:
# Load the word list file into a variable (e.g., a set or list).
# Store the words in lowercase for case-insensitive comparison.

class AnagramChecker:
    def __init__(self, filename):
        try: 
            with open(filename, 'r') as f:
                self.words = {line.strip().lower() for line in f}
        except FileNotFoundError:
            print(f"Error: File '{filename}' doesn't exist")
            self.words = set()

# Step 2: Implement is_valid_word Method
# Create a method called is_valid_word(word).
# Check if the given word exists in the loaded word list (case-insensitive).
# Return True if valid, False otherwise.

    def is_valid_word(self, word):
        # if word.lower() in self.words:
        #     return True
        # else:
        #     return False
        return word.lower().strip() in self.words

# Step 3: Implement is_anagram Method
# Create a method called is_anagram(word1, word2).
# Check if the sorted characters of word1 are equal to the sorted characters of word2.
# Return True if anagrams, False otherwise.

    def is_anagram(self, word1, word2):
        # sorting and comparison would be different if they have different capital letters. Ensure all lower before sort.
        word1, word2 = word1.lower(), word2.lower()
        # check if they are the exact same word (check before sorting). If they are, it's not considered an anagram of itself so set to False
        if word1 == word2:
            return False
        
        return sorted(word1) == sorted(word2)

# Step 4: Implement get_anagrams Method
# Create a method called get_anagrams(word).
# Create an empty list to store anagrams.
# Iterate through the word list.
# For each word in the list, check if it’s an anagram of the given word using is_anagram.
# If it’s an anagram and not the same word, add it to the anagrams list.
# Return the list of anagrams.

    def get_anagrams(self, word):
        anagrams_list = []

        for w in self.words:
            if self.is_anagram(w, word):
                anagrams_list.append(w)
        return anagrams_list
