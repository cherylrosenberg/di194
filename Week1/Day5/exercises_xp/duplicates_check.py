# Exercise: Check for duplicates in a list

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
temp = []
duplicates = []

# for letter in some_list:
#     if letter not in temp:
#         temp.append(letter)
#     else:
#         duplicates.append(letter) 
# print(f"Duplicated letters: {duplicates}")
# print(f"Temp letters are: {temp}")

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)