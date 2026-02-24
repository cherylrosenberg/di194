import math

# Daily Challenge - Circle
# What You’ll learn
# Object-Oriented Programming (OOP)
# Dunder (Magic) Methods in Python

# Instructions
# The goal is to create a class that represents a simple circle.

# A Circle can be defined by either specifying the radius or the diameter - use a decorator for it.
# The user can query the circle for either its radius or diameter.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        """Calculate diameter based on radius"""
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, value):
        """Set radius based on a new diameter value"""
        self.radius = value / 2

# Abilities of a Circle Instance
# Your Circle class should be able to:

# ✅ Compute the circle’s area.

    @property
    def area(self):
        """Computes the area: A = π * r²"""
        return math.pi * (self.radius ** 2)
    
# ✅ Print the attributes of the circle — use a dunder method (__str__ or __repr__).

    def __str__(self):
        return f"Circle with Radius: {self.radius: .2f} | Diameter: {self.diameter: .2f} | Area: {self.area: .2f}"
    
    def __repr__(self):
        return f"Circle({self.radius})"

# ✅ Add two circles together and return a new circle with the new radius — use a dunder method (__add__).

    def __add__(self,other):
        if not isinstance(other, Circle):
            raise TypeError (f"Only add a Cirlce object to a Circle")
        
        new_circle_radius = self.radius + other.radius
        return Circle(new_circle_radius)

# ✅ Compare two circles to see which is bigger — use a dunder method (__gt__).

    def __gt__(self,other):
        if not isinstance(other, Circle):
            raise TypeError (f"You can only compare two circles to each other")
        
        return self.radius > other.radius
    
# ✅ Compare two circles to check if they are equal — use a dunder method (__eq__).

    def __eq__(self,other):
        if not isinstance(other, Circle):
            raise TypeError (f"Only two Circle objects can equal each other")
        
        return self.radius == other.radius

    def __lt__(self,other):
        if not isinstance(other, Circle):
            raise TypeError (f"You can only compare two circles to each other")
        
        return self.radius < other.radius
    
# # ✅ Store multiple circles in a list and sort them — implement __lt__ or other comparison methods.
circles = [Circle(10), Circle(2), Circle(5), Circle(1)]

print("Original Order:")
print(circles)

circles.sort()

print("\nSorted order (Smallest to Largest):")
for c in circles:
    print(c)
    

## Test it 
c = Circle(5)
c2 = Circle(10)
c3 = c + c2
print(f"Radius: {c.radius}")
print(f"Area: {c.area:.4f}")
print(c)

print(c3)
print(type(c3))


# Bonus Challenge (Optional)
# If you want an extra challenge:
# Install the Turtle module (pip install PythonTurtle)
# Draw the sorted circles visually on the screen!

# 💡 Tip:
# Test your implementation by creating several circles and printing comparisons, additions, and sorted results.