# Exercise 4: Current Date
# Goal: Create a function that displays the current date.

# Key Python Topics:
# datetime module

# Instructions:
# Use the datetime module to create a function that displays the current date.
# Step 1: Import the datetime module

import datetime as dt

def current_date():
    # Step 2: Get the current date
    current_date = dt.datetime.now().date()
    # Step 3: Display the date
    print(current_date)

current_date()