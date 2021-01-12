maior, menor, meio = 0, 0, 0

numA = int(input('Informe um valor para numA: '))
numB = int(input('Informe um valor para numB: '))
numC = int(input('Informe um valor para numC: '))

if numA > numB and numA > numC:
    if numB > numC:
        maior = numA
        meio = numB
        menor = numC
    else:
        maior = numA
        meio = numC
        menor = numB
    print(f'O maior é {maior}, o do meio é {meio} e o menor é {menor}')
elif numB > numA and numB > numC:
    if numA > numC:
        maior = numB
        meio = numA
        menor = numC
    else:
        maior = numB
        meio = numC
        menor = numA
    print(f'O maior é {maior}, o do meio é {meio} e o menor é {menor}')
elif numC > numA and numC > numB:
    if numA > numB:
        maior = numC
        meio = numA
        menor = numB
    else:
        maior = numC
        meio = numB
        menor = numA
    print(f'O maior é {maior}, o do meio é {meio} e o menor é {menor}')
