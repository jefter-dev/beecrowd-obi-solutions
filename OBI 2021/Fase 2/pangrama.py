pharse = input()

listPharse = list(pharse)

while("." in listPharse):
    listPharse.remove(".")
while("," in listPharse):
    listPharse.remove(",")
while(" " in listPharse):
    listPharse.remove(" ")
while(":" in listPharse):
    listPharse.remove(":")
while("k" in listPharse):
    listPharse.remove("k")
while("w" in listPharse):
    listPharse.remove("w")
while("y" in listPharse):
    listPharse.remove("y")
    
alphabet = list("abcdefghijlmnopqrstuvxz")

listPharse = list(set(listPharse))
listPharse.sort()

# print(alphabet)
# print(listPharse)

if(listPharse == alphabet):
    print("S")
else:
    print("N")