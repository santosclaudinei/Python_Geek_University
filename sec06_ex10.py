cont = 1
soma = 0
while cont < 51:
    if cont % 2 == 0:
        soma += cont
    cont += 1

print(f'A soma de todos os pares é {soma}')