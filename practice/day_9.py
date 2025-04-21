programming_dictionary = {
    "Bug": "An error occured",
    "Function": "Callable piece of code",
}

# Accessing an item from a dictionary 
print(programming_dictionary["Bug"])

# "Append" a new item in a dictionary
programming_dictionary["Loop"] = "Action of calling something over and over"
print(programming_dictionary)

empty_dictionary = {}

# Wipe an existing dictionary

# programming_dcitionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
print(programming_dictionary["Bug"])

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Coding Exercise 9 Grading Program

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Create an empty dictionary to collect the new values.
student_grades = {}

# Loop through each key in the student_scores dictionary.
for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'

# Nesting 
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Travel List in Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart,", "Berlin"],
}

print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log_two = {
    "South Korea": {
        "num_times_visited": 3,
        "cities_visited": ["Busan", "Seoul", "Jeju"]
    },
    "USA": {
        "num_times_visited": 2,
        "cities_visited": ["Miami", "Los Angeles"]
    }
}

print(travel_log_two["USA"["cities_visited"][0]])