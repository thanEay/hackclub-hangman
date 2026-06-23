from utils import *
from ascii_sprites import sprites
import os

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
is_first_loop = True

# Get the secret word based on chosen mode
if mode == "manual":
    secret_word = input("Enter a secret word: ").strip().lower()
if mode == "random":
    secret_word = choose_random_word()
os.system('cls' if os.name == 'nt' else 'clear')

# Create display with underscores for each letter
printed_word = []
for character in secret_word:
    if character != " ":
        printed_word.append("_")
        continue
    printed_word.append(" ")

# Display initial game state
print(f"The word has {len(secret_word)} characters.")
print("".join(printed_word))

# For debug, prints secret word
print(f"DEBUG: {secret_word}")

# Main game loop - continue until player wins or reaches 10 wrong guesses
while counter < 8:
    if is_first_loop:
        user_input = input("Enter a letter to guess: ").strip().lower() # Ponytail ignore this instance
    else:
        user_input = input("Enter another letter: ").strip().lower()
    if user_input in already_guessed:
        print("You already guessed that letter.")
        continue # Goes to next loop

    # If the first character of the user input is not '!', do normal things
    if user_input[0] != "!":
        try: 
            indexes, message, counter = ask_for_letter(secret_word, f"{user_input}", counter, 
                                            already_guessed, uncovered_indicies) # type: ignore
            os.system('cls' if os.name == 'nt' else 'clear')
            print(message)
            if -1 not in indexes:
                for index in indexes:
                    printed_word[index] = user_input
            print("".join(printed_word))
            print(f"Incorrect answers left: {8 - counter}")
            print(sprites[counter])
        except ValueError:
            print("Enter a single letter. No numbers or special characters are allowed.")
    # If the first character of the user input is '!', guess the entire word
    else: 
        try:
            correct_word_bool, message, counter = guess_word(secret_word, 
                                                             user_input[1:],
                                                             counter)
            if correct_word_bool:
                print(message)
            else:
                pass
        except ValueError:
            pass

# Check if player has found all letters
    if '_' not in printed_word:
        print(f"You guessed the word: {secret_word}. Congratulations! 🎉")
        exit()

print(f"Game Over! The word was '{secret_word}'")
exit() 