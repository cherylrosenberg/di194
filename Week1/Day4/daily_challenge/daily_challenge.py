# Daily Challenge: Coffee Shop Menu Manager
# You were hired to help a small coffee shop manage their product menu using Python.
# Write a program that:
# 1. Stores the coffee shop menu in memory
# 2. Lets the user:
# Create a new item
# Read (view) all items
# Update an item’s price
# Delete an item
# Exit
# Your program must be organized with functions.
# Do not write all the logic in one giant while loop.
# You should split behavior into reusable functions.

# 1. Data structure
# We will represent the menu using a dictionary called menu.
# The key is the drink name (string)
# The value is the price (float)
# Example starting data (you MUST start with this so tests are consistent):
menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

# 2. Required functions
# You must implement the following functions.
# a) show_menu(menu_dict)
# Input: the dictionary
# Output: prints all items in the format drink - price₪
# If the menu is empty, print: "The menu is empty."
# Example:
# Current menu:
# espresso - 7.0₪
# latte - 12.0₪
# cappuccino - 10.0₪
# This function only prints. It does not return anything.

def show_menu(menu_dict):
    if not menu_dict:
        print("The menu is empty")
    else:
        print("Current menu:")
        for drink, price in menu_dict.items():
            print(f"{drink} - {price}₪")

# b) add_item(menu_dict)
# Ask the user for:
# drink name
# price
# Add it to the dictionary.
# If the drink already exists, print "Item already exists!" and do not change the price.
# Example interaction:

def add_items(menu_dict):
    drink_name = input("What drink should we add to the menu? ").lower()

    if drink_name in menu_dict:
        print("Item already exists")
    else:
        drink_price = float(input("How much should it cost? "))

        if drink_price < 0:
            print("Invalid price.")
        else: 
            menu_dict[drink_name] = drink_price
            print(f'"{drink_name}" added')

# Enter new drink name: mocha
# Enter price: 14
# "mocha" added!
# This function mutates the dictionary. It does not return anything.

# c) update_price(menu_dict)
# Ask the user which drink they want to update.
# If it exists:
# ask for the new price
# update it
# print: "Price updated!"
# If it doesn’t exist:
# print: "Item not found."

def update_price(menu_dict):
    drink_name = input("Which drink should we update? ").lower()

    if drink_name in menu_dict:
        drink_price = float(input("What's the updated price? "))
        menu_dict[drink_name] = drink_price
        print("Price updated")
    else:
        print("Item not found.")

# d) delete_item(menu_dict)
# Ask the user which drink to remove.
# If it exists:
# delete it from the dict
# print: "Item deleted."
# Otherwise:
# print: "Item not found."

def delete_items(menu_dict):
    drink_name = input("Which drink should we remove? ").lower()

    if drink_name in menu_dict:
        del menu_dict[drink_name]
        print("Item deleted.")
    else:
        print("Item not found.")

# e) show_options()
# Prints the main menu of actions for the user:
# What would you like to do?
# 1. Show menu
# 2. Add item
# 3. Update price
# 4. Delete item
# 5. Exit
# Only prints. Doesn’t return anything.

def show_options():
    print("""
What would you like to do?  
1. Show menu
2. Add item
3. Update price
4. Delete item
5. Exit
6. Search menu
""")
    
# f) run_coffee_shop()
# This is the main controller of the program.
# Behavior:
# Keep running in a loop.
# Show options.
# Ask the user to choose (1-5).
# Depending on the choice, call the correct function.

# Rules:
# Invalid choice → print "Invalid choice, try again."
# Choice 5 stops the loop and prints "Goodbye!"

def run_coffee_shop():
    while True: 
        show_options()
        user_action = input("Enter a choice between 1-6: ")

        if user_action not in ['1','2','3','4','5','6']:
            print("Invalid choice, try again.")
        elif user_action == '1': 
            show_menu(menu)
        elif user_action == '2':
            add_items(menu)
        elif user_action == '3':
            update_price(menu)
        elif user_action == '4':
            delete_items(menu)
        elif user_action == '5':
            print("Goodbye!")
            break
        elif user_action == '6':
            search_item(menu)

# 5. Extra challenges (only if they finish early)
# Ask fast students to add one or more:
# 1. Validation:
# Don’t allow negative prices. If the user enters -5, print "Invalid price." and don’t change anything.

# 2. Search function:
# Add a function search_item(menu_dict) that asks for a drink name and:
# prints the price if found
# else prints "Not in the menu."
# Then add it as option 6 in the menu.

def search_item(menu_dict):
    drink_name = input("What drink are you considering? ")

    if drink_name in menu:
        print(f"The {drink_name} costs {menu_dict[drink_name]}₪")
    else:
        print(f"{drink_name} not in the menu")

search_item(menu)

# 3. Discount day:
# Add a function apply_discount(menu_dict, percent) that reduces every price by a percentage.
# Example: apply_discount(menu, 10) makes 10% off happy hour.

def apply_discount(menu_dict, percent):
    for drink in menu_dict:
        discount_price = menu_dict[drink]*(1-(percent/100))
        menu_dict[drink] = round(discount_price,2)
    
    print(f"Discount of {percent}% applied to all items!")

# run_coffee_shop() 
# apply_discount(menu,10) 
# print(menu)

