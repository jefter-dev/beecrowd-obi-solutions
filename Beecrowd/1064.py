# Positivos e Média
number1 = float(input())
number2 = float(input())
number3 = float(input())
number4 = float(input())
number5 = float(input())
number6 = float(input())

sum = 0

cont = 0
if(number1 > 0):
    cont += 1
    sum += number1
if(number2 > 0):
    cont += 1
    sum += number2
if(number3 > 0):
    cont += 1
    sum += number3
if(number4 > 0):
    cont += 1
    sum += number4
if(number5 > 0):
    cont += 1
    sum += number5
if(number6 > 0):
    cont += 1
    sum += number6

average = sum / cont
    
print("{:.0f} valores positivos".format(cont))
print("{:.1f}".format(average))