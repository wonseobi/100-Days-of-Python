# From a list variable, print a randomly element or item inside the list of names, determining who will pay the bill.

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option One
selected_friend = (random.choice(friends))

print("OPTION ONE")
print(f"The randomly chosen person is {selected_friend}")

# Option Two
random_choice = random.randint(0, 4)
chosen_one = ""

print("OPTION TWO")
if random_choice == 0:
    chosen_one = "Alice"
    print(f"The randomly chosen person is {chosen_one}")
elif random_choice == 1:
    chosen_one = "Bob"
    print(f"The randomly chosen person is {chosen_one}")
elif random_choice == 2:
    chosen_one = "Charlie"
    print(f"The randomly chosen person is {chosen_one}")
elif random_choice == 3:
    chosen_one = "David"
    print(f"The randomly chosen person is {chosen_one}")
elif random_choice == 4:
    chosen_one = "Emanuel"
    print(f"The randomly chosen person is {chosen_one}")