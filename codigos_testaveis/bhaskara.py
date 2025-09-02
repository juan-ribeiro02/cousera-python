import math

class Bhaskara:
    def delta(self, a, b, c):
        return b**2 - 4 * a * c
    
    def main(self):
        a = float(input("Informe o valor de a:"))
        b = float(input("Informe o valor de b:"))
        c = float(input("Informe o valor de c:"))
        print(self.calcula_raizes(a, b, c))

    def calcula_raizes(self, a, b, c):
        d = self.delta(a, b, c)
        if d == 0:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            return 1, raiz1
        elif d < 0:
            return 0
        else:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            raiz2 = (-b - math.sqrt(d)) / (2 * a)
            return 2, raiz1, raiz2
        
@pytest.mark.parametrize("entrada", "esperado", [
    (10, 10, 10, 0)
    ])

def teste_bhaskara(entrada, esperado):
    assert Bhaskara.main() == 