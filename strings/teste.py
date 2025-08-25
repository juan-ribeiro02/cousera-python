#pega o menor na ordem sla oq

def menor_string(meu_string):
    if not meu_string:
        return None

    return min(meu_string, key=str.lower)

lista = ['ana', 'Juan', 'carlos']

resul = menor_string(lista)

print(resul)