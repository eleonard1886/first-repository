class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    @property
    def area(self) -> float:
        return 3.14 * self.radius ** 2

    @property
    def radius(self) -> float:
        return self.radius

Circle1 = Circle(5)
print(f"Area of Circle1: {Circle1.area}")  # Output: Area of Circle1: 78.5