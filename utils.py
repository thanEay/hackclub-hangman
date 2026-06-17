import random

def ask_mode(input: str):
    if input.strip().lower() in ["manual", "m"]:
        mode = "manual"
    if input.strip().lower() in ["random", "automatic", "auto", "input", "r", "a", "i"]:
        mode = "random"
    return mode

def check_letter(word: str, letter: str):
    if letter in word:
        location = word.find(letter)
        if isinstance(location, int):
            return location # If letter is not in the word, will result in index of -1
        else: 
            return "Please input a letter"