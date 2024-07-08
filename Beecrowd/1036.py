# Fórmula de Bhaskara
import math

a, b, c = (input()).split()

a = float(a)
b = float(b)
c = float(c)

delta = (b ** 2) - (4 * a * c)

if(delta <= 0 or (2 * a) <= 0):
    print("Impossivel calcular")
else:
    raizDelta = (math.sqrt(delta))
    
    x1 = (-(b) + raizDelta) / (2 * a)
    x2 = (-(b) - raizDelta) / (2 * a)

    print("R1 = {:.5f}".format(x1))
    print("R2 = {:.5f}".format(x2)) 