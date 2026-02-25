import string
import re

# What You’ll learn
# OOP (Classes, Class Methods, Inheritance)
# Modules (File Handling, String Manipulation, Data Structures)
# Text Analysis Techniques

# Key Python Topics:
# OOP (Classes, Class Methods, Inheritance)
# File handling (open())
# String manipulation (split(), join(), translate(), regular expressions)
# Dictionaries
# Sets
# Lists
# string module
# re module (regular expressions)

# Instructions:
# Create a Text class to analyze text data, either from a string or a file. Then, create a TextModification class to perform text cleaning.

# Part I: Analyzing a Simple String
# Step 1: Create the Text Class
# Create a class called Text.
# The __init__ method should take a string as an argument and store it in an attribute (e.g: self.text).

class Text:
    def __init__(self, text_input):
        self.text = text_input

# Step 2: Implement word_frequency Method
# Create a method called word_frequency(word).
# Split the text attribute into a list of words.
# Count the occurrences of the given word in the list.
# Return the count.
# If the word is not found, return None or a meaningful message.

    def word_frequency(self, word):
        words_list = self.text.split()

        count = words_list.count(word)
        return count if count > 0 else f"The word '{word}' was not found"

# Step 3: Implement most_common_word Method
# Create a method called most_common_word().
# Split the text into a list of words.
# Use a dictionary to store word frequencies.
# Find the word with the highest frequency.
# Return the most common word.

    def most_common_word(self):
        words_list = self.text.split()
        word_frequencies = {}

        for word in words_list:
            if word not in word_frequencies:
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

        most_common = None
        highest_count = 0

        for word, count in word_frequencies.items():
            if count > highest_count:
                highest_count = count
                most_common = word
        
        return most_common
    

# Step 4: Implement unique_words Method
# Create a method called unique_words().
# Split the text into a list of words.
# Use a set to store unique words.
# Return the unique words as a list.

    def unique_words(self):
        words_list = self.text.split()
        unique_words_set = set(words_list)
        return list(unique_words_set)





# Part II: Analyzing Text from a File

# Step 5: Implement from_file Class Method
# Create a class method called from_file(file_path).
# Open the file at file_path in read mode.
# Read the file content.
# Create and return a Text instance with the file content as the text.
     
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r") as file:
            content = file.read()
        
        return cls(content)
    

# Bonus: Text Modification
# Step 6: Create the TextModification Class
# Create a class called TextModification that inherits from Text.
class TextModification(Text):
    def __init__(self, text_input):
        super().__init__(text_input)


# Step 7: Implement remove_punctuation Method
# Create a method called remove_punctuation().
# Use the string module to get a string of punctuation characters.
# Use a string method or regular expressions to remove punctuation from the text attribute.
# Return the modified text.

    def remove_punctuation(self):
        punctuation = string.punctuation

        clean_text = "".join(char for char in self.text if char not in punctuation)

        self.text = clean_text
        return self.text
    
# Step 8: Implement remove_stop_words Method
# Create a method called remove_stop_words().
# Search online for a list of English stop words (common words like “a”, “the”, “is”).
# Split the text into a list of words.
# Filter out stop words from the list.
# Join the remaining words back into a string.
# Return the modified text.

    def remove_stop_words(self):
        stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

        words_list = self.text.split()
        
        filtered_words = [word for word in words_list if word.lower() not in stop_words]

        self.text = " ".join(filtered_words)


# Step 9: Implement remove_special_characters Method
# Create a method called remove_special_characters().
# Use regular expressions to remove special characters from the text attribute.
# Return the modified text.

    def remove_special_characters(self):

        pattern = r'[^a-zA-Z0-9\s]'
        clean_text = re.sub(pattern, '', self.text)

        self.text = clean_text
        return self.text


raw_data = "The quick brown fox, it jumps over the lazy dog!!! @Special #Characters and the dog is happy."
processor = TextModification(raw_data)

print(f"Original: {processor.text}\n")

processor.remove_special_characters()
processor.remove_punctuation()
processor.remove_stop_words()
print(f"Cleaned:  {processor.text}\n")

print("--- Analysis ---")
print(f"Most Common Word: {processor.most_common_word()}")
print(f"Unique Words:     {len(processor.unique_words())}")
print(f"Frequency of 'dog': {processor.word_frequency('dog')}")