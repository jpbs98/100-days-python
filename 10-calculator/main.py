from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for op in operations:
        print(op)

    while True:
        op_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))
        calc_func = operations[op_symbol]
        answer = calc_func(num1, num2)
        print(f"{num1} {op_symbol} {num2} = {answer}")

        cnt_calc = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
        )
        if cnt_calc == "y":
            num1 = answer
        else:
            calculator()


calculator()
