from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')

class QuizInterface:
    # passing quiz_brain and defining what type of Class it has to be
    # for get_next_question method to work
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.minsize(width=350, height=450)
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR)
        # set easy to change score displayed after correct answer
        self.score = 0
        self.score_label = Label(
            text=f'Score: {self.score}',
            padx=20,
            pady=25,
            bg=THEME_COLOR,
            fg='white')
        self.score_label.grid(column=1, row=0, sticky='we')
        # prepare canvas for question text
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas.grid(column=0, row=1, columnspan=2, sticky='we', padx=20, pady=20)
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Question',
            font=FONT,
        )
        # true or false buttons and pictures
        self.true_button_pic = PhotoImage(file='images/true.png')
        self.false_button_pic = PhotoImage(file='images/false.png')
        # if user press one of the buttons trigger functions that check on self quiz object
        # made out of QuizBrain Class if answer is correct
        self.true_button = Button(image=self.true_button_pic, highlightthickness=0, bg=THEME_COLOR,
                                  command=self.true_pressed)
        self.true_button.grid(column=0, row=2, padx=20, pady=40)
        self.false_button = Button(image=self.false_button_pic, highlightthickness=0, bg=THEME_COLOR,
                                   command=self.wrong_pressed)
        self.false_button.grid(column=1, row=2, padx=20, pady=40)
        # trigger method to get new question from the poll
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="That's all folks!")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    # depending on which button is pressed check quiz object for answer, and pass it into feedback function
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    # feedback function changes background color green is answer is correct and red if not
    def give_feedback(self, is_right):
        if is_right:
            self.score += 1
            self.score_label.config(text=f'Score: {self.score}')
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.update()
        # after 2s change background back to white and take next question from the poll
        self.window.after(1000)
        self.canvas.config(bg='white')
        self.get_next_question()
