# Pares, Ímpares, Positivos e Negativos
def getPairs(listNumbers):
    cont = 0
    for i in range(len(listNumbers)):
        number = listNumbers[i]
        
        if(number % 2 == 0):
            cont += 1
    return cont

def getOdds(listNumbers):
    cont = 0
    for i in range(len(listNumbers)):
        number = listNumbers[i]
        
        if(number % 2 != 0):
            cont += 1
    return cont

def getPositives(listNumbers):
    cont = 0
    for i in range(len(listNumbers)):
        number = listNumbers[i]
        
        if(number > 0):
            cont += 1
    return cont

def getNegatives(listNumbers):
    cont = 0
    for i in range(len(listNumbers)):
        number = listNumbers[i]
        
        if(number < 0):
            cont += 1
    return cont

number1 = float(input())
number2 = float(input())
number3 = float(input())
number4 = float(input())
number5 = float(input())

listNumbers = [number1, number2, number3, number4, number5]

countPairs = getPairs(listNumbers)
countOdds = getOdds(listNumbers)
countPositives = getPositives(listNumbers)
countNegatives = getNegatives(listNumbers)

print("{:.0f} valor(es) par(es)".format(countPairs))
print("{:.0f} valor(es) impar(es)".format(countOdds))
print("{:.0f} valor(es) positivo(s)".format(countPositives))
print("{:.0f} valor(es) negativo(s)".format(countNegatives))