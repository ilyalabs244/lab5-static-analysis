"""Example application for static analysis."""


def calculate_total(price, quantity):
    """Calculate the total price."""
    total = price * quantity
    print("Total:", total)
    return total


def main():
    """Run the application."""
    calculate_total(100, 3)
    print("Development branch")


if __name__ == "__main__":
    main()
