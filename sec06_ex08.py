cont = 0
maior = 0
menor = 0

while cont < 10:
    numero = int(input(f'Informe o {cont+1}º numero: '))
    if cont == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    cont += 1

print(f'O maior numero foi {maior}')
print(f'O menor numero foi {menor}')
