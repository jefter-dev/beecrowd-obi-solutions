# Cálculo Simples
import math

code, quantity, value = (input()).split(" ")
code2, quantity2, value2 = (input()).split(" ")

quantity = int(quantity)
value = float(value)

quantity2 = int(quantity2)
value2 = float(value2)

result1 = quantity * value
result2= quantity2 * value2

result = (result1 + result2)

print("VALOR A PAGAR: R$ {:.2f}".format(result))