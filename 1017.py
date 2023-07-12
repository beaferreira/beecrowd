tempo = int(input())
velocidade = int(input())

distancia_percorrida = tempo * velocidade
litros = distancia_percorrida / 12

print("%.3f" % (litros))