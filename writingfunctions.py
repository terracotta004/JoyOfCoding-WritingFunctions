# writingfunctions.py
# Ben Underwood

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(f"The sum of {x} and {y} is {add(x, y)}")
    print(f"The product of {x} and {y} is {multiply(x, y)}")

if __name__ == "__main__":
    main()