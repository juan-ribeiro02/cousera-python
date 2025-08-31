def mat_mul(A, B):
    num_linha_A, num_coluna_A = len(A), len(A[0])
    num_linha_B, num_coluna_B = len(B), len(B[0])
    assert num_coluna_A == num_linha_B

    C = []

    for linha in range(num_linha_A):
        C.append([])
        for coluna in range(num_coluna_B):
            C[linha].append(0)
            for k in range(num_coluna_A):
                C[linha][coluna] += A[linha][k] * B[k][coluna]
    return C

if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[1, 2], [3, 4], [5, 6]]

    print(mat_mul(A, B))
