import random
from random_words import hangman_words

def ask_mode(input: str) -> str:
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

def check_letter(word: str, letter: str) -> int:
    """
    Returns the location of a letter in a word.
    
    Args:
        word: Word to search
        letter: Letter to search the word for
    
    Returns: 
        The resulting index of the letter in the word. If the letter is not found in
        the word, it returns -1.

    Raises:
        ValueError: The input is not a letter with a length of 1
    """
    if isinstance(letter, str) and len(letter) == 1:
        location = word.find(letter)
        return location # If letter is not in the word, will result in index of -1
    else: 
        raise ValueError(f"Invalid input: {letter}. Expected string with length of 1.")

def choose_random_word() -> str:
    return random.choice(hangman_words)