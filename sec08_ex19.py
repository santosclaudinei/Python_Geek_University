def maiorFatorial(numero):

    primos = []
    menorfat = []
    menorfator = 1


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

    for numeros in primos:
        if numero == 1:
            break
        else:
            while numero % numeros == 0:
                numero = numero / numeros
                menorfator *= numeros
                menorfat.append(numeros)
    return menorfator, menorfat

numero = int(input('informe um numero: '))
menorfator, menorfat  = maiorFatorial(numero)
print(f'O maior fator comum de {menorfator} é {menorfat}')