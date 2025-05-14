import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]

user_cards = []
computer_cards = []

def deal_card():
    user_first_card = random.choice(cards)
    user_second_card = random.choice(cards)
    cpu_first_card = random.choice(cards)
    cpu_second_card = random.choice(cards)

    user_cards.append(user_first_card)
    user_cards.append(user_second_card)
    computer_cards.append(cpu_first_card)
    computer_cards.append(cpu_second_card)

    print(user_cards)
    print(computer_cards)


deal_card()

def calculate_score(hand1, hand2):
    total_user = sum(hand1)
    total_computer = sum(hand2)
    return (total_user, total_computer)

print(f"You drew: {user_cards}")
print(f"Your opponent drew: {computer_cards}")

print("Total scores:")
print((calculate_score(user_cards, computer_cards)))