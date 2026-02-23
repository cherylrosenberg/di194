# Exercise 2: Dogs
# Goal: Create a Dog class with methods for barking, running speed, and fighting.
# Key Python Topics:
# Classes and objects
# Methods
# Attributes

# Instructions:
# Step 1: Create the Dog Class
# Create a class called Dog with name, age, and weight attributes.
# Implement a bark() method that returns “<dog_name> is barking”.
# Implement a run_speed() method that returns weight / age * 10.
# Implement a fight(other_dog) method that returns a string indicating which dog won the fight, based on run_speed * weight.

class Dog:
    def __init__(self, name: str, age: int, weight: float):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return round(self.weight / self.age * 10, 2)
    
    def fight(self, other_dog):
        my_stats = self.run_speed() * self.weight
        their_stats = other_dog.run_speed() * other_dog.weight

        if my_stats > their_stats:
            print(f"{self.name} won the fight!")
        elif their_stats > my_stats:
            print(f"{other_dog.name} won the fight!")
        else: 
            print(f"It was a tie between {self.name} and {other_dog.name}")               

# Step 2: Create Dog Instances
# Create three instances of the Dog class with different names, ages, and weights.

dog1 = Dog("Ben", 4, 20.2)
dog2 = Dog("Golda", 3, 23.0)
dog3 = Dog("Coco", 7, 19.4)

# Step 3: Test Dog Methods
# Call the bark(), run_speed(), and fight() methods on the dog instances to test their functionality.

print(dog1.bark())
print(dog2.run_speed())
print(dog3.run_speed())
dog2.fight(dog3)