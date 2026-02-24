import datetime as dt

# Exercise 6: Birthday and minutes
# Key Python Topics:
# datetime module
# datetime.datetime.strptime() (parsing dates)
# Time difference calculations
# .total_seconds() method

# Instructions:
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

def minutes_lived():
    birthdate_string = input("What is your birthday? (YYYY-MM-DD): ")

    try: 
        birthdate_object = dt.datetime.strptime(birthdate_string, "%Y-%m-%d")

        time_passed = dt.datetime.now() - birthdate_object

        minutes_passed = int(time_passed.total_seconds() / 60)

        print(f"You have lived for {minutes_passed:,} minutes in your life!")

    except ValueError:
        print("Formatting error! Please use YYYY-MM-DD")


minutes_lived()

