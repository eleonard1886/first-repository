def mi_decorator(func):
    def wrapper(*args, **kwargs):
        print("Antes de llamar a la función")
        resultado = func(*args, **kwargs)
        print("Después de llamar a la función")
        return resultado
    return wrapper



@mi_decorator
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Juan")

