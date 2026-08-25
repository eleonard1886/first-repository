def check_acces(func):
    def wrapper(employee: dict):
        if employee.get('role') == 'admin':
            return func(employee)
        else:
            print(f"Access denied for employee: {employee['name']}")
    return wrapper





@check_acces
def delete_employee(employee: dict):
    print(f"Deleting employee: {employee['name']}")


delete_employee({'name': 'Alice', 'role': 'admin'})
delete_employee({'name': 'Bob', 'role': 'user'})