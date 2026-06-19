from utils import *

# Import necessary utilities
from utils import *

mode_input = input("Would you like to set your own word or randomly generate one?\n")
# Get game mode from user (manual or random word)
try:
    if ask_mode(mode_input) == "manual":
        mode = "manual"
    elif ask_mode(mode_input) == "random":
        mode = "random"
    else: 
        print("Please enter an appropriate mode: 'manual' or 'random'.")
        exit()
except ValueError:
    print(f"'{mode_input}' is not an appropriate mode. Try 'm' for manual word input "\
        "or 'r' for random word input.")
    exit()

# Initialize game state variables
counter = 0
already_guessed = []
uncovered_indicies = []

# Get the secret word based on chosen mode
if mode == "manual":
    secret_word = input("Enter a secret word: ").strip().lower()
if mode == "random":
    secret_word = choose_random_word()

# Create display with underscores for each letter
printed_word = []
for character in secret_word:
    printed_word.append("_")

# Display initial game state
print(f"The word has {len(secret_word)} characters.")
print("".join(printed_word))

# For debug, prints secret word
print(f"DEBUG: {secret_word}")

# Main game loop - continue until player wins or reaches 10 wrong guesses
while counter < 10:
    user_input = input("Enter another letter: ")
    if user_input.strip().lower() in already_guessed:
        print("You already guessed that letter.")
        continue # Goes to next loop
    try: 
        indexes, message = ask_for_letter(secret_word, f"{user_input}", counter, 
                                        already_guessed, uncovered_indicies) # type: ignore
        print(message)
        if -1 not in indexes:
            for index in indexes:
                printed_word[index] = user_input
        print("".join(printed_word))
    except ValueError:
        print("Enter a single letter. No numbers or special characters are allowed.")
# Check if player has found all letters
    if '_' not in printed_word:
        print(f"You guessed the word: {secret_word}. Congratulations! 🎉")
        exit()