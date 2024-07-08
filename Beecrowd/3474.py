# Boa divisão
value, quantity = (input()).split(" ")

value = float(value)
quantity = int(quantity)

result = value / quantity

print("{:.2f}".format(result))