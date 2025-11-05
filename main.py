print("Welcome to the calculator")

calculate_again = "Y"

while calculate_again == "Y":
    symbol = input("Choose +, -, *, / or **: ")

    while True:
        try:
            number1 = number1 = float(input("Choose the first number: "))
            break
        except ValueError:
            print("Please enter a valid number!")

    while True:
        try:
            number2 = number2 = float(input("Choose the second number: "))
            break
        except ValueError:
            print("Please enter a valid number!")

    if symbol == "+":
        number = number1 + number2
    elif symbol == "-":
        number = number1 - number2
    elif symbol == "*":
        number = number1 * number2
    elif symbol == "/":
        number = number1 / number2
    elif symbol == "**":
        number = number1 ** number2
    else:
        symbol = None

    if symbol != None:
        print("The answer is: ", number)
    else:
        print("Invalid symbol try again")

    while True:
        calculate_again = input("Do you want to calculate again? (Y/N): ").upper()
        if calculate_again == "Y" or calculate_again == "N":
            break
        else:
            print("Wrong input")

