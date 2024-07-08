# Números Positivos
number1 = float(input())
number2 = float(input())
number3 = float(input())
number4 = float(input())
number5 = float(input())
number6 = float(input())

cont = 0
if(number1 > 0):
    cont += 1
if(number2 > 0):
    cont += 1
if(number3 > 0):
    cont += 1
if(number4 > 0):
    cont += 1
if(number5 > 0):
    cont += 1
if(number6 > 0):
    cont += 1
    
print("{:.0f} valores positivos".format(cont))