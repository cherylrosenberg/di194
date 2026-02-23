# Exercise 1: Cats
# Key Python Topics:
# Classes and objects
# Object instantiation
# Attributes
# Functions

# Instructions:
# Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create Cat Objects
# Use the Cat class to create three cat objects with different names and ages.

cat1 = Cat('Whiskers', 3)
cat2 = Cat("Fluffy", 7)
cat3 = Cat("Spot", 1)

# Step 2: Create a Function to Find the Oldest Cat
# Create a function that takes the three cat objects as input.
# Inside the function, compare the ages of the cats to find the oldest one.
# Return the oldest cat object.

def find_oldest_cat(cat1, cat2, cat3):
    if cat1.age >= cat2.age and cat1.age >= cat3.age:
        return cat1
    elif cat2.age >= cat1.age and cat2.age >= cat3.age:
        return cat2
    else:
        return cat3
    
# Step 3: Print the Oldest Cat’s Details
# Call the function to get the oldest cat.
# Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
# Replace <cat_name> and <cat_age> with the oldest cat’s name and age.
    
oldest = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old")

# Exercise 2 : Dogs
# Goal: Create a Dog class, instantiate objects, call methods, and compare dog sizes.

# Key Python Topics:
# Classes and objects
# Object instantiation
# Methods
# Attributes
# Conditional statements (if)


# Instructions:
# Create a Dog class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes.

# Step 1: Create the Dog Class
# Create a class called Dog.
# In the __init__ method, take name and height as parameters and create corresponding attributes.
# Create a bark() method that prints “<dog_name> goes woof!”.
# Create a jump() method that prints “<dog_name> jumps <x> cm high!”, where x is height * 2.

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm high!")

# Step 2: Create Dog Objects
# Create davids_dog and sarahs_dog objects with their respective names and heights.

davids_dog = Dog("Rufus", 50)
sarahs_dog = Dog("Coco", 35)

# Step 3: Print Dog Details and Call Methods
# Print the name and height of each dog.

print(f"{davids_dog.name} : {davids_dog.height}")
print(f"{sarahs_dog.name} : {sarahs_dog.height}")

# Call the bark() and jump() methods for each dog.

davids_dog.bark()
sarahs_dog.bark()

davids_dog.jump()
sarahs_dog.jump()

# Step 4: Compare Dog Sizes

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is tallest")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is tallest!")
else:
    print("{davids_dog.name} and {sarahs_dog.name} are the same height!")


# Exercise 3 : Who’s the song producer?
# Goal: Create a Song class to represent song lyrics and print them.
# Key Python Topics:
# Classes and objects
# Object instantiation
# Methods
# Lists

# Instructions:
# Create a Song class with a method to print song lyrics line by line.

# Step 1: Create the Song Class
# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.

# Example:
# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()
# Output: There’s a lady who’s sureall that glitters is goldand she’s buying a stairway to heaven

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for lyric in self.lyrics:
            print(f"{lyric}")

you_want_it_darker = Song([
    "If you are the dealer, I'm out of the game",
    "If you are the healer, it means I'm broken and lame",
    "If thine is the glory, then mine must be the shame",
    "You want it darker",
    "We kill the flame"
])

you_want_it_darker.sing_me_a_song()

# Exercise 4 : Afternoon at the Zoo
# Goal: Create a Zoo class to manage animals. The class should allow adding animals, displaying them, selling them, and organizing them into alphabetical groups.
# Key Python Topics:
# Classes and objects
# Object instantiation
# Methods
# Lists
# Dictionaries (for grouping)
# String manipulation

# Instructions
# Step 1: Define the Zoo Class
# 1. Create a class called Zoo.
# 2. Implement the __init__() method:
# It takes a string parameter zoo_name, representing the name of the zoo.
# Initialize an empty list called animals to keep track of animal names.

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    # 3. Add a method add_animal(new_animal):
    # This method adds a new animal to the animals list.
    # Do not add the animal if it is already in the list.
    def add_animal(self, *new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    # 4. Add a method get_animals():
    # This method prints all animals currently in the zoo.
    def get_animals(self):
        print(f"{self.animals}")

    # 5. Add a method sell_animal(animal_sold):
    # This method checks if a specified animal exists on the animals list and if so, remove from it.
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    # 6. Add a method sort_animals():
    # This method sorts the animals alphabetically.
    # It also groups them by the first letter of their name.
    # The result should be a dictionary where:
    # Each key is a letter.
    # Each value is a list of animals that start with that letter.
    # Example output:
    # {
    #    'B': ['Baboon', 'Bear'],
    #    'C': ['Cat', 'Cougar'],
    #    'G': ['Giraffe'],
    #    'L': ['Lion'],
    #    'Z': ['Zebra']
    # }

    def sort_animals(self):
        grouped_animals = {}

        for animal in sorted(self.animals):
            letter = animal[0]

            if letter not in grouped_animals:
                grouped_animals[letter] = []
            
            grouped_animals[letter].append(animal)
        
        return grouped_animals


    # 7. Add a method get_groups():
    # This method prints the grouped animals as created by sort_animals().
    # Example output:
    # B: ['Baboon', 'Bear']
    # C: ['Cat', 'Cougar']
    # G: ['Giraffe']

    def get_groups(self):
        groups = self.sort_animals()
        for letter, animal in groups.items():
            print(f"{letter}: {animal}")

# Step 3: Call the Zoo Methods
# Use the methods of your Zoo object to test adding, selling, displaying, sorting, and grouping animals.
central_park_zoo = Zoo('Central Park Zoo')
central_park_zoo.add_animal("Giraffe","Donkey", "Bear", "Baboon")
central_park_zoo.get_animals()
print()
central_park_zoo.sell_animal("Lion")
central_park_zoo.get_animals()
print()
central_park_zoo.add_animal("Lion")
central_park_zoo.add_animal("Liger")
central_park_zoo.add_animal("Monkey")
central_park_zoo.add_animal("Pengiun")
central_park_zoo.get_animals()
print()
central_park_zoo.sort_animals()
central_park_zoo.get_groups()






