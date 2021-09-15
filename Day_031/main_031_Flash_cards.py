from tkinter import *
import pandas
import random

# keep current card as global to use it in different functions
current_card = None

def main():
    global current_card
    # create new card from Card class and initialize it's attributes
    current_card = Card()
    # start new card function to select random word from file
    current_card.new_card()
    # UI setup
    card_canvas.itemconfig(card_image, image=card_front)
    card_canvas.itemconfig(card_title, text='Danish', fill='black')
    card_canvas.itemconfig(word, text=current_card.danish_word.strip(), fill='black')
    # update window to show danish word before waiting 3s and showing translation
    window.update()
    window.after(3000)
    # reverse card UI and current card attributes
    card_canvas.itemconfig(card_image, image=card_back)
    card_canvas.itemconfig(card_title, text='English | Polish', fill='white')
    card_canvas.itemconfig(word, text=f"{current_card.english_translation.strip()} | "
                                      f"{current_card.polish_translation.strip()}", fill='white')

def decision(keyword):
    """Allows user to choose if given word is known, and will be erased from database,
    or it's not known and will repeat."""
    # using global variable of current card (word)
    global current_card
    # if user clicks green button the word is known and will be removed
    if keyword == 'remove':
        # trigger removing function (shows error beacuse at the moment current card has no Object assigned)
        current_card.remove_word()
        # after deleting word, repeat program
        main()
    else:
        # if word is not known and user press red button, repeat program
        main()

# ---------------------------- CARD CLASS ------------------------------- #
class Card:
    # after initialization card has translation attributes
    def __init__(self):
        self.danish_word = ''
        self.english_translation = ''
        self.polish_translation = ''

    def new_card(self):
        """Draws a random word from CSV file, and assigns it's translations to Object attributes."""
        # try to read table from CSV file
        try:
            words = pandas.read_csv('data/words_to_learn.csv')
        # if first run of a program it will fail to read "words_to_learn" and will read from "danish_words"
        except FileNotFoundError:
            words = pandas.read_csv('data/danish_words.csv')
            # create copy of main file, from which known words will be erased
            words.to_csv('data/words_to_learn.csv')
        # select random Danish word from a file
        self.danish_word = random.choice(words['Danish'])
        # extract whole row for randomly selected word
        new_word_row = words[words['Danish'] == self.danish_word]
        # extract value from English and Polish column for drawn word
        self.english_translation = new_word_row['English'].values[0]
        self.polish_translation = new_word_row['Polish'].values[0]

    def remove_word(self):
        """Removes word from the poll."""
        # read from "editable" file
        words = pandas.read_csv('data/words_to_learn.csv')
        # assign all words BUT the one selected to be removed to variable
        to_save = words[words['Danish'] != self.danish_word]
        # pass variable (DataFrame) to CSV file, overwriting current values
        to_save.to_csv('data/words_to_learn.csv', mode='w')

# ---------------------------- UI SETUP ------------------------------- #
# Constants
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ('Calibri', 30, 'italic')
WORD_FONT = ('Calibri', 50, 'bold')

# Windows setup and image load
window = Tk()
window.title("Danish  ->  English | Polish Flash Cards")
window.config(bg=BACKGROUND_COLOR)
window.minsize(width=1000, height=700)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
right_image = PhotoImage(file='images/right.png')
wrong_image = PhotoImage(file='images/wrong.png')

# Canvas
card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = card_canvas.create_image(400, 263, image=card_front)
card_title = card_canvas.create_text(400, 100, text='Title', font=TITLE_FONT)
word = card_canvas.create_text(400, 300, text='WORD', font=WORD_FONT)
card_canvas.place(x=100, y=39)

# Buttons
right_button = Button(image=right_image, command=lambda: decision("remove"))
wrong_button = Button(image=wrong_image, command=lambda: decision("keep"))
right_button.place(x=700, y=560)
wrong_button.place(x=180, y=560)

if __name__ == "__main__":
    main()

window.mainloop()

