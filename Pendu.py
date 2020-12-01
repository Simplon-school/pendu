from random import choice

# mask all letters

list_of_words = ["banana", "apple", "orange", "coconut", "strawberry"]

word = choice(list_of_words)

print("word: ", word)


def function_mask():
    return "_"*len(word)


print("masked_word: ", function_mask())


def function_guessed():
    error_letters_list = []
    guessed_letter = input("give us a letter:")
    if guessed_letter in list(word):
        index_m = word.find(str(guessed_letter))

        other = function_mask()[:index_m] + guessed_letter + function_mask()[index_m + 1:]
        print(other)
        
    else:
        error_letters_list.append(guessed_letter)

        print(error_letters_list)

        #     break
        # else:
        #     print("this character {} does not exist".format(guessed_letter))
        #     error_list.append(guessed_letter)
        #     print(error_list)


print(function_guessed())
# myString = 'Position of a character'
# print(myString.find('s'))



