# Média 3
note1, note2, note3, note4 = (input()).split(" ")

note1 = float(note1)
note2 = float(note2)
note3 = float(note3)
note4 = float(note4)

average = ((note1 * 2) + (note2 * 3) + (note3 * 4) + (note4 * 1)) / (2 + 3 + 4 + 1)
average = float(average)

print("Media: {:.1f}".format(average))
if(average > 7):
    print("Aluno aprovado.")
elif(average < 5):
    print("Aluno reprovado.")
elif(average >= 5 and average <= 6.9):
    noteExame = float(input())
    finalAvarage = (noteExame + average) / 2
    
    print("Aluno em exame.")
    print("Nota do exame:", noteExame)
    print("Aluno aprovado.")
    print("Media final:", finalAvarage)
else:
    print("Aluno reprovado.")