# DAY 4 PROJECT
# Rock, paper, scissors game that will ask the user for input, and they will play against the computer, which will randomly choose the output. 

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Importing Modules
import random

# Initiating program and asking for user input
print("Welcome to rock, paper, scissors!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors "))

# Declaring some empty variables
computer_choice = random.randint(0, 2)
user_state = None
computer_state = None

# Showing output based on user choice
if user_choice == 0:
    user_state = 0
    print("You chose ROCK")
    print(rock)
    print("The computer is choosing...")
elif user_choice == 1:
    user_state = 1
    print("You chose PAPER")
    print(paper)
    print("The computer is choosing...")
elif user_choice == 2:
    user_state = 2
    print("You chose SCISSORS")
    print(scissors)
    print("The computer is choosing...")
    


if computer_choice == 0:
    computer_state = 0
    print("Computer chose ROCK")
    print(rock)
elif computer_choice == 1:
    computer_state = 1
    print("Computer chose PAPER")
    print(paper)
elif computer_choice == 2:
    computer_state = 2
    print("Computer chose SCISSORS")
    print(scissors)



if user_state == 0 and computer_state == 0:
    print("It's a DRAW!")
elif user_state == 0 and computer_state == 1:
    print("Paper beats rock, you LOSE!")
elif user_state == 0 and computer_state == 2:
    print("Rock beats scissors, you WIN!")
elif user_state == 1 and computer_state == 0:
    print("Paper beats rock, you WIN!")
elif user_state == 1 and computer_state == 1:
    print("It's a DRAW!")
elif user_state == 1 and computer_state == 2:
    print("Scissors beats paper, you LOSE!")
elif user_state == 2 and computer_state == 0:
    print("Rock beats scissors, you LOSE!")
elif user_state == 2 and computer_state == 1:
    print("Scissors beats paper, you WIN!")
elif user_state == 2 and computer_state == 2:
    print("It's a DRAW!")