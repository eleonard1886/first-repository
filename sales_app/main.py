from ecommerce.inventory import add_product, remove_product
from ecommerce.sales import process_sales

added_product = add_product("Headphones", 150, 30)
inventory = [
    add_product("Laptop", 1000, 10),
    add_product("Smartphone", 500, 20),
    add_product("Tablet", 300, 15),
    added_product
]

removed_product = remove_product(inventory, "Smartphone")   

processed_sales = process_sales([
    {'product': 'Laptop', 'quantity': 2, 'price': 1000},
    {'product': 'Tablet', 'quantity': 1, 'price': 300},
    {'product': 'Headphones', 'quantity': 3, 'price': 150}
])