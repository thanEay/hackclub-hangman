from random import choice, randint
from utils import *

mode_input = input("Would you like to set your own word or randomly generate one?\n")
if ask_mode(mode_input) == "manual":
    mode = "manual"
elif ask_mode(mode_input) == "random":
    mode = "random"
else: 
    print("Please enter an appropriate mode: 'manual' or 'random'.")
    exit()

counter = 0
already_guessed = []
uncovered_indicies = []

if mode == "manual":
    secret_word = input("Enter a secret word: ")
if mode == "random":
    secret_word = choose_random_word()

while counter < 10:
    user_input = input("Enter another letter: ")
    if user_input.strip().lower() in already_guessed:
        print("You already guessed that letter.")
        continue # Goes to next loop
    try: 
        index, message = ask_for_letter(secret_word, f"{user_input}", counter, 
                                        already_guessed, uncovered_indicies) # type: ignore
        print(message)
    except ValueError:
        print("Enter a single letter. No numbers or special characters are allowed.")