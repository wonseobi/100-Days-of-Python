#  Create a program that randomly generates the result of a coin toss, outputting heads or tails using the random Python module.

import random

random_number = random.randint(1,2)
result = ""

if random_number == 1:
    result = "Heads"
    print(f"You flipped {result}")
elif random_number == 2:
    result = "Tails"
    print(f"You flipped {result}")