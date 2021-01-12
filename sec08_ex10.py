def mostraMaior(num1, num2):
    maior = 0
    if num1 > num2 and num1 > maior:
        maior = num1
    else:
        maior = num2
    return maior


num1 = int(input('Informe um numero: '))
num2 = int(input('Informe outro numero: '))
maior = mostraMaior(num1, num2)
print(f'O maior numero entre {num1} e {num2} é {maior}')
