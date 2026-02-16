# Exercise 1: Favorite Numbers
# Key Python Topics:

# Sets
# Adding/removing items in a set
# Set concatenation (using union)


# Instructions:

# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = {6, 16, 25, 616, 92}
my_fav_numbers.add(33)
my_fav_numbers.add(42)
my_fav_numbers.remove(42)

friend_fav_numbers = {3, 6, 9, 12, 15}

our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(our_fav_numbers)

# Exercise 2: Tuple

# Key Python Topics:
# Tuples (immutability)

# Instructions:
# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.

integer_tuple = (1, 2, 3, 4, 5)
new_integer_tuple = integer_tuple + (6,7,8,9,10)
print(new_integer_tuple)

# Exercise 3: List Manipulation
# Key Python Topics:

# Lists
# List methods: append, remove, insert, count, clear

# Instructions:

# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)

# Exercise 4: Floats
# Key Python Topics:
# Lists
# Floats and integers
# Range generation

# Instructions:

# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

numbers = []
i = 1.5

while i <= 5:
    numbers.append(i)
    i += 0.5
print(numbers)

# Exercise 5: For Loop
# Key Python Topics:
# Loops (for)
# Range and indexing

# Instructions:

# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

for i in range(1, 21):
    print(i)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Exercise 6: While Loop
# Key Python Topics:
# Loops (while)
# Conditionals

# Instructions:

# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop

name = input("What is your name? ")
while True: 
    if name.isdigit() or len(name) < 3:
        name = input("Please enter a valid name: ")
    else: 
        print("thank you")
        break

# Exercise 7: Favorite Fruits
# Key Python Topics:
# Input/output
# Strings and lists
# Conditionals

# Instructions:
# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

favorite_fruits = input("What are your favorite fruits? ").split()
fruit = input("Give me a name of a fruit: ")
if fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# Exercise 8: Pizza Toppings
# Key Python Topics:

# Loops
# Lists
# String formatting


# Instructions:

# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

toppings = []
while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total_cost = 10 + len(toppings)*2.5
print(f"Toppings: {', '.join(toppings)}")
print(f"Total cost: ${total_cost:.2f}")

# Exercise 9: Cinemax Tickets
# Key Python Topics:

# Conditionals
# Lists
# Loops


# Instructions:

# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

total_cost = 0
while True:
    age = input("What is your age? ")
    if int(age) < 3:
        total_cost += 0
    elif int(age) <= 12: 
        total_cost += 10
    else: 
        total_cost += 15
    more = input("Is there another person in the family? (yes/no) ")
    if more.lower() != "yes":
        break

print(f"The total ticket cost is: ${total_cost}")

# Bonus:

# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.

attendees = []
while True:
    age = input("What is your age? ")
    if int(age) < 16 or int(age) > 21:
        print("Sorry, you are not allowed to watch the movie.")
    else: 
        input_name = input("What is your name? ")
        attendees.append(input_name)
    more = input("Is there another person? (yes/no) ")
    if more.lower() != "yes":
        break
print("Attendees: " + ", ".join(attendees))