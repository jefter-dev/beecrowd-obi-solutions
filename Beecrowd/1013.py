# O Maior
a, b, c = (input()).split(" ")

a = int(a)
b = int(b)
c = int(c)

bigger = (a+b+abs(a-b)) / 2

if(c > bigger):
    bigger = c

print(int(bigger), "eh o maior")