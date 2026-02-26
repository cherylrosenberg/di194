# https://colab.research.google.com/drive/1KKWfO1qrJ3NkNap92giXrvChImJ5C7MM?usp=sharing#scrollTo=cell-0020

## Error Syntax

try:
    # write your code that might fail
    result = int(input("Enter a number: "))
except ValueError:
    #Python will go here if a ValueError type occurs. You should always catch specific error types - ValueError, FileNotFound etc. You shouldn't just write except with nothing. 
    #Code that runs if it fails
    print("That's not a number!")

try:
    with open("file.txt", "r") as f:
        f.read()
except FileNotFoundError:
    print("File not found! Using default data.")
    content = "default"

