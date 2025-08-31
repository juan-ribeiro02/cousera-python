class Carro:
    pass

meu_carro = Carro()

carro_do_ime = Carro()

meu_carro.ano = 1998
meu_carro.modelo = 'ferrari'
meu_carro.cor = 'vermelho'

carro_do_ime.ano = 2000
carro_do_ime.modelo = 'aston martin'
carro_do_ime.cor = 'verde'

carro_do_jao = carro_do_ime

carro_do_jao.ano += 10

print(carro_do_ime.ano)
