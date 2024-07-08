monthlyQuota = int(input())
quantityMonths = int(input())

quantityQuota = monthlyQuota * (quantityMonths + 1)   
quantityUseMonth = 0
for i in range(quantityMonths):
    usedQuote = int(input())
    
    quantityUseMonth += usedQuote
    
print(quantityQuota - quantityUseMonth)