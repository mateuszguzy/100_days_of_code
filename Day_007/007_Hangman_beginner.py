import hangman_art, hangman_words, random

print(hangman_art.logo)
guessed_word =  random.choice(hangman_words.word_list) #hangman_words.word_list[13]
hint = "_ " * len(guessed_word) + "\n"

# define how many tries user has (defined by graphic stages)
mistakes = 6

print(hint)
# print(guessed_word)

def letter_guess(hint, mistakes):

    splitted_hint = hint.split()

    while "_" in hint:

        guess = input("Guess a letter: ")
        joined_hint = ""
        index = 0
        found = 0

        for letter in guessed_word:

            if letter == guess:

                # need to apply index to start searching for another result at the last found letter
                # otherwise it will match all the time the same letter index
                splitted_hint[guessed_word.find(letter, index)] = guess
                index = guessed_word.find(letter, index) + 1

                # count founded letters, if no match at all, able to print next hangman step
                found += 1

        # if found any matches print current hangman state
        if found != 0:

            print("You guessed: %s, and it's correct." % guess)
            print(hangman_art.stages[mistakes])

        # if no match, print next hangman step
        elif found == 0:
            
            print("You guessed: %s, and it's wrong." % guess)
            mistakes -= 1
            print(hangman_art.stages[mistakes])

        # if mistakes reach 0, game is over
        if mistakes == 0:

            print("GAME OVER ! YOU LOSE !")
            print("The word was: %s" % guessed_word)
            quit()

        # add spaces and newlines for better visibility
        for letter in splitted_hint:

            joined_hint += letter + " "
            hint = "\n" + joined_hint + "\n"

        print(hint)

    print("CONGRATULATIONS ! YOU WON !")

letter_guess(hint, mistakes)

