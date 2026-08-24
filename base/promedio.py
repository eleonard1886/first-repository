def calcular_promedio(lista: list[float]) -> float:
    """Calcula el promedio de una lista de números.

    Returns:
        float: El promedio de los números en la lista.
    """
    if not lista:
        return 0
    return sum(lista) / len(lista)