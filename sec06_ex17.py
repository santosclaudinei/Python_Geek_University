total = 0
n = int(input('Informe um numero positivo: '))
if n > 0:
    for i in range(1, n+1):
        # if i % 2 == 0:
        total += i
    print(f'A soma de todos os numeros é {total}')
else:
    print('Numero inválido')