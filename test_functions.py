from utils import *

# appropriate_values = ['value1', 'value2', 'value3']
secret_word = choose_random_word()
counter = 0
already_guessed = []

# index, message = ask_for_letter(secret_word, "e", counter, already_guessed) # type: ignore

# print(index)
# print(message)

printed_word = []
for character in secret_word:
    printed_word.append("_")

print("".join(printed_word))