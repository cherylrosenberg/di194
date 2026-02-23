# https://colab.research.google.com/drive/1B2x_hwTcg70cUAF2IXu25FOyvvXyIdHB?usp=sharing#scrollTo=cell-0017

class Dog:
    def __init__(self, name: str, age: int, weight: float, breed: str):
        self.name = name
        self.age = age
        self.weight = weight
        self.breed = breed
    
    def run_speed(self):
        return (self.weight / self.age) * 10
    
    def fight(self, other_dog: "Dog"):
        # if self.run_speed() > other_dog.run_speed():
        #     print(f"{self.name} wins!")
        # elif other_dog.run_speed() > self.run_speed():
        #     print(f"{other_dog.name} wins!")
        # else:
        #     print("It's a draw")
        # doing it the below way means you only call the method twice, instead of how I did it above, you call the method 4 times 
        my_speed = self.run_speed()
        their_speed = other_dog.run_speed()
        if my_speed > their_speed:
            print(f"{self.name} wins!")
        elif their_speed > my_speed:
            print(f"{other_dog.name} wins!")
        else: 
            print("It's a draw")


class Dogs: 
    def __init__(self):
        self.pack = []

    def add_dog(self, dog: "Dog"):
        if isinstance(dog, Dog):
            self.pack.append(dog)
    
    def fight_all(self):
        for i in range(len(self.pack)):
            for j in range(i+1, len(self.pack)):
                self.pack[i].fight(self.pack[j])

dog1 = Dog("Rex", 4, 20.00, "German Shepherd")
dog2 = Dog("Bella", 2, 12.0, "Poodle")
dog3 = Dog("Max", 6, 30.0, "Saint Bernard")

pack = Dogs()
pack.add_dog(dog1)
pack.add_dog(dog2)
pack.add_dog(dog3)

pack.fight_all()
     