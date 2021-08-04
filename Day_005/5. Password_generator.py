import random

password_length = int(input("How long your password should be?\n"))
special_characters_amount = int(input("How many special characters should password contain?\n"))
numbers_amount = int(input("How many numbers should password contain?\n"))
letters_amount = password_length - special_characters_amount - numbers_amount

if letters_amount < 0:
    print("Error 1: Choosen more special characters, than total password length!")
    exit()

password_index_list = []
all_characters = []
password = ''
alphabet = []
special_characters_list = []

# create list of available letters, from ASCII table

for a in range(65, 91):

    alphabet.append(chr(a))

for a in range(97, 123):
    
    alphabet.append(chr(a))

# create list of possible characters positions in password to withdraw from during character locating

for i in range(0, password_length):
    password_index_list.append(i)

# create list of available special characters, from ASCII table

for s in range(33, 48):
    special_characters_list.append(chr(s))

for s in range(58, 65):
    special_characters_list.append(chr(s))

# random selection of characters from previously prepared lists

selected_numbers = random.choices(range(0, 9), k = numbers_amount)
selected_letters = random.choices(alphabet, k = letters_amount)
selected_special_characters = random.choices(special_characters_list, k = special_characters_amount)
all_characters = selected_letters + selected_numbers + selected_special_characters

for position in password_index_list:

    # random selection of character to be assigned to "position" in password

    choosen_character = random.choice(all_characters)
    password += str(choosen_character)

    # remove choosen character from pool to not be choosen again

    all_characters.remove(choosen_character)

print(password)
