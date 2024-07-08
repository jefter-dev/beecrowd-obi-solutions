# Aviões de Papel
numberCompetitors, numbersheets, numbersheetsReceive = input().split()

numberCompetitors = int(numberCompetitors)
numbersheets = int(numbersheets)
numbersheetsReceive = int(numbersheetsReceive)

calc = numberCompetitors * numbersheetsReceive

if(calc <= numbersheets):
    print("S")
else:
    print("N")
    
