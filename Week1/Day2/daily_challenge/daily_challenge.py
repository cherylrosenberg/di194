# Challenge 1: Multiples of a Number

# Key Python Topics:
# input() function
# Loops (for or while)
# Lists and appending items
# Basic arithmetic (multiplication)

# 1. Ask the user for two inputs:

# A number (integer).
# A length (integer).

number = int(input("Please enter a number: "))
length = int(input("Please enter a length: "))

#  2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.

number_list = []
for i in range(number, (number * length) +1, number):
    number_list.append(i) 
print(number_list)

# Challenge 2: Remove Consecutive Duplicate Letters
# Key Python Topics:
# input() function
# Strings and string manipulation
# Loops (for or while)
# Conditional statements (if)

# Instructions:
# 1. Ask the user for a string.
# 2. Write a program that processes the string to remove consecutive duplicate letters.

# The new string should only contain unique consecutive letters.
# For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
# 3. The program should print the modified string.

string_input = input("Please enter a string: ")
string_non_duplicate = ""
last_char = ""

for char in string_input:
    if char != last_char:
        string_non_duplicate += char
    last_char = char

print(string_non_duplicate)
