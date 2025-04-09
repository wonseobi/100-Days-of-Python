# DAY 6 PROJECT
# Reeborg's World Code Solutions

# Alone

def build_square():
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()

def build_square_two():
    turn_left()
    turn_left()
    turn_left()
    move()

def build_square_three():
    turn_left()
    turn_left()
    turn_left()
    move()

build_square()
build_square_two()
build_square_three()

# Hurdle No. 1

my_list = [1,2,3,4,5,6]

def advance():
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()

for i in my_list:
    advance()

# Hurdle 3 

def advance():
    if wall_in_infront():
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
        move()
        turn_left()
    elif front_is_clear and not wall_in_front():
        move()

while not at_goal():
    advance()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# Maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()