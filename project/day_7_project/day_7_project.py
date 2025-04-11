# DAY 7 PROJECT
# Hangman game using If/Else conditionals, lists, Python functions, and my own functions
import random
from hangman_words import word_list
from hangman_words import stages
from hangman_words import logo

# To Do 1 
lives = 6

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word) # Debugging

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False 
correct_letters = []

while not game_over:

    print(f"You have {lives}/6 LIVES left")

    guess = input("Guess a letter > ").lower()

    if guess in correct_letters:
        print(f"You have already guessed {guess}!")

    display = ""

    for i in chosen_word:
        # Add letter to blank space
        if i == guess:
            display += i
            correct_letters.append(guess)
        # ignore for repeated guesses
        elif i in correct_letters:
            display += i
            
        # Keep blank space
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the word, you lose a life")
        if lives == 0:
            game_over = True
            print(f"The correct word was {chosen_word}")
            print("You LOSE.")

    if display == chosen_word:
        print("You WIN!")
        game_over = True

    print(stages[lives])