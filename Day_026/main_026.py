import pandas

code_data = pandas.read_csv('nato_phonetic_alphabet.csv')
code_dict = {row.letter: row.code for (index, row) in code_data.iterrows()}


def main():
    name = input("Write your name: ")

    try:
        code_list = [code_dict[letter.upper()] for letter in name]
        print(code_list)

    except KeyError:
        print("Do not insert numbers.")
        main()

if __name__ == "__main__":
    main()




