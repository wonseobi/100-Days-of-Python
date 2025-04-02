# FIZZ BUZZ CHALLENGE
# Show numbers from 1-100 including, if the number is divisible by 3 print "Fizz", if the number is divisble by 5 print "Buzz", if the number is divisble by 3 AND also 5 print "FizzBuzz".
        
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)