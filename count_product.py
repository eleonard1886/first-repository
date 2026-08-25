from collections import defaultdict

def count_product(orders: list[str]) -> defaultdict:
    #crea un diccionario con valor por defecto de tipo int
    product_count = defaultdict(int)
    
    for product in orders:
        product_count[product] += 1            
    return product_count

orders = ['laptop', 'keyboard', 'laptop', 'mouse','smartphone', 'keyboard', 'laptop', 'mouse', 'smartphone', 'tablet']
count = count_product(orders)

print(count)


