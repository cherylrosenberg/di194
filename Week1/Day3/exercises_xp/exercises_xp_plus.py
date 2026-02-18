# You are given a dictionary containing student names as keys and lists of their grades as values. 
# Your task is to create a summary report that calculates the average grade for each student, assigns a letter grade, and determines the class average.

student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

# Calculate the average grade for each student and store the results in a new dictionary called student_averages.

student_averages = {
    key:round(sum(value)/(len(value)),2) for key, value in student_grades.items()
}

print(student_averages)

# Assign each student a letter grade (A, B, C, D, F) based on their average grade according to the following scale, and store the results in a dictionary called student_letter_grades:
# A: 90 and above
# B: 80 to 89
# C: 70 to 79
# D: 60 to 69
# F: Below 60

student_letter_grades = {}

for key,value in student_averages.items():
    if value >= 90:
        letter = 'A'
    elif 80 <= value <= 89:
        letter = 'B'
    elif 70 <= value <= 79:
        letter = 'C'
    elif 60 <= value <= 69:
        letter = 'D'
    else:
        letter = 'F'

    student_letter_grades[key] = letter

print(f"Final Grades: {student_letter_grades}")