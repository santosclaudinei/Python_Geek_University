dia = int(input("Escolha um dia da semana: "))

if (dia > 0) and (dia < 8):
    if (dia == 1):
        print('O dia escolhido foi DOMINGO')
    elif (dia == 2):
        print('O dia escolhido foi SEGUNDA')
    elif (dia == 3):
        print('O dia escolhido foi TERÇA')
    elif (dia == 4):
        print('O dia escolhido foi QUARTA')
    elif (dia == 5):
        print('O dia escolhido foi QUINTA')
    elif (dia == 6):
        print('O dia escolhido foi SEXTA')
    else:
        print('O dia escolhido foi SABADO')
else:
    print('Dia invalido.')