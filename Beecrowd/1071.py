# Soma de Impares Consecutivos I
def getOdds(listNumbers):
    listOdds = []
    for i in range(len(listNumbers)):
        number = listNumbers[i]
        
        if(number % 2 != 0):
            listOdds.append(number)
    return listOdds

number1 = int(input())
number2 = int(input())

number1Fixed = number1
number2Fixed = number2
if(number1 > number2):
    number2 = number1Fixed
    number1 = number2Fixed
    
# print("NUMBER 1", number1)
# print("NUMBER 2", number2)

listNumbers = []
for i in range(number1 + 1, number2):
    listNumbers.append(i)

# print("LIST NUMBERS: ", listNumbers)

listOdds = getOdds(listNumbers)
# print(listOdds)

sum = 0
for number in listOdds:
    sum += number

print(sum)