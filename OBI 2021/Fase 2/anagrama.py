quantityLetters = int(input())
pharse1 = input()
pharse2 = input()

contLettersEqualsPharse1 = 0
contLettersEqualsPharse2 = 0

l1 = list(pharse1)
l2 = list(pharse2)
l1.sort()
l2.sort()

while(" " in l1):
    l1.remove(" ")
while("," in l1):
    l1.remove(",")
while("." in l1):
    l1.remove(".")

while(" " in l2):
    l2.remove(" ")
while("," in l2):
    l2.remove(",")
while("." in l2):
    l2.remove(".")

# print(l1)
# print(l2)

if(l1 == l2):
    print("S")
else:
    print("N")