# 38. Using the LOOP with Python
fruits = ["Apple", "Peach", "Banana"]

for fruit in fruits:
    print(fruit)
    print(f"I love eating {fruit}" + ""
    "pie")
print(fruits)

# 39. Highest Score
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 250]

total_exam_score = sum(student_scores)
print(total_exam_score)

sum = 0

# For Loop: Iterate over each element in a list
for score in student_scores:
    sum += score


print(sum)

# Print the largest number in a list
print(max(student_scores))

# TASK Find the largest number in a list using the For Loop, Lists, and Conditionals.

# My code
biggest_score = 0
current_score = 0

for current_score in student_scores:
    if biggest_score > current_score:
        print(f"The biggest score is {biggest_score}")
    else:
        current_score = biggest_score 


# Angela Yu Code
max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

# Range 

for number in range(1, 10, 3):
    print(number)


# TASK The Gauss Challenge Work out the total sum of numbers between 1 and 100 

gauss_counter = 0

for number in range(1, 101):
    gauss_counter += number
    print(f"This is the Gauss Counter: {gauss_counter}")