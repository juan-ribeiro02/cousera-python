def cria_matriz(num_linhas, num_colunas, valor):
    matriz = []

    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(valor)

        matriz.append(linha)

    return matriz

def le_matriz():
    lin = int(input("Informe o número de linhas:"))
    col = int(input("Informe o número de colunas"))
    return cria_matriz(lin, col)
