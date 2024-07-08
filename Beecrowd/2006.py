
# Identificando o Chá
typeTea = int(input())
a, b, c, d, e = (input()).split()

a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)

cont = 0

if(a == typeTea):
    cont += 1
if(b == typeTea):
    cont += 1
if(c == typeTea):
    cont += 1
if(d == typeTea):
    cont += 1
if(e == typeTea):
    cont += 1
    
print(cont)