from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = \
        {
            website:
                {
                    'Username': username,
                    'Password': password
                },
        }
    # check if user filled all blank places, if not prompt an error
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Not enough data!", message="Please enter needed data.")
    # if all data is filled confirm if it's correct and user want to save
    else:
        # .askokcancel returns boolean value
        is_ok = messagebox.askokcancel(title="Save?", message=f"Do you want to save credentials for {website}?"
                                                              f"\n\nUsername: {username}\nPassword: {password}")

        if is_ok:
            try:
                with open('data.json', mode='r') as file:
                    file_data = json.load(file)
                    file_data.update(new_data)
            except FileNotFoundError:
                with open('data.json', mode='w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open('data.json', mode='w') as file:
                    json.dump(file_data, file, indent=4)
            finally:
                # delete existing data after saving in a file
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- SEARCH ENTRY ------------------------------- #
def search():

    try:
        with open('data.json', mode='r') as file:
            file_data = json.load(file)
            data_to_search = website_entry.get()
    except FileNotFoundError:
        messagebox.showinfo(title="Oops!", message="File not found!")

    else:
        if len(data_to_search) == 0:
            messagebox.showinfo(title='Oops!', message='Fill website name you want to search for.')
        else:
            try:
                record = file_data[data_to_search]
            except KeyError:
                messagebox.showinfo(title="Oops!", message="Record not found!")
            else:
                username = record['Username']
                password = record['Password']
                messagebox.showinfo(title='Record found!', message=f'Credentials for {data_to_search}\n\n'
                                                                   f'Username: {username}\nPassword: {password}')
            finally:
                # delete existing data after search
                website_entry.delete(0, END)

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
website_entry.grid(column=1, row=1, columnspan=1, sticky='we', pady=PADDING)

username_entry = Entry(width=21)
username_entry.insert(0, string="name@email.com")
username_entry.grid(column=1, row=2, sticky='we', pady=PADDING)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky='we', pady=PADDING)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password, font=FONT)
generate_button.grid(column=2, row=3, sticky="e", padx=10)

add_button = Button(text="Add", command=transfer_to_file, font=FONT)
add_button.grid(column=1, row=4, columnspan=3, sticky="we", pady=5)

search_button = Button(text="Search", command=search, font=FONT)
search_button.grid(column=2, row=1, sticky="we", padx=10)

window.mainloop()
