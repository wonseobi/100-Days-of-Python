# DAY 11 PROJECT
# Fully functional Blackjack Game

import random

user_cards = []
computer_cards = []
total_user = 0

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


def calculate_score(hand1, hand2):
    total_user = sum(hand1)
    total_computer = sum(hand2)
    return (total_user, total_computer)

print(f"You drew: {user_cards}")
print(f"Your opponent drew: {computer_cards}")

print("Total scores:")
print((calculate_score(user_cards, computer_cards)))