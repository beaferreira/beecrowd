N = int(input())

cedulas = [100, 50, 20, 10, 5, 2, 1]

print((N))

for cedula in cedulas:
    quantidade = N // cedula
    N %= cedula
    print("%d nota(s) de R$ %d,00" % (quantidade, cedula))
    


