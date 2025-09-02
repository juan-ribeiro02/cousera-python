class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):
        if self.a == self.b == self.c:
            return "equilátero"
        elif self.a != self.b and self.a != self.c and self.b != self.c:
            return "escaleno"
        else:
            return "isósceles"

    

# t = Triangulo(4, 4, 4)
# print(t.tipo_lado())

# t2 = Triangulo(3, 4, 5)
# print(t2.tipo_lado())

# t3 = Triangulo(3, 2, 2)
# print(t3.tipo_lado())
