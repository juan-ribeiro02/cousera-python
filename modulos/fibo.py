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

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
