# Área
a, b, c = (input()).split(" ")

a = float(a)
b = float(b)
c = float(c)

pi = 3.14159

triangle = (a * c) / 2
circle = pi * (c ** 2)
trapeze = ((a + b) * c) / 2
square = b * b
rectangle = a * b

print("TRIANGULO: {:.3f}".format(triangle))
print("CIRCULO: {:.3f}".format(circle))
print("TRAPEZIO: {:.3f}".format(trapeze))
print("QUADRADO: {:.3f}".format(square))
print("RETANGULO: {:.3f}".format(rectangle))