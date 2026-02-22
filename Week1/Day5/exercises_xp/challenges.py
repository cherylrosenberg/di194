# Exercise 1 Instructions
# Write a script that inserts an item at a defined index in a list.

list = [1,2,3,4,5]
item = 0

list.insert(3,item)
print(list)

# Exercise 2 Instructions
# Write a script that counts the number of spaces in a string.

string = ('This is a String and it would be nice to know how Many spaces there are')
spaces_count = string.count(' ')
print(spaces_count)

# Exercise 3 Instructions
# Write a script that calculates the number of upper case letters and lower case letters in a string.

count_upper = 0
count_lower = 0
for char in string:
    if char.isupper():
        count_upper += 1
for char in string:
    if char.islower():
        count_lower += 1

print(f"The number of upper case letters is: {count_upper}")
print(f"The number of lower case letters is: {count_lower}")

# Exercise 4 Instructions
# Write a function to find the sum of an array without using the built in function:

# >>>my_sum([1,5,4,2])
# >>>12

def calculate_sum(array):
    sum = 0
    for item in array:
        sum += item
    return sum

array = [14,7,21,54]
sum_array = (calculate_sum(array))
print(sum_array)

# Exercise 5 Instructions
# Write a function to find the max number in a list

# >>>find_max([0,1,3,50])
# >>>50

def find_max(list):
    max = 0
    for item in list: 
        if item >= max:
            max = item
    return max

list = [0, 33, 194, 732, 12]
max_num = (find_max(list))
print(max_num)

# Exercise 6 Instructions
# Write a function that returns factorial of a number

# >>>factorial(4)
# >>>24

def factorial(num):
    """
    Calculates the factorial of a non-negative integer    
    
    :param num: A non-negative integer
    Returns: The factoiral of num
    """ 
    # Check if the num is negative
    if num < 0:
        return 1 
    elif num == 0:
        return 1
    else:
        result = 1
        for i in range(1, num+1):
            result *= i
        return result
    
factorial = factorial(4)
print(factorial)
    
# Exercise 7
# Instructions
# Write a function that counts an element in a list (without using the count method):

list = ['el 1', 'el 2', 'el 3', 'el 4', 'el 5']

def count_element(list):
    count = 0
    for i in list:
        count += 1
    return count

count_el = count_element(list)
print(count_el)

# Exercise 8
# Instructions
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

# >>>norm([1,2,2])
# >>>3

list = [1,3,5,3]

def l2_norm(list):
    sum_squares = 0
    for i in list:
        sum_squares += i**2

    root = sum_squares**0.5
    return root

result = l2_norm(list)
print(result)

# Exercise 9
# Instructions
# Write a function to find if an array is monotonic (sorted either ascending or descending)

# >>>is_mono([7,6,5,5,2,0])
# >>>True

# >>>is_mono([2,3,3,3])
# >>>True

# >>>is_mono([1,2,0,4])
# >>>False

# array = [1,2,3,4]
# def is_mono(array):
#     for array[i] in array:
#         if i >= i+1:
#             return True
#         else: 
#             for i in list:
#                 if i <= i-1:
#                     return True
#                 else: 
#                     return False

array = [1,2,3,4]
def is_mono(array):
    increasing = True
    decreasing = True

    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            increasing = False
        if array[i] < array[i+1]:
            decreasing = False
    
    return increasing or decreasing


print(is_mono([7,6,5,5,2,0])) # True
print(is_mono([2,3,3,3]))     # True
print(is_mono([1,2,0,4]))     # False