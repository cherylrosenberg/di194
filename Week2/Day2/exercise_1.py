# Exercise 1: Pets
class Pet:
    is_lazy = False

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def make_sound(self):
      print("...")

class Cat(Pet):
    is_lazy = True

    def __init__(self, name: str, age: int, indoor: bool):
        super().__init__(name, age)
        self.indoor = indoor

    def make_sound(self):
       print(f"{self.name} says: Meow!")

class Dog(Pet):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed
    
    def make_sound(self):
        print(f"{self.name} says: Woof!")
    
    def fetch(self, item: str):
        print(f"{self.name} fetches the {item}")

# Tests
cat = Cat("Whiskers", 4, indoor=True)
dog = Dog("Buddy", 2, "Beagle")

cat.description()
cat.make_sound()
dog.make_sound()
dog.fetch("stick")

## Polymorphism = many forms
# Python will know which make sound to call based on the class type even though they're all in the same pets list

pets = [Cat('Whiskers', 4, True), Dog('Rex', 2, 'Lab'), Pet('Nemo', 1)]
for pet in pets:
  pet.make_sound()

# Can use isinstance to loop through the list and only call the method on the items that hare in the Pets class 
class Circle:
  ...

pets = [Cat('Whiskers', 4, True), Dog('Rex', 2, 'Lab'), Pet('Nemo', 1), Circle()]
for pet in pets:
  if isinstance(pet, Pet):
    pet.make_sound()



