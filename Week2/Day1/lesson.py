# https://colab.research.google.com/drive/1d4isLwVjYFxgzoBQ9dslaktdT-0Z4aRz?usp=sharing

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Fluffy", 3)
cat2 = Cat("Whiskers", 7)
cat3 = Cat("Mittens", 1)

print(f"Cat 1: {cat1.name}, age: {cat1.age}")
print(f"Cat 2: {cat2.name}, age: {cat2.age}")
print(f"Cat 3: {cat3.name}, age: {cat3.age}")

# Exercise 1: Cats

# My attempt - works
# def find_oldest_cat(cat1, cat2, cat3):
#     oldest_cat = cat1
#     if cat2.age > oldest_cat.age:
#         oldest_cat = cat2
#     elif cat3.age > oldest_cat.age:
#         oldest_cat = cat3
#     print (f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

# oldest_cat = find_oldest_cat(cat1,cat2,cat3)
# print(oldest_cat)

#Instructor version
def find_oldest_cat(cat1, cat2, cat3):
    if cat1.age >= cat2.age and cat1.age >= cat3.age:
        return cat1
    elif cat2.age >= cat1.age and cat2.age >= cat3.age:
        return cat2
    else:
        return cat3

oldest = find_oldest_cat(cat1,cat2,cat3)
print(oldest.name, oldest.age)

# Part 3: Methods - Teaching Objects to DO Things

# In procedural coding, the function doesn't know anything - you pass everything in 
# In OOP, the method is stateful. It lives in an object that already has the data. You bundle behaviour and data in the same place

class Cat: 
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

    def make_sound(self): 
        print(f"{self.name} says Meow!")

fluffy = Cat(cat_name='Fluffy', cat_age=3)
fluffy.make_sound()

class Car: 
    def __init__(self, brand: str, speed: int):
        self.brand = brand
        self.speed = speed

    def describe(self):
        print(f"This is a {self.brand} with a top speed of {self.speed} km/h")

    def race(self, other_car):
        if self.speed > other_car.speed:
            print(f"{self.brand} wins the race against {other_car.brand}")
        elif other_car.speed > self.speed:
            print(f"{other_car.brand} wins the race against {self.brand}")
        else:
            print(f"It's a tie between {self.brand} and {other_car.brand}")

ferrari = Car('Ferrari', 100)
fiat = Car('Fiat', 80)

cars = []
cars.append(ferrari)
cars.append(fiat)

for i, car in enumerate(cars):
    print(f"Car {i+1}: {car.brand}")

# get just the brands
print(f"Car 1: {ferrari.brand}")
print(f"Car 2: {fiat.brand}")

#call methods
for car in cars:
    car.describe()

ferrari.race(fiat)

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm high")


davids_dog = Dog('Coco', 35)
sarahs_dog = Dog('Nala', 55)

print(f"{davids_dog.name} is {davids_dog.height} cm tall")
print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall")
print()

davids_dog.bark()
sarahs_dog.bark()

sarahs_dog.jump()
davids_dog.jump()

print()

def compare_sizes(dog1, dog2):
    if dog1.height > dog2.height:
        print(f"{dog1.name} is taller than {dog2.name}")
    elif dog2.height > dog1.height:
        print(f"{dog2.name} is taller than {dog1.name}")
    else: 
        print(f"{dog1.name} and {dog2.name} are the same height")

compare_sizes(davids_dog, sarahs_dog)

class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs # a plain list of song title strings

    def play_all(self):
        # loop over the list of the songs
        print(f"Now playing: {self.name}")
        for song in self.songs:
            print(f" - {song}")

    def add_song(self, new_song):
        self.songs.append(new_song)
        print(f"Added {new_song} to the '{self.name}' playlist")

morning = Playlist("Morning Commute", [
    "Here Comes the Sun",
    "Good Day Sunshine",
    "Walking on Sunshine"
])

morning.play_all()
print()
morning.add_song('Mr. Blue Sky')
print()
print(f"Total songs: {len(morning.songs)}")

class Song: 
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for lyric in self.lyrics:
            print(lyric)

you_want_it_darker = Song([
    "If you are the dealer, I'm out of the game",
    "If you are the healer, it means I'm broken and lame",
    "If thine is the glory, then mine must be the shame",
    "You want it darker",
    "We kill the flame"
])

you_want_it_darker.sing_me_a_song()

# Exercise 4 - Zoo

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = [] # a default attribute
    
    def add_animal(self, new_animal):
        if new_animal not in self.animals: #de-duplication guard
            self.animals.append(new_animal)
    
    def get_animals(self):
        print(self.animals)
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        groups = { }

        for animal in sorted(self.animals):
            letter = animal[0] # takes the first character
            #'A'?'B'?
            
            if letter not in groups:
                groups[letter] = [] # 'B': []
            
            groups[letter].append(animal)
            
        return groups

    def get_groups(self):
        groups = self.sort_animals()
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")

# Create a zoo and test it 
central_park_zoo = Zoo('Central Park Zoo')
central_park_zoo.add_animal("Giraffe")
central_park_zoo.add_animal("Lion")
central_park_zoo.add_animal("Baboon")
central_park_zoo.add_animal("Giraffe") # - duplicate, should be ignored
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