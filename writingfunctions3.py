# writingfunctions3.py
# Ben Underwood

def is_even(n):
    """Returns True if n is even, False otherwise."""
    return n % 2 == 0

def calculate_total(meal_cost, tip_percentage, tax_percentage):
    """Calculates the total meal cost including tip and tax."""
    tip = meal_cost * (tip_percentage)
    tax = meal_cost * (tax_percentage)
    total_cost = meal_cost + tip + tax
    return round(total_cost)


def main():
    number = int(input("Enter a number to check if it's even: "))
    if is_even(number):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

    meal_cost = float(input("Enter the meal cost: "))
    tip_percentage = float(input("Enter the tip percentage (as a decimal): "))
    tax_percentage = float(input("Enter the tax percentage (as a decimal): "))
    total = calculate_total(meal_cost, tip_percentage, tax_percentage)
    print(f"The total meal cost is: {total}")

if __name__ == "__main__":
    main()