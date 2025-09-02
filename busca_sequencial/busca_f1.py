class Piloto:
    def __init__(self, nome, vitorias, podios, titulos, ano_de_estreia):
        self.nome = nome
        self.vitorias = vitorias
        self.podios =  podios
        self.titulos = titulos
        self.ano_de_estreia = ano_de_estreia

class Buscador:
    def buscar_por_piloto(self, pilotos, piloto):
        for i in range(len(pilotos)):
            if pilotos[i].nome == piloto:
                return i
        return -1


    def vamos_buscar(self):
        lista_de_pilotos = [Piloto("Max Verstappen", 64, 107, 4, 2015),
                            Piloto("Charles Leclerc", 8, 27, 0, 2018),
                            Piloto("Oscar Piastri", 10, 21, 0, 2023)]
        
        onde_achou = self.buscar_por_piloto(lista_de_pilotos, "Max Verstappen")

        if onde_achou == -1:
            print("Este piloto não está na lista")
        else:
            piloto_achado = lista_de_pilotos[onde_achou]
            print(lista_de_pilotos[onde_achou].nome) #ou print(piloto_achado.nome)


b = Buscador()
b.vamos_buscar()
