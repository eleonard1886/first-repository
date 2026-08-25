def divide(a:int, b:int) -> float:

    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers.")

    if b == 0:
        raise ValueError("Denominator cannot be zero.")

    return a / b


try:
    print(divide(10, 0))
except (ValueError, TypeError) as e:
    print(f"Error: {e}")