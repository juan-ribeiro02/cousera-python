class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

carro_do_meu_avo = Carro("Fusca", 1935, "vermelho")

print(carro_do_meu_avo.cor)
