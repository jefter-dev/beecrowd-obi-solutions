# Salário com Bônus
name = input()
salary = float(input())
salesAmount = float(input())

result = (15 * (salesAmount / 100)) + salary

print("TOTAL = R$ {0:.2f}".format(result))
