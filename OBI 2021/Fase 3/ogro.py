number = int(input())

handLeft = ""
handRight = ""
if(number <= 5):
    for i in range(number):
        handLeft += "I"
    handRight += "*"
else:
    handLeft += "IIIII"
    for i in range(number - 5):
        handRight += "I"
        
if(handLeft == ""):
    handLeft = "*"

print(handLeft)
print(handRight)