import random

# global variables that will be used in other functions
number_of_tries = 0
number_to_guess = random.choice(range(0,101))

def game_mode():
    """Function defines number of tries based on choosen difficulty."""
    global number_of_tries
    answer = input("\nChoose difficulty: 'easy', 'hard'.\n")
    if answer == "easy":
        number_of_tries = 10
    else:
        number_of_tries = 5
        
def number_check(guess):
    """Function used to check if number is correct or give hints if it's to high or to low."""
    global number_to_guess
    # if incorrect number is given show message and ask again
    if guess > 100 or guess < 0:
        print("Wrong number!\n")
        user_guess()
    if guess == number_to_guess:
        print("\nThat's the number! You win!\n")
        quit()
    elif guess < number_to_guess:
        print("Too low.\n")
    elif guess > number_to_guess:
        print("Too high.\n")

def user_guess():
    """Function allows to pass user input and change number of possible tries."""
    global number_of_tries
    # inform user how many tries are left
    print(f"You have {number_of_tries} tries left.")
    # assign user input to returned variable
    guess = int(input("Choose a number:\n"))
    # lower number of left tries
    number_of_tries -= 1
    return guess

def main():
    global number_to_guess
    print("Welcome to 'Guess a number!'")
    print("Guess a number from 0 to 100!")
    # choose game mode - number of tries
    game_mode()
    # perform guesses until no more tries left
    while number_of_tries > 0:
        # assign user input to variable
        guess = user_guess()
        # and pass it into checking function
        number_check(guess)
    # if number is not guessed until run out of tries, end game message is showed
    print("\nYou run out of tries. You lose!")
    print(f"Number you wanted to guess was: {number_to_guess}")

if __name__ == "__main__":
    main()