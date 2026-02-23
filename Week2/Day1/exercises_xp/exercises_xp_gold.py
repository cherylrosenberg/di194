import random
# Exercise 1 : Geometry
# Instructions
# Write a class called Circle that receives a radius as an argument (default is 1.0).
# Write two instance methods to compute perimeter and area.
# Write a method that prints the geometrical definition of a circle.

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def compute_perimeter(self):
        return (self.radius*3.14*2)
    
    def compute_area(self):
        return(3.14*(self.radius**2))
    
    def define_circle(self):
        print(f"In geometry, a circle is defined as the set of all points in a plane that are at an equal, fixed distance from a single, central point.")
    
circle = Circle(3.0)
print(circle.compute_perimeter())
print(circle.compute_area())

# Exercise 2 : Custom List Class
# Instructions
# Create a class called MyList, the class should receive a list of letters.
# Add a method that returns the reversed list.
# Add a method that returns the sorted list.
# Bonus : Create a method that generates a second list with the same length as mylist. The list should be constructed with random numbers. (use list comprehension).

class Mylist:
    def __init__(self, letters):
        self.letters = letters

    def reverse_list(self):
       reversed_list = self.letters[::-1]
       return reversed_list
    
    def sorted_list(self):
        sorted_list = sorted(self.letters)
        return sorted_list
    
    def second_list_gen(self):
        return [random.randint(1,100) for _ in self.letters]

my_list = Mylist(['a','b','x','c','d','e'])
print(my_list.reverse_list())
print(my_list.sorted_list())
print(my_list.second_list_gen())