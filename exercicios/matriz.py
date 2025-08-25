def cria_matriz(num_linhas, num_colunas):
    matriz = []

    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input(f"Informe o elemento [{i}] [{j}]:"))
            linha.append(valor)

        matriz.append(linha)

    return matriz

def le_matriz():
    lin = int(input("Informe o número de linhas:"))
    col = int(input("Informe o número de colunas"))
    return cria_matriz(lin, col)

matriz = cria_matriz(2,2)

for i in range(len(matriz)):
    print("aaaaaaa")
