quantity = int(input())

listBestState = []
for i in range(quantity):
    state, alcohol, gasoline = input().split()
    
    alcohol = float(alcohol) 
    gasoline = float(gasoline)
    
    if(alcohol <= 0.7 * gasoline):
        listBestState.append(state)
        
if(len(listBestState) == 0):
    print("*")
else:
    for i in range(len(listBestState)):
        print(listBestState[i])