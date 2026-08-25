# Example 1: Unpacking a list into function arguments
# The *operator unpacks the list elements as individual arguments to the function
def add(a,b,c):
    return a + b + c

numbers = [1, 2, 3]
# *numbers unpacks to: add(1, 2, 3)
result = add(*numbers)
print(result)  # Output: 6

# Example 2: Unpacking a list with different data types
# This demonstrates unpacking with mixed data types (strings and integers)
def info_user(name, age, city):
    return f"{name} is {age} years old and lives in {city}."

user_info = {"name": "Alice", "age": 30, "city": "London"}
# **user_info unpacks to: info_user(name="Alice", age=30, city="London")
result = info_user(**user_info)
print(result)  # Output: Alice is 30 years old and lives in London.