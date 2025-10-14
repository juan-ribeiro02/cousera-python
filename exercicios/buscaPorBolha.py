def bubble_sort(lista):
    fim = len(lista)

    for i in range(fim):
        for j in range(0, fim - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print(lista)
    return lista