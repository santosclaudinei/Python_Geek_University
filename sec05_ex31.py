altura = float(input('Informe a sua altura: '))
peso = float(input('Informe o seu peso: '))

if (altura > 0) and (peso > 0):
    if (altura < 1.20):
        if (0 < peso <= 60):
            print('Sua classificação é "A"')
        elif (60 < peso <= 90):
            print('Sua classificação é "D"')
        else:
            print('Sua classificação é "G"')
    elif (1.20 <= altura <= 1.70):
        if (0 < peso <= 60):
            print('Sua classificação é "B"')
        elif (60 < peso <= 90):
            print('Sua classificação é "E"')
        else:
            print('Sua classificação é "H"')
    else:
        if (0 < peso <= 60):
            print('Sua classificação é "C"')
        elif (60 < peso <= 90):
            print('Sua classificação é "F"')
        else:
            print('Sua classificação é "I"')
else:
    print('Altura ou Peso Invalido(s)')