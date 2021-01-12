cont = 0
soma = 0
while cont < 10:
    numero = int(input(f'Informe o {cont+1}º numero: '))
    soma += numero
    cont += 1

print(f'A soma dos valores é: {soma}' )