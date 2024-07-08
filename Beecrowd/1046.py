# Tempo de Jogo
start, end = (input()).split(" ")

start = int(start)
end = int(end)

# end = 24 if end == 0 else end

if(end > start):
    duration = end - start
elif(start == end):
    duration = 24
else:
    duration = (24 - start) + end
        
print("O JOGO DUROU {:.0f} HORA(S)".format(abs(duration)))