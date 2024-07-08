# Experiências
quantity = int(input())

contRabbits = 0
contMouses = 0
contFrogs = 0
totalGuineaPigs = 0
for i in range(quantity):
    number, type = input().split()
    number = int(number)
    
    if(type == "C"):
        contRabbits += number
    elif(type == "R"):
        contMouses += number
    elif(type == "S"):
        contFrogs += number
    
    totalGuineaPigs += number
    
percentRabbits = (contRabbits / totalGuineaPigs) * 100
percentMouses = (contMouses / totalGuineaPigs) * 100
percentFrogs = (contFrogs / totalGuineaPigs) * 100
        
print("Total: {} cobaias".format(totalGuineaPigs))
print("Total de coelhos: {}".format(contRabbits))
print("Total de ratos: {}".format(contMouses))
print("Total de sapos: {}".format(contFrogs))
print("Percentual de coelhos: {:.2f} %".format(percentRabbits))
print("Percentual de ratos: {:.2f} %".format(percentMouses))
print("Percentual de sapos: {:.2f} %".format(percentFrogs))