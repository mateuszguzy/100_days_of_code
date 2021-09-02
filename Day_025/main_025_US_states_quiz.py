from turtle import Screen, Turtle
import pandas

screen = Screen()
pointer = Turtle()

screen.setup()
# importing map as a background
image = 'blank_states_img.gif'
screen.addshape(image)
pointer.shape(image)
game_is_on = True
correct_guesses = list()
screen.title('U.S. Quiz Game')
states_list = pandas.read_csv('50_states.csv')
# dictionary prepared to create CSV with all missed states
states_to_learn = {'State': list()}


def main():
    while game_is_on:
        # answer after every guess for a new one
        answer = screen.textinput(title=f"{len(correct_guesses)}/50 | Guess a state",
                                  prompt="What's the next state name: ").title()
        # if typed exit, quit the game and list all missed states
        if answer == "Exit":
            break
        # this variable contains either an Object or nothing, in case when it's nothing length is equal to 0
        answer_check = states_list.state[states_list.state == answer]
        # check if guess is correct, and if it wasn't answered before
        if len(answer_check) != 0 and answer_check.values[0] == answer and answer not in correct_guesses:
            row = states_list[states_list.state == answer]
            # values attribute takes single value from a row
            x_cord = row.x.values[0]
            y_cord = row.y.values[0]
            # run function for printing guessed states on screen using turtle
            print_state(answer, x_cord, y_cord)
            correct_guesses.append(answer)
        # if all states are guessed game is over
        elif len(correct_guesses) == 50:
            print("Congratulation! You've guessed all the states!")
            exit()
        # when guess is not good, run program again
        else:
            main()
    # when stopped guessing prepare a list of all missed states
    # it must be present in original table
    for state in states_list.state:
        # and not present in list of correct guesses
        if state not in correct_guesses:
            states_to_learn['State'].append(state)
    # create a new table out of missed states
    new_table = pandas.DataFrame(states_to_learn)
    print(new_table)


def print_state(answer, x_cord, y_cord):
    state = Turtle()
    state.penup()
    state.hideturtle()
    state.goto(x=x_cord, y=y_cord)
    state.write(arg=f"{answer}", align="center", font=("Courier", 10, "normal"))


if __name__ == "__main__":
    main()
