# Cédulas
value = int(input())

print(value)

calc = value // 100
value = value - (calc * 100)

print(calc, "nota(s) de R$ 100,00")

calc = value // 50
value = value - (calc * 50)

print(calc, "nota(s) de R$ 50,00")

calc = value // 20
value = value - (calc * 20)

print(calc, "nota(s) de R$ 20,00")

calc = value // 10
value = value - (calc * 10)

print(calc, "nota(s) de R$ 10,00")

calc = value // 5
value = value - (calc * 5)

print(calc, "nota(s) de R$ 5,00")

calc = value // 2
value = value - (calc * 2)

print(calc, "nota(s) de R$ 2,00")

calc = value // 1
value = value - (calc * 1)

print(calc, "nota(s) de R$ 1,00")