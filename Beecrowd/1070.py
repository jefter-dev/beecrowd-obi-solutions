# Seis Números Ímpares
def getOdds(listNumbers):
    listOdds = []
    for i in range(len(listNumbers)):
        number = listNumbers[i]
        
        if(number % 2 != 0):
            listOdds.append(number)
    return listOdds

number = int(input())

listNumbers = []
i = number
for i in range(number, number + 12):
    listNumbers.append(i)

listOdds = getOdds(listNumbers)

for number in listOdds:
    print(number)