# import dependencies A dependency is libary or module that our code needs to funtion.

import time # to make code interactive
from colorama import Fore, Style, init

# launch colorama
init(autoreset = True)

player_score = 0

def introduction():
    #Welcome the Player
    print(Fore.LIGHTMAGENTA_EX + "Welcome to the adejoke game adventure")
    time.sleep(1)
    player_name = input(Fore.LIGHTCYAN_EX + "What's your name? ")
    time.sleep(1)
    print(Fore.LIGHTBLUE_EX+f"Hello {player_name} you find yourself in a scary forest")

    print(Fore.LIGHTWHITE_EX+"Make choices to navigate through the adventure")



def make_choices(question, options, score_change):
    print(Fore.GREEN + Style.BRIGHT + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            choice = int(input(Fore.LIGHTBLUE_EX + "Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                    # Update global score variable
                global player_score 
                player_score   += score_change[choice - 1]
                return choice
            else:
                print(Fore.RED + Style.BRIGHT + "Invaild choice try again")
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Invaild input. Enter a number") 

def forest_path():
    print(Fore.CYAN + Style.BRIGHT + "You come across a fork in the path")
    time.sleep(1)
    choice = make_choices("Which path do you take?",["Go left", "Go right"],[1, -1])

    if choice == 1:
        print(Fore.GREEN + Style.BRIGHT + "You enconter a friendly squirrel.It leads you to safety")
    else:
        print(Fore.RED + Style.DIM + "Oh no! you stumble into a spider web")

def mountain_climb():
    print( Fore.LIGHTYELLOW_EX + Style.DIM + "Your walking around, and you reach a steep mountain blocking your way. What do you do?")
    time.sleep(1)
    choice = make_choices("How do you climb it?",["Climb a rope", "Climb without equipment"],[1, -1])
    if choice == 1:
        print("Smart choice! The rope helps you climb safely.")
    else:
        print("Uh oh! Climbing without equipment is risky. You slip, but lucky, you catch yourself")

def mystical_cave():
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "You finally get over thr rock and you discover a mystical cave filled with glowing crystal")
    choice = make_choices("What do you do?",["Enter the cave","Continue on your journey"],[1, -1])
    time.sleep(1)
    if choice == 1:
            print(Fore.GREEN + Style.DIM + "The cave is enchanted! You gained magicly powers.")
    else:
            print(Fore.RED + Style.BRIGHT + "You decide to continue on your journey")

    
          
# Main game loop
def play_game():
    introduction()

    # Start of the adventure
    forest_path()
    mountain_climb()
    mystical_cave()

if __name__ == "__main__":
    play_game()