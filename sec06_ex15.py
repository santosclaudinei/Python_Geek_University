n = int(input('Informe um numero positivo: '))
if n > 0 and n % 2 == 1:
    for i in range(1, n+1):
        if i % 2 == 1:
            print(i)
else:
    print('Numero inválido')