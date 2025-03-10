import art


def add(n1, n2):
    """
    Adds n1 to n2 returning the value
    """
    return n1 + n2

def sub(n1, n2):
    """
    Subtracts n2 to n1 returning the value
    """
    return n1 - n2

def mul(n1, n2):
    """
    Multiplies n1 to n2 returning the value
    """
    return n1 * n2

def div(n1, n2):
    """
    Divides n2 to n1 returning the value
    """
    return n1 / n2

# This dictionary stores the functions by their symbol to make easier use of the operations
calculator_operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}


def calculator():
    """
    This function is a calculator that can keep using the value calculated before
    or can be restarted. This also has the option to stop
    """

    calculator_on = True

    # The calculator stops after the user choose the stop option
    while calculator_on:
        print(art.logo)

        f_number = float(input("Type the first number: "))

        accumulated_value = True

        # This cycle is used if the user chooses to keep the value of the operation he had done before
        while accumulated_value:
            print("Between the following operators")

            for symbol in calculator_operations:
                print(symbol)

            operator = input("Type the one you want to preform the operation: ")
            s_number = float(input("Type the second number: "))

            total = calculator_operations[operator](f_number, s_number)

            print(f"{f_number} {operator} {s_number} = {total}")

            # Here the user makes the choice to
            # 'y': continue with the last calculated value,
            # 'n': restart the calculator or
            # 'e': exit the program
            choice = input("Choose one of the options bellow\n"
                           f"Type 'y' to continue the calculations using {total}\n"
                           "Type 'n' to reset the calculator\n"
                           "Type 'e' to exit the calculator\n"
                           "Choice: ")

            if choice == "y":
                f_number = total

            if choice == "n":
                print("\n" *40)
                calculator()

            elif choice == "e":
                accumulated_value = False
                calculator_on = False

calculator()