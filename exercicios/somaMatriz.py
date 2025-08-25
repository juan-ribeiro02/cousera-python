def soma_matrizes(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False

    matriz_soma = []
    for i in range(len(m1)):
        linha_soma = []
        for j in range(len(m1[0])):
            linha_soma.append(m1[i][j] + m2[i][j])
        matriz_soma.append(linha_soma)
    return matriz_soma
