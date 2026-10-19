
from calculator.operations import (
    add,
    subtract,
    multiply,
    divide,
    modulo,
)


def main():
    while True:
        print("\n=== Simple Calculator ===")
        print("+  Addition")
        print("-  Subtraction")
        print("*  Multiplication")
        print("/  Division")
        print("%  Modulo (remainder)")
        print("q  Quit")

        choice = input("Choose an operation: ").strip()

        if choice == "q":
            print("Goodbye!")
            break

        if choice not in ("+", "-", "*", "/", "%"):
            print("Invalid choice! Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue

        try:
            if choice == "+":
                result = add(num1, num2)
            elif choice == "-":
                result = subtract(num1, num2)
            elif choice == "*":
                result = multiply(num1, num2)
            elif choice == "/":
                result = divide(num1, num2)
            else:
                result = modulo(num1, num2)

        except ValueError as error:
            print(f"Error: {error}")
            continue

        print("Result:", result)


if __name__ == "__main__":
    main()
