nome = str(input())
salario = float(input())
vendas = float(input())

comissao = vendas * (15/100)
bonus = salario + comissao

print("TOTAL = R$ %.2f" % (bonus))