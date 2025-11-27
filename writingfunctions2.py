# writingfunctions2.py
# Ben Underwood

def pyramid(symbol, height):
    """Prints a pyramid of the given symbol and height."""
    for i in range(1, height + 1):
        print(symbol * i)

def absolute_difference(a, b):
    """Returns the absolute difference between a and b."""
    return abs(a - b)

def main():
    sym = input("Enter a symbol for the pyramid: ")
    h = int(input("Enter the height of the pyramid: "))
    pyramid(sym, h)

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"The absolute difference between {num1} and {num2} is {absolute_difference(num1, num2)}")

if __name__ == "__main__":
    main()