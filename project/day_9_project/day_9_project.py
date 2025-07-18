# DAY 9 Project
# Private bidding program, will ask for name for each user, amount to bid, and calculates the highest bid 
from art import welcome_message

print(welcome_message)
print("Welcome to the Private Bidding Program!")

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
        elif should_continue == "yes":
            print("\n" * 20)

    print(f"The winner is {winner} with a bid of ${highest_bid}")


continue_bidding = True

bids = {}

while continue_bidding:
    
    name = input("What is your name?: ")
    price = int(input("What is your bid: $"))
    
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)