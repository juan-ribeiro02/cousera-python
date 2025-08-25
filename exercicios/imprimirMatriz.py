def imprime_matriz(matriz):
    for linha in matriz:
        print(" ".join(map(str, linha)))

matriz = [[2, 2],[2, 2]]

imprime_matriz(matriz)
