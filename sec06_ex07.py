cont = 0
soma = 0
media = 0

while True:
    if cont < 10:
        numero = int(input(f'Informe o {cont+1} numero: '))
        if numero > 0:
            soma += numero
            cont += 1
        else:
            print("Este numero não será computado.")
    else:
        break
media = soma/cont
print(f'A soma de todos os numeros é {soma}')
print(f'A media entre todos os numeros digitados é {media}')