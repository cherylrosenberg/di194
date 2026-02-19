# Exercise 1: Converting Lists into Dictionaries
# Key Python Topics:
# Creating dictionaries
# Zip function or dictionary comprehension

# Instructions
# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.

# Lists:
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Expected Output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

numbers_dict = dict(zip(keys,values))

# # Exercise 2: Cinemax #2
# # Key Python Topics:
# # Looping through dictionaries
# # Conditionals
# # Calculations

# # Instructions
# # Write a program that calculates the total cost of movie tickets for a family based on their ages.

# # Family members’ ages are stored in a dictionary.
# # The ticket pricing rules are as follows:
# # Under 3 years old: Free
# # 3 to 12 years old: $10
# # Over 12 years old: $15

# Family Data:
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0
# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.

for name,age in family.items():
    #Ticket pricing logic
    if age < 3: 
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else: 
        price = 15

    #Add to total and print individual price
    total_cost += price
    print(f"{name.capitalize()}'s ticket price: ${price}")

#Print the total cost at the end
print(f"Total cost for the family: ${total_cost}")


# Bonus:
# Allow the user to input family members’ names and ages, then calculate the total ticket cost.

family = {}

while True: 
    name = input("Enter name (type done when finished): ").strip().lower()
    if name == 'done':
        break
    
    try: 
        age = int(input(f"Enter age for {name.capitalize()}:"))
        family[name] = age # Adds the pair to the dictionary
    except ValueError: 
        print("Please enter a valid number for the age.")

print(family)

# Exercise 3: Zara
# Key Python Topics:
# Creating dictionaries
# Accessing and modifying dictionary elements
# Dictionary methods like .pop() and .update()

# Instructions
# Create and manipulate a dictionary that contains information about the Zara brand.

# Brand Information:
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green

# Create a dictionary called brand with the provided data.
zara_brand = {
    'name': 'zara',
    'creation_date':1975,
    'creator_name':'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women','children','home'], 
    'international_competitors':['Gap','H&M','Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ['pink','green']
    }
}

# Modify and access the dictionary as follows:

# Change the value of number_stores to 2.
zara_brand['number_stores'] = 2

# Print a sentence describing Zara’s clients using the type_of_clothes key.
categories = ", ".join(zara_brand['type_of_clothes'])
print(f"Zara sells to clients that are looking for items in the following categories: {categories}")

# Add a new key country_creation with the value Spain.
zara_brand['country_creation'] ='Spain'

# Check if international_competitors exists and, if so, add “Desigual” to the list.
if 'international_competitors' in zara_brand:
    zara_brand['international_competitors'].append('Desigual')

print(zara_brand['international_competitors'])

# Delete the creation_date key.
del zara_brand['creation_date']
print(zara_brand)

# Print the last item in international_competitors.
print(zara_brand['international_competitors'][-1])

# Print the major colors in the US.
print(zara_brand['major_color']['US'])

# Print the number of keys in the dictionary.
num_keys = len(zara_brand)
print(num_keys)

# Print all keys of the dictionary.
# for key in zara_brand:
#     print(key)

print(zara_brand.keys())

# Bonus:
# Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.

more_on_zara = {
    'creation_date':1975,
    'number_stores': 7000
}

zara_brand.update(more_on_zara)
print(zara_brand['number_stores'])

# Exercise 4: Disney Characters
# Key Python Topics:
# Looping with indexes
# Dictionary creation
# Sorting

# Instructions
# You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:

# Character List:
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# Expected Results:

# 1. Create a dictionary that maps characters to their indices:
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
char_indices = {user:index for index, user in enumerate(users)}
print(char_indices)

# 2. Create a dictionary that maps indices to characters:
# {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
char_indices = {index:user for index, user in enumerate(users)}
print(char_indices)

# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

sorted_users = sorted(users)
sorted_char_indices = {user:index for index, user in enumerate(sorted_users)}
print(sorted_char_indices)