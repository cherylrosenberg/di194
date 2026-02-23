# https://colab.research.google.com/drive/1B2x_hwTcg70cUAF2IXu25FOyvvXyIdHB?usp=sharing

# The class Car will have the methods that are on Car and on Vehicle. When you make a new class ElectricCar, and pass in the details of car, it'll have the attributes of the Car class and the Vehicle class

class Vehicle:
  movable = True # class attribute

  def __init__(self, make, speed):
    self.make = make
    self.speed = speed

  def describe(self):
    print(f"{self.make} - top speed: {self.speed} km/h")

  def move(self):
    print(f"The {self.make} is moving.")

class Car(Vehicle):
  def __init__(self, make, speed, doors):
    super().__init__(make, speed)
    self.doors = doors

  def honk(self):
    print(f"The {self.make} goes: Beep beep!")

class ElectricCar(Car):
  def __init__(self, make, speed, doors, battery_kw):
    super().__init__(make, speed, doors)
    self.battery_kw = battery_kw

  def charge(self):
    print(f"Charging {self.make} - battery: {self.battery_kw} kW")


tesla = ElectricCar("Tesla Model 3", 250, 4, 75)
tesla.describe()
tesla.honk()
tesla.charge()
print(tesla.doors)

# Useful built-ins for checking inheritance
print(isinstance(tesla,ElectricCar))
print(isinstance(tesla,Car))
print(isinstance(tesla,Vehicle))
print(issubclass(Car, Vehicle))
print(issubclass(ElectricCar, Vehicle))
print(issubclass(ElectricCar, Car))

# *args IN INHERITED CLASSES — How to pass variable arguments up
# ══════════════════════════════════════════════════════════════════

class Animal:
    def __init__(self, name, age, *traits):
        self.name   = name
        self.age    = age
        self.traits = list(traits)   # e.g. ['fast', 'fierce']

class Dog(Animal):
    def __init__(self, name, age, breed, *traits):
        super().__init__(name, age, *traits)  # unpack *traits for Animal
        self.breed = breed

steve = Animal('Monkey', 3, 'fast', 'strong', 'smart')
print(steve.traits)
rex = Dog("Rex", 4, "Labrador", "loyal", "energetic")
print(rex.traits)   # ['loyal', 'energetic']
print(rex.breed)    # 'Labrador'

# https://colab.research.google.com/drive/1B2x_hwTcg70cUAF2IXu25FOyvvXyIdHB?usp=sharing#scrollTo=cell-0017

# IS-A means inheritance. For example, a dog IS A animal, so it inherits its attributes
# HAS-A means composition. For example, a student HAS A classroom. It doesn't inherit the attributes of a classroom
# composition is one class storing references to instances of another class. A Family stores a list of Person objects. A Playlist has a list of Student objects. The objects in the list are fully functional objects with their own attributes and methods. 
# This is how most OOP works in practice. Classes talk to each other

class Player: 
    def __init__(self, name, goals, assists):
        self.name = name
        self.goals = goals
        self.assists = assists

    def stats(self):
        print(f"{self.name}: {self.goals}g / {self.assists}a")

class Team:
    def __init__(self, name):
        self.name = name
        self.players = [] # will hold Player objects

    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)

    def total_goals(self):
        return sum(p.goals for p in self.players) # calls each Player's .goals attribute
    
    def top_scorer(self):
        return max(self.players, key=lambda p: p.goals)
        # lambda p: p.goals # given a player p, give me p.goals()

    ## an alternative version without the lambda
    # def top_scorer(self): 
    #     def get_score(p: Player):
    #         return p.goals
    #     return max(self.players, key=get_score)

    def squad_report(self):
        for player in self.players:
            player.stats()
        print(f"Total goals: {self.total_goals()}")
        best = self.top_scorer()
        print(f"Top Scorer: {best.name} ({best.goals} goals)")

barca = Team("Barcelona")
barca.add_player(Player("Messi", 30, 15))
barca.add_player(Player("Xavi", 12, 20))
barca.add_player(Player("Iniesta", 10, 18))

barca.squad_report()