# Pares entre Cinco Números
number1 = float(input())
number2 = float(input())
number3 = float(input())
number4 = float(input())
number5 = float(input())

cont = 0
if(number1 % 2) == 0:
    cont += 1
if(number2 % 2) == 0:
    cont += 1
if(number3 % 2) == 0:
    cont += 1
if(number4 % 2) == 0:
    cont += 1
if(number5 % 2) == 0:
    cont += 1

print("{:.0f} valores pares".format(cont))