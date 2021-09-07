from tkinter import *


def clicked():
    miles = user_input.get()
    kilometers = round(float(miles) * 1.609344, 2)
    kilometers_label['text'] = kilometers
    # text.insert(END, kilometers)


# window
window = Tk()
window.title('Miles to Kilometers Converter')
window.minsize(width=200, height=100)

# labels
miles_label = Label(text='miles', font=('Arial', 10))
miles_label.grid(column=2, row=0)

equal_label = Label(text='is equal to', font=('Arial', 10))
equal_label.grid(column=0, row=1)

km_label = Label(text='km', font=('Arial', 10))
km_label.grid(column=2, row=1)

kilometers_label = Label(text='0', font=('Arial', 10))
kilometers_label.grid(column=1, row=1)

# button
button = Button(text='Convert', command=clicked)
button.grid(column=1, row=2)

# input
user_input = Entry(width=10)
user_input.grid(column=1, row=0)


window.mainloop()

