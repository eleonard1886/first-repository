import multiprocessing


def calcular_cuadrado(numero) -> int:
    return numero * numero

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5]
    with multiprocessing.Pool() as pool:
        resultados = pool.map(calcular_cuadrado, numeros)
    print(resultados)