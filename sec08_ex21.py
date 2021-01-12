def maiorFatorial(numero):

    primos = []

    for i in range(1, numero):
        cont = 0
        for j in range(1, numero):
            if (i % j == 0):
                cont += 1
                num = i
        if cont == 2:
            primos.append(num)
        else:
            continue
    return primos


numero = int(input('informe um numero: '))
primos  = maiorFatorial(numero)
print(f'Os numeros primos entre 1 e {numero} é {primos}')