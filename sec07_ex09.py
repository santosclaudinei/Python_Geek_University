pares = []
cont = 0

while cont <= 5:
    num = int(input(f'Informe o {cont+1}º numero: '))
    if num % 2 == 0:
        pares.append(num)
        cont += 1

print(pares[::-1])

