def fatorial(num):
    cont, fatorial = 1, 1
    n = num

    while cont != num:
        if n > 1:
            fatorial = fatorial * (n * (n - 1))
            cont += 1
            n = n - 2
        else:
            break
    return fatorial


num = int(input('Informe o numero que deseja saber o seu fatorial: '))
resultado = fatorial(num)
print(f'O fatorial de {num} é {resultado}')