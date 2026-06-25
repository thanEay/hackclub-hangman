from utils import *
from ascii_sprites import sprites, freed_sprites
import os

mode_input = input("Would you like to set your own word or randomly generate one?\n"\
                   "Enter 'm' for manual input or 'r' for a random word. Start with '!' "\
                   "to enable infinite guessing. For example, '!m' or '!r'.\n")
# Get game mode from user (manual or random word)
try:
    mode, disable_counter = ask_mode(mode_input)
except ValueError:
    print(f"'{mode_input}' is not an appropriate mode. Try 'm' for manual word input "\
          f"or 'r' for random word input. Start with '!' to enable infinite guessing. "\
          f"For example, '!m' or '!r'.")
    exit()

# Initialize game state variables
counter = 0
already_guessed_letters = []
already_guessed_words = []
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
while disable_counter or counter < 8:
    user_input = input("Enter a letter to guess, or start your guess with '!' to guess "\
                       "an entire word: ").strip().lower() 
    if user_input in already_guessed_letters:
        print("You already guessed that letter.")
        continue # Goes to next loop

    # If the first character of the user input is not '!', do normal things
    try:
        if user_input[0] != "!":
            try:
                old_counter = counter
                indexes, message, counter = ask_for_letter(secret_word, f"{user_input}", counter, 
                                                already_guessed_letters, uncovered_indicies,
                                                already_guessed_words)
                if disable_counter:
                    counter = old_counter
                os.system('cls' if os.name == 'nt' else 'clear')
                print(message)
                if -1 not in indexes:
                    for index in indexes:
                        printed_word[index] = user_input
                print("".join(printed_word))
                if not disable_counter:
                    print(f"Incorrect answers left: {8 - counter}")
                    print(sprites[counter])
            except ValueError:
                print("Enter a single letter or a word beginning with '!', such as '!hangman'.")

        # If the first character of the user input is '!', guess the entire word
        else: 
            if user_input[1:] not in already_guessed_words:
                try:
                    old_counter = counter
                    correct_word_bool, message, counter = guess_word(secret_word, user_input[1:],
                                                                    counter)
                    if disable_counter:
                        counter = old_counter
                    if correct_word_bool:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"{message} Congratulations! 🎉")
                        if freed_sprites[counter] != "" and not disable_counter:
                            print(freed_sprites[counter])
                        exit()
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        already_guessed_words.append(user_input[1:])
                        if already_guessed_letters == []:
                            print(f"{message} You have already guessed {', '.join(already_guessed_words)}.")
                        else:
                            print(f"{message} You have already guessed {', '.join(already_guessed_letters)}, "\
                            f"{', '.join(already_guessed_words)}.")
                        print("".join(printed_word))
                        if not disable_counter:
                            print(f"Incorrect answers left: {8 - counter}")
                            print(sprites[counter])
                        continue
                except ValueError:
                    pass
            else:
                print(f"You have already guessed that word. You have already guessed "\
                    f"{', '.join(already_guessed_letters)}, {', '.join(already_guessed_words)}.")
    except IndexError:
        print("Enter a valid input.")

# Check if player has found all letters
    if '_' not in printed_word:
        print(f"You guessed the word: {secret_word}. Congratulations! 🎉")
        exit()

print(f"Game Over! The word was '{secret_word}'")
exit() 