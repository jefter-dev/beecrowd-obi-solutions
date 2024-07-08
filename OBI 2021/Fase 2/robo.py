numeroEstacoes, numeroComandos, estacaoDevastada = input().split()
commands = input().split()

numeroEstacoes = int(numeroEstacoes)
numeroComandos  = int(numeroComandos)
estacaoDevastada = int(estacaoDevastada)

estacao = 1
contTotal = 0

if(estacaoDevastada == 1):
    contTotal += 1

for i in range(numeroComandos):        
    if(estacao == estacaoDevastada):
        contTotal += 1
        
    if(estacao < 1):
        estacao = numeroComandos
    elif(estacao > numeroComandos):
        estacao = 1
        
    estacao += int(commands[i])
    print("estacao:", estacao) 
      
print(contTotal)