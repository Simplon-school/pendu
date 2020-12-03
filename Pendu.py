import random
from display_hangman import display_hangman

# List of words that we will choose from
list_of_fruits = ["banana", "apple", "orange", "coconut", "strawberry"]
list_of_French_cities = ["meaux", "pessac", "nice", "albi", "poitiers" ]
# Module "choice" to choose a word from list_of_words randomly
word_to_guess = random.choice(list_of_French_cities)

print("word_to_guess: ", word_to_guess)

# List of letters guessed from the player
found_letters = []

# # List of error letters guessed from the player
error_lists = []

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


def main():
    # The player have var times to play, if he exceed the specified times he loses
    error = 7
    var = len(display_hangman())
    while True:
        var -= 1
        mask = ""

        # The player tries to guess a letter
        guessed_letter = input("give us a letter:")

        # If the guessed letter not in guessed word, append it into the list of error letters
        if guessed_letter not in word_to_guess:
            if guessed_letter not in error_lists:
                error_lists.append(guessed_letter)
                print("error_lists: ", error_lists)
                print(display_hangman()[error - len(error_lists)])
            elif guessed_letter in error_lists:
                print("'{}' is already guessed  and exist in error_lists ".format(guessed_letter))

        if guessed_letter in found_letters:
            print("'{}' is already guessed  and exist in found_letters ".format(guessed_letter))

        # In all cases, the guessed letter will be added to the list of letters guessed
        elif guessed_letter not in found_letters:
            found_letters.append(guessed_letter)
            print("found_letters: ", found_letters)

        # Apply the generated_mask function
        generated_mask(mask, word_to_guess)

        print("mask: ", generated_mask(mask, word_to_guess))
        print("*********************")

        # In the case that the player reached the word guessed, he win.
        if generated_mask(mask, word_to_guess) == word_to_guess:
            print("You win!")
            break

        # In the case that the player exceeded the number of times specified, he loses
        elif var <= 0:
            print("You have exceeded the length of guessed word")
            print("You lose!")
            # print(display_hangman()[0])
            break
