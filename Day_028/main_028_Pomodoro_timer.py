from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
LIGHT_RED = "#911F27"
RED = "#630A10"
EGGSHELL = "#FCF0C8"
YELLOW = "#FACE7F"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global rep
    rep = 0
    window.after_cancel(timer)
    checkmark['text'] = ""
    title['text'] = "Timer"
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global rep
    rep += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if rep == 8:
        title.config(text="BREAK", fg=EGGSHELL)
        countdown(long_break_sec)
    elif rep % 2 == 0:
        title.config(text="BREAK", fg=EGGSHELL)
        countdown(short_break_sec)
    else:
        title.config(text="WORK", fg=RED)
        countdown(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global rep, timer
    if count > 0:
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec == 0:
            count_sec = "00"
        elif count_sec < 10:
            count_sec = f"0{count_sec}"
        if count_min < 10:
            count_min = f"0{count_min}"
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if rep % 2 == 0:
            checkmark.config(text="✓" * int(rep / 2))
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", fill=EGGSHELL, font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

title = Label(text='TIMER', bg=YELLOW, fg=RED, font=(FONT_NAME, 40, 'bold'))
title.grid(column=1, row=0)

start_button = Button(text="Start", bg=YELLOW, fg=RED, command=start_timer, font=(FONT_NAME, 15, 'bold'))
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, fg=RED, command=reset_timer, font=(FONT_NAME, 15, 'bold'))
reset_button.grid(column=2, row=2)

checkmark = Label(fg=RED, bg=YELLOW, font=(FONT_NAME, 25))
checkmark.grid(column=1, row=3)

window.mainloop()
