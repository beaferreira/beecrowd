cod1, num1, valor1 = input().split()
cod2, num2, valor2 = input().split()

num1 = float(num1)
num2 = float(num2)
valor1 = float(valor1)
valor2 = float(valor2)

calculo = (num1 * valor1) + (num2 * valor2)

print("VALOR A PAGAR: R$ %.2f" % (calculo))