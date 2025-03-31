# DAY 3 PROJECT
# Treasure Adventure game, with multiple options where the user can choose from, trial and error game, fantasy-like.

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You wake up in an empty cellar room, you have to get out of here...")
print("After noticing two doors up ahead, which one do you choose?")
user_choice_one = int(input("(1) Left or (2) Right? \n"))

if user_choice_one == 1:
    print("The door up ahead opens up to a cliff side")
    print("You go up ahead")
elif user_choice_one == 2:
    print("You go through the right door")
    print("The ground opens up, you fall to your death...")
    print("GAME OVER")
    exit()
else:
    print("You decide to go through the right door")
    print("The ground opens up, you fall to your death...")
    print("GAME OVER")
    exit()

print("""
   ______________________________________________________
   [[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]
   .-.`| `-/-.__/.-'\_.-._,'/`-._'\_.-._`-'_/-._.'|/.-'\-
   \_.-`./`-._'\__.-`-.__.-`--._/--.`-._\`-._\__.-)`-'._/
   `._-'.\_.---._-.\_`-..`\_.---._`-.__.-`'._.--./`-'._,'
   __/`.-/       `.'_`./`.'       '.\__.-`.'    (_.-\_,-.
   `._-/'          |._.-|           |.'`.|       `(_.`-._
   .-',`)          | /`.|           |`-/`|         ;.-'_/
   `\,-/           |\.-'|           |\-'`|          ;\_,-
    -./`._        [[[[[[[[         [[[[[[[[         .',-'
    `.`--.~~-^_~-/.`-._`-.\^~-_~-^/`-.'-,.'\^~-~_^"'`-.'_
    -,.'"-"~^-~_~- - - _- -~^-_.~ - -_ - - -~- . "'"-"-""
    ""-'"-""-"~- _~.^-~-^.-^_.- .^~.-  ~-. ~^_-""-""-"'-"
    jgs ""-'"-"    ~- ^. - ~ -~^ - ~  ^~- ~     ""-"'-'
""")
print("Outside the cellar you have two choices")
print("Either swim or wait a moment, which do you choose?")
user_choice_two = int(input("(1) Swim or (2) Wait \n"))

if user_choice_two == 1:
    print("You jump down and try to swim")
    print("Trout attack you and you die...")
    print("GAME OVER")
    exit()
elif user_choice_two == 2:
    print("You wait a moment and see there's a door up ahead")
    print("You go through the door")
else:
    print("You decide to jump down and try to swim")
    print("Trout attack you and you die...")
    print("GAME OVER")
    exit()


print("""
   ^    / \:/ \      ^               +                        |>
  / \      ^        / \        *    / \    *              |>  |
 /   \             /   \      OnO  :xxx:  OnO             |  III     |>
(_____)           (_____)     I I   I I   I I           /-|\ III i>  |
 |   |  _   _   _  |   |      I I   I I   I I         _|__|__III i   ^
 | O |_| |_| |_| |_| O |     O_O_O_O_O_O_O_O_O     |>\______/III i  ^^^
 |   |   - _^_     |   |     \_______________/     |   !__!__III/\ ^^^^^
 |  _|    //|\\  - |   |      I     ___     I     /\\ ////|====IIII ===
 |   |   ///|\\\   |  -|      I    / i \    I    /\\\/////|====IIII ===
 |-  |_  |||||||   |   |      I   I: i :I   I    | | ||||::::::IIII ===
 |   |   |||||||   |-  |      I___I:_i_:I___I    | | ||||      IIII ===
 |___|___|||||||___|___|                         -----------------------
         (      (
          \      \            . o       c ,              0   \0
           )      )           `'#v-- --v#`'             /0--- :\
           |      |            /'>     <`\              / >  / >
           (      )
            \      \
""")

print("Going through the door you manage to go outside and see three castles afar")
print("Each one behind a gate of distinct colors, Red, Yellow, and Blue")
print("Which one do you choose?")
user_choice_three = int(input("(1) Red, (2) Yellow, or (3) Blue \n"))

if user_choice_three == 1:
    print("You go through the Red door")
    print("A fiery barrel falls on you, burning to death")
    print("GAME OVER")
    exit()
elif user_choice_three == 2:
    print("You go through the Yellow door")
    print("This door leads you to a safe haven.")
    print("YOU WIN! CONGRATULATIONS")
    exit()
elif user_choice_three == 3:
    print("You go through the Blue door")
    print("Beats attack you, and you die...")
    print("GAME OVER")
    exit()
else:
    print("You wait for a moment, not knowing what to do")
    print("The night falls soundly, you die of hunger")
    print("GAME OVER")
    exit()