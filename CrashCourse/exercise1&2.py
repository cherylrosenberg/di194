# Exercise 1
#1
first = "Hello World"
#2
# This is a comment.
#3
print("I AM A COMPUTER!")
#4
if 1 < 2 and 4 > 2:
    print("Math is fun!")
#5
nope = None
#6
True and False
#7
len("What's my length?")
#8
"I am shouting".upper()
#9
string = "1000"
num = int(string)
#10
num = 4
word = "real"
combined = f"{num}{word}"
#11 (answer: "coolcoolcool")
3 * "cool"
#12 (answer: error)
1 / 0 
#13
# [] is a list
#14
name = input("What is your name?")
#15
number = int(input("Enter a number:"))
if number < 0:
    print("That number is less than 0!")
elif number > 0:
    print("That number is greater than 0!")
else: 
    print("You picked 0!")
#16
fruit = "apple"
fruit.index("l")
#17
if "y" in "xylophone":
    print("y is in xylophone")
#18
my_string = "i am all lowercase"
if my_string.islower():
    print("my_string is all lowercase")


# Exercise 2 

human_years = int(input("Enter human years:"))
dog_years = 0
cat_years = 0

if human_years == 1:
    cat_years = 15
    dog_years = 15
elif human_years == 2:
    cat_years = 15 + 9
    dog_years = 15 + 9
else:
    cat_years = 24 + (human_years - 2)*4
    dog_years = 24 + (human_years - 2)*5

print(human_years,cat_years,dog_years)