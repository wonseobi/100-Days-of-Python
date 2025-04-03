# DAY 5 PROJECT
# Program that generates a secure password, asking the user how many letters, symbols, numbers, they want to include in the password.

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassword Generator!")
number_letters = int(input("How many letters would you like in your password?\n"))
number_symbols = int(input(f"How many symbols would you like?\n"))
number_numbers = int(input(f"How many numbers would you like?\n"))

# EASY Level, generate the password in order letter, symbols, numbers

easy_password = ""

    # Store randomly chosen letters, symbols, and numbers in an empty str variable
for char in range(1, number_letters + 1):
    easy_password += random.choice(letters)

for char in range(1, number_symbols + 1):
    easy_password += random.choice(symbols)

for char in range(1, number_numbers + 1):
    easy_password += random.choice(numbers)

    # Print out the str password variable
print(f"This is your final password: {easy_password}")
    
# HARD level, generate the password in RANDOM order, letter, symbols, numbers

hard_password = []
sorted_hard_password = ""

    # Store letters, symbols, numbers in a new variable as a list.
for char in range(1, number_letters + 1):
    hard_password.append(random.choice(letters)) 

for char in range(1, number_symbols + 1):
    hard_password.append(random.choice(symbols)) 

for char in range(1, number_numbers + 1):
    hard_password.append(random.choice(numbers))

    # Resorting order from created list, then print out resorted password.
for char in hard_password:
    sorted_hard_password += random.choice(hard_password)

print(f"This is your final enhanced password: {sorted_hard_password}")