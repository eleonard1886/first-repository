def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract two numbers"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Error: Division by zero"
    return a / b


def power(a, b):
    """Raise a number to a power"""
    return a ** b


def modulo(a, b):
    """Get the remainder of division"""
    if b == 0:
        return "Error: Division by zero"
    return a % b




if __name__ == "__main__":
    print("Calculator Operations:")
    result1 = add(10, 5)
    print(f"Addition: 10 + 5 = {result1}")
    result2 = subtract(10, 5)
    print(f"Subtraction: 10 - 5 = {result2}")
    result3 = multiply(10, 5)
    print(f"Multiplication: 10 * 5 = {result3}")
    result4 = divide(10, 0)
    print(f"Division: 10 / 0 = {result4}")
    result5 = power(2, 3)
    print(f"Power: 2 ^ 3 = {result5}")
    result6 = modulo(10, 3)
    print(f"Modulo: 10 % 3 = {result6}")
    