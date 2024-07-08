quantityNumbers = int(input())

result = 0
for i in range(quantityNumbers):
    number = input()
    potency = number[-1]
    number = number[:-1]
    
    result += int(number) ** int(potency)

print(result)