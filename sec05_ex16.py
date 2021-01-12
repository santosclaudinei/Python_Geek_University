mes = int(input("Escolha um mês do ano: "))

if (mes > 0) and (mes < 13):
    if (mes == 1):
        print('O mês escolhido foi JANEIRO')
    elif (mes == 2):
        print('O mês escolhido foi FEVEREIRO')
    elif (mes == 3):
        print('O mês escolhido foi MARÇO')
    elif (mes == 4):
        print('O mês escolhido foi ABRIL')
    elif (mes == 5):
        print('O mês escolhido foi MAIO')
    elif (mes == 6):
        print('O mês escolhido foi JUNHO')
    elif (mes == 7):
        print('O mês escolhido foi JULHO')
    elif (mes == 8):
        print('O mês escolhido foi AGOSTO')
    elif (mes == 9):
        print('O mês escolhido foi SETEMBRO')
    elif (mes == 10):
        print('O mês escolhido foi OUTUBRO')
    elif (mes == 11):
        print('O mês escolhido foi NOVEMBRO')
    else:
        print('O mês escolhido foi DEZEMBRO')
else:
    print('Dia invalido.')