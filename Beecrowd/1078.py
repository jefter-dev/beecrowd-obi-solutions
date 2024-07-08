# Tabuada
number = int(input())

for i in range(1, 10 + 1):
    calc = number * i 
    print("{:.0f} x {:.0f} = {:.0f}".format(i, number, calc))