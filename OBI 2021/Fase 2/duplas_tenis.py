
a = int(input())
b = int(input())
c = int(input())
d = int(input())

listAthletes = [a, b, c, d]
listAthletes.sort()

sumPair1 = listAthletes[0] + listAthletes[3] 
sumPair2 = listAthletes[1] + listAthletes[2]
 
print(abs(sumPair1 - sumPair2))