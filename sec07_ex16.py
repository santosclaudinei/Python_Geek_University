numeros = [5.0, 7.0, 6.0, 10.0, 8.0]

codigo = int(input('informe o codigo para prosseguir: '))

if codigo == 1:
    print('Os numeros da lista em ordem são: ')
    for numero in numeros:
        print(f'{numero}', end=' ')

elif codigo == 2:
    print('Os numeros da lista na ordem inversa são: ')

    print(numeros[::-1])