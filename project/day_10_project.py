# DAY 10 PROJECT
# Calculator in Python that does all 4 basic arithmetic operations, but has the feature of reusing the result of the previous operation as input for the next calculation.

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(operations["*"](4, 8))

def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Which operation are you choosing?: ")
        num2 = float(input("What is the second number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input("Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation.\n")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            # function recursion
            calculator()

calculator() 