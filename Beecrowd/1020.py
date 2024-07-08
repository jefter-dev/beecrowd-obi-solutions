# Idade em Dias
days = (int(input()))

years = days // 365
days = days - (years * 365)

months = days // 30
days = days - (months * 30)

print(years, "ano(s)")
print(months, "mes(es)")
print(days, "dia(s)")