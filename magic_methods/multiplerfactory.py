class MultiplierFactory:
    """A callable factory that stores a multiplier and applies it to values.

    This class demonstrates magic methods by customizing instance creation
    with __new__, initialization with __init__, and call behavior with __call__.
    When an instance is called like a function, it multiplies the given value
    by the stored factor.
    """

    def __new__(cls, factor: int):
        print(f'Creating a new MultiplierFactory instance with multiplier: {factor}')
        return super().__new__(cls)
    

    def __init__(self, factor: int):
        print(f'Initializing MultiplierFactory instance with multiplier: {factor}')
        self.multiplier = factor


    def __call__(self, value: int) -> int:
        print(f'Calling MultiplierFactory instance with value: {value}')
        return value * self.multiplier


mult = MultiplierFactory(3)
print(mult(5))  # Output: 15