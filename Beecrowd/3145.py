# Uma Jornada Inesperada
number1, number2 = (input()).split(" ")

dwarves = float(number1)
distancy = float(number2)

people = dwarves + 2

result = distancy / people

print("{:.2f}".format(result))