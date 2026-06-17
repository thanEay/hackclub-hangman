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

if mode == "manual":
    secret_word = input("Enter a secret word: ")
if mode == "random":
    secret_word = choose_random_word()