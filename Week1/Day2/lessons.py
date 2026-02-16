# Given this list:

# find the value 20 in the list, and if it is present, replace it with 200. 
# Only update the first occurrence of a value
# use the index method 

list1 = [5, 10, 15, 20, 25, 50, 20]

index_20 = list1.index(20)
list1[index_20] = 200

# Bonus:

# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.

attendees = []
while True:
    age = input("What is your age? ")
    if int(age) < 16 or int(age) > 21:
        print("Sorry, you are not allowed to watch the movie.")
    else: 
        input_name = input("What is your name? ")
        attendees.append(input_name)
    more = input("Is there another person? (yes/no) ")
    if more.lower() != "yes":
        break
print("Attendees: " + ", ".join(attendees))
