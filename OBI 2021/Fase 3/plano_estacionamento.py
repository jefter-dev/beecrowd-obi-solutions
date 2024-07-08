#!/usr/bin/env python3

# OBI2021 - Fase 3
# Plano de ação
num_vagas = int(input())
num_carros = int(input())

vagas = [0 for i in range(num_vagas+1)]
total = 0

i = 0
ok = True
while i < num_carros and ok:
    plano = int(input())
    while plano > 0 and vagas[plano] > 0:
        t = vagas[plano]
        vagas[plano] = vagas[plano] + 1
        plano = plano - t
    if plano <= 0:
        ok = False
    else:
        vagas[plano] = 1
        total = total + 1
    i = i + 1

print(total)