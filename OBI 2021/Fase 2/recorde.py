olympicResult = int(input())
worldRecord = int(input())
olympicRecord = int(input())

if(worldRecord > olympicResult):
    print("RM")
else:
    print("*")
    
if(olympicRecord > olympicResult):
    print("RO")
else:
    print("*")