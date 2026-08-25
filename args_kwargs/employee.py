class Employee:

    def __init__(self,name:str,*args,**kwargs):
        self.name = name
        self.args = args
        self.kwargs = kwargs


    def __str__(self):
        return f"Employee Name: {self.name}, Args: {self.args}, Kwargs: {list(self.kwargs.keys())}"


employee = Employee("John Doe", 30, "Engineer", department="IT", location="New York")
print(employee)  # Output: Employee Name: John Doe, Args: (30, 'Engineer'), Kwargs: ['department', 'location']