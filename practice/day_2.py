# Program that calcualtes a tip from a bill and splits the bill
# between n amount of people.

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
calc_tip = tip / 100
final_tip = bill * calc_tip
final_bill = round((bill + final_tip) / people)

if people > 1:
    print(f"The final bill is {final_bill} for each person")
else:
    print(f"The final bill is {final_bill}")
