import hangman_art, hangman_words, random

print(hangman_art.logo)
guessed_word = hangman_words.word_list[2] #random.choice(hangman_words.word_list)
hint = "_ " * len(guessed_word) + "\n"
print(hint)
print(guessed_word)

def letter_guess():

    splitted_hint = hint.split()
    guess = input("Guess a letter:\n")

    for letter in guessed_word:

        if letter == guess:            
            
            print("Index: ", guessed_word.find(letter), "Guess", guess)
            splitted_hint[guessed_word.find(letter)] = guess
            print(splitted_hint)

letter_guess()

