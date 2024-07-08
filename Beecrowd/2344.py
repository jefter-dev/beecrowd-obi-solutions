# Notas da Prova
note = int(input())

if(note == 0):
    concept = "E"
elif(note >= 1 and note <= 35):
    concept = "D"
elif(note >= 36 and note <= 60):
    concept = "C"
elif(note >= 61 and note <= 85):
    concept = "B"  
elif(note >= 86 and note <= 100):
    concept = "A"
        
print(concept)