from art import logo
import operator

def decision(result):
    choice = input(f"Do you want to continue calculation on # {result} #?\nType (y)es, or (n)o to perform a new one.\n")

    if choice == "y":
        return "y"
    else:
        return "n"

def operation(first_number, second_number, choosen_operation):
    # using "operator" lookup table, because python doesn't treat string as an operator
    operators = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.truediv}
    operation_result = operators[choosen_operation] (first_number,  second_number)
    return  operation_result

def inputs(first_number):
    operations = ["+", "-", "*", "/"]
    # list all available choices
    for choice in operations:
        print(choice)

    choosen_operation = input("Choose an operator: ")
    second_number = float(input("Type next number: "))
    result = operation(first_number, second_number, choosen_operation)
    # returning all valuable info from last function in line. Will be returned as tuple
    return first_number, choosen_operation,  second_number, result

def main():
    print(logo)
    first_number = float(input("Type first number: "))
    # predefine answer to continue calculations, further function will work until user choose to end it
    answer = "y"

    while answer == "y":
        result = inputs(first_number)
        # printing results of operation() function which were returned as a tuple
        print(f"\n{result[0]} {result[1]} {result[2]} = {result[3]}\n")
        # assign results to arguments allowing to perform continous operation
        answer = decision(result[3])
        first_number = result[3]
    # when user type "n" to perform a new calculation program will start over
    main()

if __name__ == "__main__":
    main()