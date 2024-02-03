# import dependencies A dependency is libary or module that our code needs to funtion.

import time # to make code interactive
from colorama import Fore, Style, init

# launch colorama
init(autoreset = True)

player_score = 0

def introduction():
    # Welcome the Player
    print(Fore.LIGHTMAGENTA_EX + "Welcome to the game adventure")

    time.sleep(1)
    player_name = input(Fore.LIGHTCYAN_EX + "What's your name? ")
    time.sleep(1)
    Favorite_pet = input(Fore.LIGHTYELLOW_EX + "What is your favorite pet? ")
    time.sleep(1)
    print(Fore.LIGHTWHITE_EX+"Make choices to navigate through the adventure")
    time.sleep(1)
    print(Fore.LIGHTBLUE_EX+f"Hello {player_name} you find yourself in a scary forest with a magical {Favorite_pet}")
    time.sleep(2)
    print( Fore.LIGHTGREEN_EX +f"The magical {Favorite_pet} says hi {player_name} i am your magical pet tell me to do something and i will do it")
    time.sleep(2)
    print("but sadly i dont have a name will you like to name me")
    time.sleep(2)
    pet_name = input(Fore.LIGHTGREEN_EX + "what will you like to name your pet")
    time.sleep(1)
    print(Fore.GREEN+f"i love the name {pet_name}")
show = introduction()

