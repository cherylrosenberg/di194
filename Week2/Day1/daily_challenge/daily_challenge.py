# Daily challenge: Old MacDonald’s Farm

# Key Python Topics:

# Classes and Objects
# Dictionaries
# String Formatting
# Methods
# List manipulation (sorted())
# Conditional logic (if)
# String concatenation


# Step 1: Create the Farm Class
# Create a class called Farm.
# This class will represent a farm and its animals.

# Step 2: Implement the __init__ Method

# The Farm class should have an __init__ method.
# It should take one parameter: farm_name.
# Inside __init__, create two attributes: name to store the farm’s name and animals to store the animals (initialize as an empty dictionary).

class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

# Step 3: Implement the add_animal Method
# Create a method called add_animal.
# It should take two parameters: animal_type and count (with a default value of 1). Count is the quantity of the animal that will be added to the animal dictionary.
# The dictionary will look like this:
# {'cow': 1, 'pig':3, 'horse': 2}
# If the animal_type already exists in the animals dictionary, increment its count by count.
# If it doesn’t exist, add it to the dictionary as the key and with the given count as value.

    def add_animal(self, animal_type, count=1):
        if animal_type not in self.animals:
            self.animals[animal_type] = count
        else:
            self.animals[animal_type] += count

# Step 4: Implement the get_info Method

# Create a method called get_info.
# It should return a string that displays the farm’s name, the animals and their counts, and the “E-I-E-I-0!” phrase.
# Format the output to match the provided example.
# Use string formatting to align the animal names and counts into columns.

    def get_info(self):
        output = f"{self.name}\n\n"

        for animal_type, count in self.animals.items():
            output += f"{animal_type:<10} : {count}\n"
            
        output += f"\nE-I-E-I-O!"
        return output
    
# Bonus: Expand The Farm
# Step 6: Implement the get_animal_types Method
# Add a method called get_animal_types to the Farm class.
# This method should return a sorted list of all animal types (keys from the animals dictionary).
# Use the sorted() function to sort the list.
    
    def get_animal_types(self):
        return sorted(self.animals)
    
# Step 7: Implement the get_short_info Method
# Add a method called get_short_info to the Farm class.
# This method should return a string like “McDonald’s farm has cows, goats and sheeps.”.
# Call the get_animal_types method to get the list of animals.
# Construct the string, adding an “s” to the animal name if its count is greater than 1.
# Use string formatting to create the output.
    
    def get_short_info(self):
        animal_list = self.get_animal_types()
        plural_animals = []

        for animal in animal_list:
            count = self.animals[animal]

            if count > 1:
                plural_animals.append(f"{animal}s")
            else:
                plural_animals.append(f"a {animal}")

        if len(plural_animals) > 1:
            all_but_last = ", ".join(plural_animals[:-1])
            last_one = plural_animals[-1]

            if len(plural_animals) > 2:
                animal_string = f"{all_but_last}, and {last_one}"
            else:
                animal_string = f"{all_but_last} and {last_one}"
        
        else:
            animal_string = plural_animals[0] if plural_animals else ""

        
        return f"{self.name} has {animal_string}"
            
# Step 5: Test Your Code
# Create a Farm object and call the add_animal and get_info methods.
# Verify that the output matches the provided example.

mcdonald = Farm("McDonald's Farm")
mcdonald.add_animal('cow', 5)
mcdonald.add_animal('sheep')
mcdonald.add_animal('sheep')
mcdonald.add_animal('goat', 1)
print(mcdonald.get_info())
animal_types = mcdonald.get_animal_types()
print(animal_types)
short_info = mcdonald.get_short_info()
print(short_info)

# # Step 8: upgrade the add_animal Method
# # use **kwargs for passing multiple animals. The keys will be the animal name and the value will be the quantity.
# # Then you can call the method this way: macdonald.add_animal('cow'= 5, 'sheep' = 2, 'goat' = 12)

# #comment out the rest of the page to use the below code 
# class Farm:
#     def __init__(self, farm_name):
#         self.name = farm_name
#         self.animals = {}

#     def add_animal(self, **kwargs):
#         # loop throuh each keyword argument passed
#         for name, count in kwargs.items():
#             # Get the current count (defualting to 0) and add the new amount
#             self.animals[name] = self.animals.get(name, 0) + count

# mcdonald = Farm("McDonald's Farm")
# mcdonald.add_animal(cow=5, sheep=2, goat=1)
# print(mcdonald.animals)