import time
import ordenador
import random

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista
    
    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista
    
    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]
        lista3 = lista1[:]

        o = ordenador.Ordenador()

        print("Comparando com lista aleatórias")
        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("Algoritmo bolha =", depois - antes)

        antes = time.time()
        o.bolha_curta(lista3)
        depois = time.time()
        print("Algoritmo bolha curta =", depois - antes)

        antes = time.time()
        o.direta(lista2)
        depois = time.time()
        print("Algoritmo direta =", depois - antes)

        print("Comparando com lista quase ordenada")

        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]
        lista3 = lista1[:]
               
        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("Algoritmo bolha =", depois - antes)

        antes = time.time()
        o.bolha_curta(lista3)
        depois = time.time()
        print("Algoritmo bolha curta =", depois - antes)

        antes = time.time()
        o.direta(lista2)
        depois = time.time()
        print("Algoritmo direta =", depois - antes)

if __name__ == "__main__":
    m = ContaTempos()
    m.compara(1000)
