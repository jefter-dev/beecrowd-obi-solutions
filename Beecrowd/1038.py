# 	Lanche
import math

products = {
    1: 4,
    2: 4.5,
    3: 5,
    4: 2,
    5: 1.5
} 

code, quantity = (input()).split(" ")

code = int(code)
quantity = int(quantity)

result = quantity * (products[code])

print("Total: R$ {:.2f}".format(result))