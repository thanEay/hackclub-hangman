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
    # Acceptable user responses for manual vs random word selection.
    appropriate_values = ["manual", "m", "man", "random", "rand", "automatic", "auto",
                           "input", "r", "a", "i"]
    if user_input not in appropriate_values:
        raise ValueError(f"Invalid input: '{user_input}'. Expected one of appropriate "\
                         f"values: {appropriate_values}")

    # Map user input to a mode.
    if user_input in ["manual", "m", "man"]:
        mode = "manual"
    if user_input in ["random", "rand", "automatic", "auto", "input", "r", "a", "i"]:
        mode = "random"
    return mode

def check_letter(word: str, letter: str) -> list:
    """
    Returns the location of a letter in a word.
    
    Args:
        word: Word to search.
        letter: Letter to search the word for.
    
    Returns: 
        A list of the resulting index (or indexes) of the letter in the word. If the
        letter is not found in the word, it returns -1.

    Raises:
        ValueError: The input is not a letter with a length of 1.
    """
    if isinstance(letter, str) and len(letter) == 1:
        locations = []
        if word.count(letter) == 1:
            locations = [word.find(letter)]
        elif word.count(letter) > 1: # BUG found here! elif was an if statement
            for index, character in enumerate(word):
                if character == letter:
                    locations.append(index)  
        else:
            locations = [-1]      
        return locations # If letter is not in the word, will result in index of -1
    raise ValueError(f"Invalid input: {letter}. Expected string with length of 1.")

# Choose a secret word for the game from the predefined word list.
def choose_random_word() -> str:
    """Returns a random word (all lower) from random_words.py file."""
    return random.choice(hangman_words)

# Check a guessed letter and prepare the response message for the game.
def ask_for_letter(word: str, letter: str, counter: int, already_guessed: list,
                   uncovered_indicies: list, already_guessed_words):
    """Letter checking and incorrect answer counter logic. 
    
    Args:
        word: Secret word being guessed.
        letter: Letter to search the word for.
        counter: The number of incorrect answers this game, results in hangman sprite change.
        already_guessed: A list of characters that were already guessed. Prevents the
        player from increasing the counter on a letter that was already guessed. 
        uncovered_indicies: A list of indicies that map to correctly guessed (and
        therefore uncovered) letters in the secret word.
        already_guessed_words: A list of words that were already guessed. Printed in the
        message.
    
    Returns:
        tuple[list[int], str, int]: A tuple containing the list of letter positions,
            a message describing the result, and the updated incorrect guess counter.

    Raises:
        ValueError: If the input is not a single character.
    """
    indexes = check_letter(word, letter)
    try:
        # If the guessed letter exists in the word, append it to guessed letters.
        already_guessed.append(letter)
        if -1 not in indexes:
            if len(indexes) == 1:
                if already_guessed_words == []:
                    message = f"{letter} is in the word at index {str(indexes)}. "\
                    f"You have already guessed {", ".join(already_guessed)}."
                else:
                    message = f"{letter} is in the word at index {str(indexes)}. "\
                    f"You have already guessed {", ".join(already_guessed)}, "\
                    f"{", ".join(already_guessed_words)}."
            else:
                message = f"'{letter}' is in the word at indexes {", ".join(map(str, indexes))}\n"\
                f"You have already guessed {", ".join(already_guessed)}."
            uncovered_indicies.append(indexes)
            return indexes, message, counter

        # Handle the case where the guessed letter is not present, when -1 is in 
        # indexes.
        message = f"{letter} is in the word at index {str(indexes)}. "\
        f"You have already guessed {", ".join(already_guessed)}, "\
        f"{", ".join(already_guessed_words)}."
        counter += 1
        return indexes, message, counter
    except ValueError:
        # Inform the user about invalid input, such as digits or multiple characters.
        print("Enter a single letter. No numbers or special characters are allowed.")
        raise ValueError(f"Invalid input: {letter}. Expected string with length of 1.")
    
def guess_word(secret_word, guessed_word, counter):
    """Allow the player to guess an entire word. If guessed incorrectly, the couter 
    goes up one. If guessed correctly, the game is won.

    Args: 
        secret_word: Secret word being guessed of.
        guessed_word: The guess by the player.

    Returns: 
        boolean: Whether or not the guessed word is the same as the secret word.
        message: The message that will be printed to the terminal.
        counter: The number of incorrect answers guessed so far. Increases if the word
                 is guessed correctly.
    
    Raises: 
        TODO
    """
    # try: 
    if secret_word == guessed_word:
        message = f"'{guessed_word}' \033[3mis\033[0m the word!"
        return True, message, counter
    else:
        counter += 1
        message = f"'{guessed_word}' is NOT the word."
        return False, message, counter
    # except ValueError:
    #     # raise ValueError(TODO)
    #     pass