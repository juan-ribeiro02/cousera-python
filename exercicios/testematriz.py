import matriz

def soma_matriz(A, B):
    num_linha = len(A)
    num_coluna = len(A[0])
    C = matriz.cria_matriz(num_linha, num_coluna, 0)

    for lin in range(num_linha): #percorre as linhas da matriz
        for col in range(num_coluna): #percorre as colunas da matriz
            C[lin][col] = A[lin][col] + B[lin][col]
    return C

if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[10, 20, 30], [40, 50, 60], [70, 80 ,90]]

    print(soma_matriz(A, B))
