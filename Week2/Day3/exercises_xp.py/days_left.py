# Exercise 5: Amount of time left until January 1st
# Goal: Create a function that displays the amount of time left until January 1st.
# Key Python Topics:
# datetime module
# Time difference calculations

# Instructions:
# Use the datetime module to calculate and display the time left until January 1st.
# more info about this module HERE

# Step 1: Import the datetime module

import datetime as dt

# Step 2: Get the current date and time

# current_date = dt.date.today()
# current_time = dt.datetime.now().time()
current_date_time = dt.datetime.now()
# print(current_date_time)

# Step 3: Create a datetime object for January 1st of the next year

next_jan_first = dt.datetime(dt.datetime.now().year + 1 , 1, 1)
# print(next_jan_first)

# Step 4: Calculate the time difference

time_difference = next_jan_first - current_date_time

# Step 5: Display the time difference

print(time_difference)

