# Sort Simples
number1, number2, number3 = (input()).split(" ")

number1 = int(number1)
number2 = int(number2)
number3 = int(number3)

if(number1 >= number2 and number1 >= number3):
    primary = number1
    if(number2 >= number3):
        secondary = number2
        third = number3
    else:
        secondary = number3
        third = number2
elif(number2 >= number1 and number2 >= number3):
    primary = number2
    if(number1 >= number3):
        secondary = number1
        third = number3
    else:
        secondary = number3
        third = number1
elif(number3 >= number1 and number3 >= number2):
    primary = number3
    if(number1 >= number2):
        secondary = number1
        third = number2
    else:
        secondary = number2
        third = number1
        
print(third)
print(secondary)
print(primary)
print("")
print(number1)
print(number2)
print(number3)
    
    
