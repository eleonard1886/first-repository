def ventas(*args, **kwargs):
    total = 0
    for arg in args:
        total += arg
    for key, value in kwargs.items():
        if key == 'descuento':
            total = total * (1 - value / 100)
        if key == 'impuesto':
            total += total * (value / 100)
    return round(total)

ventas_result = ventas(100, 200, 300, descuento=30, impuesto=5)
print(ventas_result)  # Output: 585.0