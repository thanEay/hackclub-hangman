import random
from random_words import hangman_words

# Utility functions for the hangman game.
# These helpers support choosing the game mode, checking letters, and selecting words.
# In other words, this code does most of the heavy lifting for the hangman game.

def ask_mode(user_input: str) -> str:
    """Return a variable to determine manual or random word choice. 
    
    Args: 
        user_input: The input by the user.
    
    Returns: 
        Either "manual" or "random" strings.
    
    Raises: 
        ValueError: If the input is not one of the expected values.
    """
    user_input = user_input.strip().lower()
    # Acceptable user responses for manual vs random word selection.
    appropriate_values = ["manual", "m", "random", "automatic", "auto", "input", "r", "a", "i"]
    if user_input not in appropriate_values:
        raise ValueError(f"Invalid input: '{user_input}'. Expected one of appropriate values: {appropriate_values}")

    # Map user input to a mode.
    if user_input in ["manual", "m"]:
        mode = "manual"
    if user_input in ["random", "automatic", "auto", "input", "r", "a", "i"]:
        mode = "random"
    return mode

def check_letter(word: str, letter: str) -> int:
    """
    Returns the location of a letter in a word.
    
    Args:
        word: Word to search.
        letter: Letter to search the word for.
    
    Returns: 
        The resulting index of the letter in the word. If the letter is not found in
        the word, it returns -1.

    Raises:
        ValueError: The input is not a letter with a length of 1.
    """
    if isinstance(letter, str) and len(letter) == 1:
        location = word.find(letter)
        return location # If letter is not in the word, will result in index of -1
    raise ValueError(f"Invalid input: {letter}. Expected string with length of 1.")

# Choose a secret word for the game from the predefined word list.
def choose_random_word() -> str:
    """Returns a random word (all lower) from random_words.py file."""
    return random.choice(hangman_words)

# Check a guessed letter and prepare the response message for the game.
def ask_for_letter(word: str, letter: str, counter: int, already_guessed: list,
                   uncovered_indicies: list):
    """Letter checking and incorrect answer counter logic. 
    
    Args:
        word: Secret word being guessed.
        letter: Letter to search the word for.
        counter: The number of incorrect answers this game, results in hangman sprite change.
        already_guessed: A list of characters that were already guessed. Prevents the
        player from increasing the counter on a letter that was already guessed. 
        uncovered_indicies: A list of indicies that map to correctly guessed (and
        therefore uncovered) letters in the secret word.
    
    Returns:
        Tuple[int, str]: The position of the letter and a user-facing message.
    
    Raises: 
        ValueError: If the input is not a single character.
    """
    index = check_letter(word, letter)
    try:
        # If the guessed letter exists in the word, append it to guessed letters.
        if index != -1:
            already_guessed.append(letter)
            message = f"{letter} is in the word at index {index}."
            uncovered_indicies.append(index)
            return index, message

        # Handle the case where the guessed letter is not present, when 
        # index == -1.
        message = f"'{letter}' is NOT in the word."
        already_guessed.append(letter)
        return index, message
    except ValueError:
        # Inform the user about invalid input, such as digits or multiple characters.
        print("Enter a single letter. No numbers or special characters are allowed.")
        raise ValueError(f"Invalid input: {letter}. Expected string with length of 1.")
    
