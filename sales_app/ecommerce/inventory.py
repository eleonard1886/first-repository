def add_product(name, price, quantity):
    return {
        'name': name,
        'price': price,
        'quantity': quantity
    }


def remove_product(inventory, product_name):
    return [product for product in inventory if product['name'] != product_name]



products = [
    add_product("Laptop", 1000, 10),
    add_product("Smartphone", 500, 20),
    add_product("Tablet", 300, 15)
]

removed_product = remove_product(products, "Smartphone")

print(removed_product)

new = add_product("Headphones", 100, 30)

products.append(new)

print(products)
