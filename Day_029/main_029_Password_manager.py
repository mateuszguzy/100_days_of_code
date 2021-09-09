from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [letter for letter in random.choices(letters, k=nr_letters)]
    password_list += [symbol for symbol in random.choices(symbols, k=nr_symbols)]
    password_list += [number for number in random.choices(numbers, k=nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)

    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def transfer_to_file():
    w = website_entry.get()
    u = username_entry.get()
    p = password_entry.get()

    if len(w) == 0:
        messagebox.showinfo(title="Not enough data!", message="Please enter website to save data.")
    elif len(p) == 0:
        messagebox.showinfo(title="Not enough data!", message="Please enter password to save data.")
    else:
        is_ok = messagebox.askokcancel(title="Save?", message=f"Do you want to save credentials for "
                                                              f"{w}?\n\nUsername: {u}\nPassword: {p}")

        if is_ok:
            with open('data.txt', mode='a') as file:
                data_string = f'{w} | {u} | {p}\n'
                file.write(data_string)
                # delete existing data after saving in a file
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
FONT = ('Arial', 10)

website_label = Label(text="Website", font=FONT)
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username", font=FONT)
username_label.grid(column=0, row=2)

password_label = Label(text="Password", font=FONT)
password_label.grid(column=0, row=3)

# Entries
PADDING = 2

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky='we', pady=PADDING)

username_entry = Entry(width=21)
username_entry.insert(0, string="name@email.com")
username_entry.grid(column=1, row=2, sticky='we', pady=PADDING)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky='we', pady=PADDING)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password, font=FONT)
generate_button.grid(column=2, row=3, sticky="e")

add_button = Button(text="Add", command=transfer_to_file, font=FONT)
add_button.grid(column=1, row=4, columnspan=3, sticky="we")





window.mainloop()
