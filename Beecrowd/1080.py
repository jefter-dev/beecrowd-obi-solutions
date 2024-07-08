# Maior e Posição
listNumbers = []

numberMax = 0
numberPosition = 0

for position in range(100):
    number = int(input())
    
    listNumbers.append(number)
    
for position, number in enumerate(listNumbers):
    if(number >= numberMax):
        numberMax = number
        numberPosition = position + 1

print(numberMax)
print(numberPosition)