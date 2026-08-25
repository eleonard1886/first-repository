def sum_numbers(**kwargs):
    """Returns the sum of all numbers passed as keyword arguments."""
    return sum(kwargs.values())


sum_result = sum_numbers(a=1, b=2, c=3)
print(sum_result)  # Output: 6