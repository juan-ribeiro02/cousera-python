class Ordenador:
    def direta(self, lista):
        fim = len(lista)

        for i in range(fim -1):
            pos_min = i

            for j in range(i+1, fim):
                if lista[j] < lista[pos_min]:
                    pos_min = j

            lista[i], lista[pos_min] = lista[pos_min], lista[i]

    def bolha(self, lista):
        fim = len(lista)

        for i in range(fim - 1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j +1] = lista[j + 1], lista[j]

    def bolha_curta(self, lista):
        fim = len(lista)

        for i in range(fim - 1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j +1] = lista[j + 1], lista[j]
                    trocou = True
            if not trocou:
                return