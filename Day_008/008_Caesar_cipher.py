from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode_decode_function(message, shift, type):

    splited_message = list(message)
    encoded_message = ""

    for letter in splited_message:

        # original index is the same no matter the function
        original_index = alphabet.index(letter)

        # if function is "encode" type we execute slightly different code
        if type == "e":

            shifted_index = original_index + shift

            # when we reach end of the alphabet we start over from index 0
            if shifted_index > 25 and type == "e": # 25 - number of letters in alphabet

                shifted_index = (shift - (25 - original_index)) - 1 # -1 because counting starts from 0

        if type == "d":

            shifted_index = original_index - shift

            if shifted_index < 0:

                # we take rest of what's left after reaching 0 and substract it from last letter index
                shifted_index = 25 - (shift - (original_index + 1))

        # joining whole word
        encoded_message += alphabet[shifted_index]

    print(encoded_message)

# function allows to decide after each encryption/decryption what to do next, go again or quit
def whats_next():

    answer = input("What do you want to do next? (q)uit or go (a)gain?\n")

    if answer == "a":
        main()
        
    else:
        quit()

def main():

    print(logo)
    program_function = input("Choose a function: (e)ncode || (d)ecode\n")
    message = input("Type your message: \n")
    shift = int(input("Type the shift number: \n"))

    if program_function == "e":

        encode_decode_function(message, shift, "e")
        whats_next()

    elif program_function == "d":

        encode_decode_function(message, shift, "d")
        whats_next()

if __name__ == "__main__":
    main()