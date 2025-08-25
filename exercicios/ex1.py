def cria_matriz(num_linha, num_coluna):
    matriz = []

    for i in range(num_linha):
        linha = []
        for j in range(num_coluna):
            valor = int(input(f"Informe o elemento [{i}] [{j}]:"))
            linha.append(valor)
        matriz.append(linha)

    return matriz

def mostra_funcao(matriz):
    for linha in matriz:
        for elemento in linha:
            print(elemento, end=" ")
        print()

def dimensoes(matriz):
    num_linha = len(matriz)
    num_coluna = len(matriz[0])

    print(f"{num_linha}X{num_coluna}")

dimensoes(cria_matriz(2, 3))
