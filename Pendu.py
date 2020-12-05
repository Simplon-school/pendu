import random


# List of words that we will choose from
list_of_fruits = ["banana", "apple", "orange", "coconut", "strawberry"]
list_of_French_cities = ["meaux", "pessac", "nice", "albi", "amiens"]
# Module "choice" to choose a word from list_of_words randomly
word_to_guess = random.choice(list_of_French_cities)

# print("word_to_guess: ", word_to_guess)

# List of letters guessed from the player
found_letters = []

# # List of error letters guessed from the player
error_lists = []


# Mask the word
def mask_word():
    return "_"*len(word_to_guess)


print(mask_word())

"""
Generate the mask of guessed word.
    if it is not exist --> put "_"
    if it is exist --> put the guessed letter in the specified position
"""


def generated_mask(mask_word, guess_word):
    for letter in guess_word:
        if letter in found_letters:
            mask_word += letter
        else:
            mask_word += "_"

    return mask_word





