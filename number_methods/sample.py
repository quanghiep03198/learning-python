def create_number_sample():
    # Basic arithmetic operations
    a = 10
    b = 3
    print(f"Basic operations with {a} and {b}:")
    print(f"Addition: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")
    print(f"Division: {a / b}")
    print(f"Floor Division: {a // b}")
    print(f"Modulus: {a % b}")
    print(f"Power: {a ** b}")

    # Built-in number methods
    num = -15.75
    print(f"\nBuilt-in methods for {num}:")
    print(f"Absolute value: {abs(num)}")
    print(f"Round: {round(num)}")
    print(f"Round to 1 decimal: {round(num, 1)}")

    # Math module functions
    import math

    x = 16
    print(f"\nMath module functions:")
    print(f"Square root of {x}: {math.sqrt(x)}")
    print(f"Floor of {num}: {math.floor(num)}")
    print(f"Ceiling of {num}: {math.ceil(num)}")
    print(f"Pi constant: {math.pi}")
    print(f"e constant: {math.e}")

    # Type conversion
    print("\nType conversion:")
    print(f"Integer conversion: {int(5.7)}")
    print(f"Float conversion: {float(5)}")
    print(f"Complex number: {complex(3, 4)}")


if __name__ == "__main__":
    create_number_sample()
