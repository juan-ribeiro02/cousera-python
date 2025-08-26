def menor_nome(nomes):
    if not nomes:
        return None
    
    menor = min(nomes, key=lambda x: len(x.strip()))
    
    return menor.strip().capitalize()

lista = ['maria', 'josé', 'PAULO', 'Catarina']

resul = menor_nome(lista)

print(resul)
