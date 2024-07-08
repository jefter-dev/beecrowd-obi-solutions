
# Cimba
import math

a, b, c = input().split(" ")

a = int(a)
b = int(b)
c = int(c)

area = (a + b + c) / 2

result = math.sqrt(area * (area - a) * (area - b) * (area - c))

print("{:.3f} m2".format(result))