# Step 1: Import AnagramChecker
from anagram_checker import AnagramChecker

# Step 2: Create a Menu Loop
# Step 3: Get User Input and Validate
# Step 4: Find and Display Anagrams
# Create an instance of AnagramChecker.
# Use is_valid_word to check if the word is valid.
# Use get_anagrams to find anagrams.
# Display the word, its validity, and the anagrams in a formatted message.

my_checker = AnagramChecker(r'Week2\Day5\exercises_xp\sowpods.txt')

while True:
    print("\n--- Anagram Finder ---")
    user_input = input("Enter a word (or type 'exit' to quit): ").strip().lower()

    if user_input == 'exit':
        print("Goodbye!")
        break

    if my_checker.is_valid_word(user_input):
        anagrams = my_checker.get_anagrams(user_input)
        print(f"'{user_input}' is a valid word.")
        print(f"Anagrams found: {','.join(anagrams) if anagrams else 'None'}")
    else:
        print(f"'{user_input}' is not in the dictionary")



