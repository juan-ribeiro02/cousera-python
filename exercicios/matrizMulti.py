def cria_matriz(num_linha, num_coluna):
    matriz = []

    for i in range(num_linha):
        linha = []
        for j in range(num_coluna):
            valor = int(input(f"Informe o elemento [{i}] [{j}]:"))
            linha.append(valor)
        matriz.append(linha)

    return matriz

def sao_multiplicaveis(m1, m2):
    num_colunas = len(m1[0])
    num_linhas = len(m2)

    if num_linhas == num_colunas:
        return True
    else:
        return False

print(sao_multiplicaveis(cria_matriz(2,2), cria_matriz(3,2)))
