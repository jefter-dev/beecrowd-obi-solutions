number1 = (input())
number2 = (input())

quantityNumbers1 = len(number1)
quantityNumbers2 = len(number2)

if(quantityNumbers1 > quantityNumbers2):
    quantityNumbers = quantityNumbers1
else:
    quantityNumbers = quantityNumbers2
        
number1 = str(number1).zfill(quantityNumbers)
number2 = str(number2).zfill(quantityNumbers)

listNumbers1 = list(number1)
listNumbers2 = list(number2)

result1 = ""
result2 = ""
for i in range(len(listNumbers1)):
    numberList1 = listNumbers1[i]
    numberList2 = listNumbers2[i]
    
    if(numberList1 >= numberList2):
        result1 += numberList1
    if(numberList2 >= numberList1):
        result2 += numberList2

    # print(numberList1, " > ", numberList2)

if(result1 == ""):
    result1 = -1
if(result2 == ""):
    result2 = -1
    
result1 = int(result1)
result2 = int(result2)
    
if(result1 < result2):
    print("{} {}".format(result1, result2))
else:
    print("{} {}".format(result2, result1))