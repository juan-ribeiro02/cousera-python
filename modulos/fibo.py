def fib(n):
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a + b
        i += 1

    return a

def seq_fib(n):
    resul = []
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a + b
        i += 1
        resul.append(a)
    return resul

import pytest

@pytest.mark.parametrize("entrada", "esperado", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5)
    ])

def teste_fib(entrada, esperado):
    assert fib(entrada) == esperado