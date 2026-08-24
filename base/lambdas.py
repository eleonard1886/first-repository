"""
* Seccion lambda

"""
# x = lambda x : x +10
# print(x(5))


# j = lambda j : j**2 if j > 2 else 0

# print(j(4))

# def myfunction (n):
#     return lambda a : a * n


# foo = myfunction(2)
# print(foo(4))



# service = [1,2,3,4]

# if (n := len(service))>0:
#     print(n)


# def get_tax(price):
#     price = price * 0.15 
#     return  price# Simulated complex calculation

prices = [10, 55, 100, 20, 150]

# Without Walrus: We would have to call get_tax(p) twice.
# With Walrus: (t := get_tax(p)) saves the result.
# expensive_taxes = [t for p in prices if (t := get_tax(p)) > 10]

# print(expensive_taxes) # Output: [15.0, 22.5]

data = list(map(lambda x : x+1,prices))
print(data)
data1 = list(range(1,20))
even_num = list(filter(lambda x: x%2 == 0,data1))
print(even_num)





