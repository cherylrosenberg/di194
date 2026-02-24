# https://colab.research.google.com/drive/1iAH8bCN_k40OTOFmoafWPbzjbkjb701A?usp=sharing

## DUNDER Methods
class Temperature:
    def __init__(self, degrees):
        self.degrees = degrees

    # This will return when you use print(temp object)
    def __str__(self):
        return f"{self.degrees}C"
    
    #Returns a string but for developers, so it can be returned to the original object
    def __repr__(self):
        return f"Temperature({self.degrees})"
    
    # returns an int
    def __int__(self):
        return int(self.degrees)
    
    # + operator
    def __add__(self, other: "Temperature | int | float"):
    
        if isinstance(other, (int, float)):
            return Temperature(self.degrees + other.degrees)
    
        return Temperature(self.degrees + other.degrees)
    
    # += 
    def __iadd__(self, other: "Temperature"):
        self.degrees += other.degrees
        return self

t = Temperature(25.5)
t2 = Temperature(32.3)

print(t)
print(repr(t))
print(int(t))

t3 = t + t2
print(t3)

t += t2
print(t)