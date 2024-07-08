# Intervalo 2
quantity = int(input())

contIn = 0
contOut = 0
for i in range(quantity):
    number = int(input())
    
    if(number >= 10 and number <= 20):
        contIn += 1
    else:
        contOut += 1
        
print(contIn, "in")
print(contOut, "out")