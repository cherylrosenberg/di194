# ## Using a dictionary to make an if else statement easier to read

# user_name = input("What is your name? ")

# greetings = {
#     'alex':'hola',
#     'aaron':'shalom',
#     'leeroy':'bonjour',
#     'cheryl':'hello'
# }

# print(greetings[user_name])

# #### Functions 

# def say_hello(username, location):
#     """A function that says hello to everyone"""
#     print(f"Hello, {username.capitalize()}! You are from {location.capitalize()}")

# def logout(username):
#     print(f"User {username} logged out!")

# user = input("What's the username? ")
# location = input("Where are you from? ")

# # say_hello will now take the variable user and use it in the function wherever the input variable is referenced.
# # in the def it uses username as the variable name

# say_hello(location =location, username = user)
# # logout(user)


# # A function can see outside of itself.
# # So if a variable is defined outside of a function, it can be called in the function. Not the other way around.

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title() #.title is a string method. It capitalizes the first letter of each word in a string

# print(get_formatted_name('jimi', 'hendrix'))

# #musician = get_formatted_name('jimi', 'hendrix') 
# #print(musician)

# #How is the return statement different than print? 

# def add_three(num):
#     return num + 3

# def square(num):
#     return num ** 2

# def divide_by_2(num):
#     return num / 2

# step1 = 10

# step2 = add_three(step1) #13
# step3 = square(step2) #169
# step4 = divide_by_2(step3) #84.5

# print(step4)

# result = divide_by_2(square(add_three(step1)))
# print(result)

# def get_coords(location):
#     print(f"I know where {location} is.")
#     return(33.1234, 100.745)

# lat,long = get_coords("Ramat Gan")

# print(lat)

# Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. 
# And also it must return both addition and subtraction in a single return call

# def calculation(var1,var2):
#     return(f"Adding the two variables results in: {var1+var2}. Subtracting the two variables results in {var2-var1}.")

# result = calculation(3,5)
# print(result)

# def calculation(a,b):
#     add = a + b
#     sub = a - b
#     return [add, sub]

# res = calculation(40,10)
# print(res)

###Args (return tuples) and kwargs (return dictionary)

# def say_hello(*args):
#     print("The greetings are: ", args)

# say_hello("ahoy", "hello", "hi")

# def say_hello(**kwargs):
#     print("The greetings are: ", kwargs)

# print(say_hello(greeting1='ahoy',greeting2='hello', greeting3='hi'))

def make_sandwich(type,*args,**kwargs):
    print(f"Making a {type} sandwich")
    if args:
        for arg in args:
            print(f"adding {arg}")
    if kwargs:
        print("additional parameters are: ", kwargs)

make_sandwich("cheese", "lettuce", "tomato", breadtype = "brown pita")



