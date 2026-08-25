class Employee:
    """Simple Employee class demonstrating @property, setter and deleter.

    The property decorator (@property) turns the salary() method into a
    getter for the attribute 'salary'. The corresponding @salary.setter and
    @salary.deleter define how to set and delete the underlying value.

    Internally we store the value in a private attribute _salary to avoid
    recursive calls to the property methods.
    """

    def __init__(self, name, salary):
        self.name = name
        # use the property setter to validate initial value
        self.salary = salary

    @property
    def salary(self):
        """Getter for salary. Returns the internal _salary value."""
        return self._salary

    @salary.setter
    def salary(self, value):
        """Setter for salary. Validates value before assigning to _salary."""
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

    @salary.deleter
    def salary(self):
        """Deleter for salary. Removes the internal _salary attribute."""
        del self._salary


employee = Employee("John Doe", 50000)
print(employee.name)   # Output: John Doe
print(employee.salary) # Output: 50000


employee.salary = 60000  # Update salary using setters 
print(employee.salary) # Output: 60000

del employee.salary  # Delete salary using deleter