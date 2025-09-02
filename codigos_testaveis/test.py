import bhaskara
import pytest

@pytest.mark.parametrize("entrada", "esperado", [
    (10, 10, 10, 0)
    ])

def teste_bhaskara(entrada, esperado):
    assert 