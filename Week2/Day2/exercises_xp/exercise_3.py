import random
from exercise_2 import Dog

# Exercise 3: Dogs Domesticated
# Goal: Create a PetDog class that inherits from Dog and adds training and tricks.
# Key Python Topics:
# Inheritance
# super() function
# *args
# Random module

# Instructions:
# Step 1: Import the Dog Class
# In a new Python file, import the Dog class from the previous exercise.

# Step 2: Create the PetDog Class
# Create a class called PetDog that inherits from the Dog class.
# Add a trained attribute to the __init__ method, with a default value of False.
# trained means that the dog is trained to do some tricks.

class PetDog(Dog): 
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained 

    # Implement a train() method that prints the output of bark() and sets trained to True.
    def train(self):
        print(self.bark())
        self.trained = True

    # Implement a play(*args) method that prints “<dog_names> all play together”.
    # *args on this method is a list of dog instances.
    def play(self, *args):
        dog_names = []
        dog_names.append(self.name)

        for dog in args:
            dog_names.append(dog.name)
        
        names_string = ", ".join(dog_names)

        print(f"{names_string} all play together")

    # Implement a do_a_trick() method that prints a random trick if trained is True.
    # Use this list for the ramdom tricks:
    # tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
    # Choose a random index from it each time the method is called.
    def do_a_trick(self):
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        if self.trained:
           print(f"{self.name} {tricks[random.randrange(len(tricks))]}") 


# Step 3: Test PetDog Methods
# Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() methods.

petDog1 = PetDog("Rufus", 3, 22.0, trained=True)
petDog2 = PetDog("Spot", 9, 13.0, trained=True)
petDog3 = PetDog("Golda", 1, 12.0, trained=False)

petDog3.train()
# print(petDog3.trained)

petDog3.play(petDog1, petDog2)

petDog1.do_a_trick()