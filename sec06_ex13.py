n = int(input('Informe um numero positivo: '))
if n > 0 and n % 2 == 0:
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i)
else:
    print('Numero inválido')