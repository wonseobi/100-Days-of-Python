# From a list variable, print a randomly element or item inside the list of names, determining who will pay the bill.

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
selected_friend = (random.choice(friends))

print(f"The randomly chosen person is {selected_friend}")