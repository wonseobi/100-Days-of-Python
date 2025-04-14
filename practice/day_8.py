def greet():
    print("Hello")
    print("message")
    print("from a function")


greet()


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"current user {name}")



greet_with_name("Python")


def greet_with_name_age(name, age):
    print(f"Hello {name}")
    print(f"you are {age} years old")
    print("thank you for your time")


greet_with_name_age("Zuckerberg", 40)

def greet_with_location(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


# Positional arguments
greet_with_location("Eve", "Nowhere")

# Keyword arguments
greet_with_location(name = "Invincible", location = "Earth")

# Challenge: Love Calculator
# Create a function that takes two parameters, name1 and name2, and finds the occurences of T R U E and L O V E, combines these two number of times the letter occurs and prints out the final "love score".

def calculate_love_score(name1, name2):
    # for TRUE occurences
    true_score = name1.count('t')
    true_score = true_score + name1.count('r')
    true_score = true_score + name1.count('u')
    true_score = true_score + name1.count('e')
    true_score = true_score + name2.count('t')
    true_score = true_score + name2.count('r')
    true_score = true_score + name2.count('u')
    true_score = true_score + name2.count('e')
    # for LOVE occurences
    love_score = name1.count('l')
    love_score = love_score + name1.count('o')
    love_score = love_score + name1.count('v')
    love_score = love_score + name1.count('e')
    love_score = love_score + name2.count('l')
    love_score = love_score + name2.count('o')
    love_score = love_score + name2.count('v')
    love_score = love_score + name2.count('e')
    final_score = str(true_score) + str(love_score)
    print(f"{final_score}")
    
    
    
calculate_love_score("Kanye West", "Kim Kardashian")


def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
calculate_love_score("Kanye West", "Kim Kardashian")
