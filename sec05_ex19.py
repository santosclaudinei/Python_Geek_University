numero = int(input("Informe um numero: "))

if (numero % 3 == 0) and (not (numero % 5 == 0)):
    print('Divisivel apenas por 3.')
elif(numero % 5 == 0) and (not (numero % 3 == 0)):
    print('Divisivel apenas por 5.')
elif(numero % 5 == 0) and (numero % 3 == 0):
    print('É Divisivel por 3 e por 5.')