from flask import Flask
import random
app = Flask(__name__)

number_to_guess = random.randint(0, 9)

def bold_decorator(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


@app.route('/')
def main():
    return "<h1>Guess the number from 0 to 9</h1>\n " \
           "<img src=https://media.giphy.com/media/13RcbHeXlLNysE/giphy.gif>"


@app.route('/<int:number>')
def guess(number):
    if number_to_guess == number:
        return f"<h1>Well done!</h1> \n " \
               "<img src=https://media.giphy.com/media/l0Iy7zmLUiALbkna8/giphy.gif>"
    elif number_to_guess > number:
        return "<h1>Try again! Higher next time.</h1> \n" \
               "<img src=https://media.giphy.com/media/VlqzeaRnhCvPLfrSh6/giphy.gif>"
    elif number_to_guess < number:
        return "<h1>Try again! Lower next time.</h1> \n" \
               "<img src=https://media.giphy.com/media/VlqzeaRnhCvPLfrSh6/giphy.gif>"


if __name__ == "__main__":
    app.run(debug=True)
