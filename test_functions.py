"""
This is the place where I tested out functions and code snippets during the making of this project.
This has no use in the final deployed version, but it is here to look at and (maybe) learn from.
"""

from utils import *
from ascii_sprites import sprites, freed_sprites

# appropriate_values = ['value1', 'value2', 'value3']
secret_word = choose_random_word()
counter = 0
already_guessed = []
uncovered_indicies = []

# index, message = ask_for_letter(secret_word, "e", counter, already_guessed) # type: ignore

# print(index)
# print(message)

# index, message = ask_for_letter("stardanceaaaaa", "a", counter, already_guessed, uncovered_indicies)

# printed_word = []
# for character in secret_word:
#     printed_word.append("_")

# print(f"DEBUG: {secret_word}")
# while counter < 10:
#     user_input = input("Enter another letter: ")
#     if user_input.strip().lower() in already_guessed:
#         print("You already guessed that letter.")
#         continue # Goes to next loop
#     try: 
#         indexes, message = ask_for_letter(secret_word, f"{user_input}", counter, 
#                                         already_guessed, uncovered_indicies) # type: ignore
#         print(message)
#         if -1 not in indexes:
#             for index in indexes:
#                 printed_word[index] = user_input
#         print("".join(printed_word))
#     except ValueError:
#         print("Enter a single letter. No numbers or special characters are allowed.")
# # Check if player has found all letters
#     if '_' not in printed_word:
#         print(f"You guessed the word: {secret_word}. Congratulations! 🎉")
#         exit()

# print(message)

# indexes = check_letter(secret_word, 'a')
# print(indexes)

# list = ['stardance', 'hack club', 'foobar', 'python']

# print(", ".join(list))

# print(f"Foobar \033[3mis\033[0m the word!")

# for index, sprite in enumerate(freed_sprites):
#     print(str(index))
#     print(sprites[index])
#     print(sprite)
