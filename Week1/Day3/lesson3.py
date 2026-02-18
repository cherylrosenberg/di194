# rick_dict = {
#     'first_name':'Rick',
#     'last_name':' Sanchez'
# }

# print(rick_dict['first_name'])

# print(f"The last name of {rick_dict['first_name']} is:{rick_dict['last_name']}")

# # The two four loops are equivelant

# for item in rick_dict:
#     print(item, '->', rick_dict[item])

# for key,value in rick_dict.items():
#     print(key, '->', value)


# ##Nested Dictionaries
# my_dog = {
#     'name':'Rufus',
#     'age':4,
#     'good_dog':True,
#     'best_friend': {
#         'name': 'Felix',
#         'age':'4.5'
#     },
# }

# ### Exercise 1: Access the value of key history

# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# print(sample_dict['class']['student']['marks']['history'])

# ### Change a value 
# sample_dict['class']['student']['marks']['history'] = 100
# print(sample_dict['class']['student']['marks']['history'])

# ### Add a new value
# sample_dict['class']['student']['marks']['music'] = 93
# print(sample_dict) 

# print('age') in my_dog #True
# print('4') in my_dog #False because this only works on the keys, not the values 

# print(my_dog.keys())
# print(my_dog.values())
# print(my_dog.items())

# ### Exercise 2: Delete set of keys from Python Dictionary

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# keys_to_remove = ["name", "salary"]

# #del sample_dict['name'],sample_dict['salary']
# #print(sample_dict)

# for item in keys_to_remove:
#     del sample_dict[item]
# print(sample_dict)

# ###############
# # Advanced Dictorionaries and Loops

# my_books = {
#   "title": "Harry Potter",
#   "author": "JK Rowling",
# }

# for x, y in my_books.items():
#     print("the" + x + "is" + y)

# # >> the title is Harry Potter
# # the author is JK Rowling

# for item in my_books.keys():
#     print(item, my_books[item])

# for item in my_books.values():
#     print(item)

# ## Enumerate gives the index of the item in the list as well as the item itself.
# my_list = ['xiao', 'jingwen', 'cheryl']
# print(list(enumerate(my_list)))

# for index,item in enumerate(my_list):
#     print(f'index {index} is {item}')

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# # duplicates = []
# # for value in some_list:
# #     if some_list.count(value) > 1:
# #         if value not in duplicates:
# #             duplicates.append(value)
# # print(duplicates)

# # duplicates = [value for value in some_list if some_list.count(value) > 1]
# duplicates = list(set([value for value in some_list if some_list.count(value) > 1]))
# print(duplicates)

# user = {
#     'basket': [1,2,3],
#     'greet':'hello',
#     'age':20
# }

# print(user.items())

# ### Exercise Dictionary Methods 

# # 1 Create a user profile for your new game
# # This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
# user = {
#     'age':0, 
#     'username':' ', 
#     'weapons':None, 
#     'is_active':False,
#       'clan':None
# }

# # 2 iterate and print all the keys in the above user.
# print(user.keys())

# # 3 Add a new weapon to your user
# user['weapons'] = 'sword'

# # 4 Add a new key to include 'is_banned'. Set it to false
# user.update({'is_banned': False})

# # 5 Ban the user by setting the previous key to True
# user['is_banned'] = True

# # 6 create a new user2 my copying the previous user and update the age value and username value.
# user2 = user.copy()
# user2.update({'age':50, 'username':'user2'})
# print(user)
# print(user2)

# my_dict = {num:num*2 for num in [1,2,3]}