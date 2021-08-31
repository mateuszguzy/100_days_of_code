import re


def main():
    # prepare regex to match placeholder inside form
    reg_ex = '\[name\]'
    # open name list and for each name make following operations
    with open('Input/Names/invited_names.txt') as name_file:
        for name in name_file:
            # open letter form
            with open('Input/Letters/starting_letter.txt') as letter:
                # and for each line of letter form
                for line in letter:
                    # search for placeholder and replace it with a name and write each file line by line
                    with open(f'Output/ReadyToSend/letter_to_{name}.txt', mode='a') as letter_to_send:
                        letter_to_send.write(re.sub(reg_ex, name.rstrip(), line))


if __name__ == "__main__":
    main()
