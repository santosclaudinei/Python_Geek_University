n = int(input('Informe um numero positivo: '))
if n > 0:
    for i in range(n, 0, -1):
        print(i)
else:
    print('Numero inválido')