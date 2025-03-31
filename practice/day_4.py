# Import modules
import random
import day_4_my_module

#     Generate a random integer within a range
random_integer = random.randint(1, 10)

print(random_integer)

#     Generate a random float within a range

random_float = random.random() * 10
print(random_float)

random_float_2 =random.uniform(1, 10)
print(random_float_2)

# Print a variable from a module!
print(day_4_my_module.my_favorite_number)