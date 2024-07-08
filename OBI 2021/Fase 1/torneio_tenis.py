win1 = input()
win2 = input()
win3 = input()
win4 = input()
win5 = input()
win6 = input()

contWin = 0
if(win1 == "V"):
    contWin += 1
if(win2 == "V"):
    contWin += 1
if(win3 == "V"):
    contWin += 1
if(win4 == "V"):
    contWin += 1
if(win5 == "V"):
    contWin += 1
if(win6 == "V"):
    contWin += 1

group = -1
if(contWin >= 1 and contWin <= 2):
    group = 3
elif(contWin >= 3 and contWin <= 4):
    group = 2
elif(contWin >= 5 and contWin <= 6):
    group = 1
    
print(group)