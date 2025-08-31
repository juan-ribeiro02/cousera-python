def main():
    carro1 = Carro("Ferrari", 1988, "vermelha", 200)
    carro2 = Carro("Ford", 1956, "Branco", 190)

    carro1.acelere(50)
    carro2.acelere(55)
    carro1.acelere(190)
    carro2.acelere(187)
    carro1.pare()
    carro2.pare()

class Carro:
    def __init__(self, modelo, ano, cor, velocidade_maxima):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
        self.velocidade_maxima = velocidade_maxima

    def imprima(self):
        if self.velocidade == 0:
            print(f"Seu carro de modelo {self.modelo}, ano de {self.ano}, e cor {self.cor} está parado")
        elif self.velocidade < self.velocidade_maxima:
            print(f"A {self.modelo} está indo a {self.velocidade} KM/H")
        else:
            print(f"A {self.modelo} está indo a {self.velocidade} KM/H, isso é rápido demais")

    def acelere(self, velocidade):
        self.velocidade = velocidade
        if self.velocidade > self.velocidade_maxima:
            self.velocidade = self.velocidade_maxima
        self.imprima()

    def pare(self):
        self.velocidade = 0
        self.imprima()

main()
