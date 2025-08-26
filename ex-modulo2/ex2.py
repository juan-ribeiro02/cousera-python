def menor_nome(nomes):
    if not nomes:
        return None

    return min(nomes, key=str.lower)
