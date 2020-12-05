from Pendu import *
from display_hangman import *

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
                game_over = display_hangman()[error - len(error_lists)]
                print(game_over)
                if game_over == display_hangman()[0]:
                    print("You lose!")
                    print("Guessed word is: ", word_to_guess)
                    break
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


if __name__ == "__main__":
    main()
