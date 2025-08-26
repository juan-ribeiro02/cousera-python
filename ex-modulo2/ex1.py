def maiusculas(frase):
    teste = []
    i = 0

    while i < len(frase):
        if frase[i].isupper():
            teste.append(frase[i])
        i += 1

    return ''.join(teste)
