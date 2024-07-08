# Distância Entre Dois Pontos
import math

x1, y1 = (input()).split(" ")
x2, y2 = (input()).split(" ")

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

calc = (x2 - x1) ** 2 + (y2 - y1) ** 2

result = math.sqrt(calc)

print("{:.4f}".format(result))