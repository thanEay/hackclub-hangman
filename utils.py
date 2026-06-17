import random

def ask_mode(input: str):
    """Return a variable to determine manual or random word choice.
    
    Args: 
        input: The input by the user.
    
    Returns: 
        Either "manual" or "random" strings.
    
    Raises: 
        ValueError: If the input is not one of the expected values
    """
    appropriate_values = ["manual", "m", "random", "automatic", "auto", "input", "r", "a", "i"]
    if input.strip().lower() not in appropriate_values:
        raise ValueError(f"Invalid input: '{input}'. Expected one of appropriate values: {appropriate_values}")
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