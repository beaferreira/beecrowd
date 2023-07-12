N = int(input())

horas = N // 3600
minutos = (N % 3600) // 60
segundos = N % 60 

tempo_formatado = "{:01d}:{:01d}:{:01d}".format(horas, minutos, segundos)
print(tempo_formatado)