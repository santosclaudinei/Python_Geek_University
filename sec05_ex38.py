dia = int(input('Informe o dia do seu nascimento: '))
mes = int(input('Informe o mês do seu nascimento: '))
ano = int(input('Informe o ano do seu nascimento: '))
dias_tipo1 = 31
dias_tipo0 = 30
ano_atual = 2008

if (ano % 4) == 0 and (ano % 100 != 0) or (ano % 400 == 0):
    dias_tipo2 = 29
else:
    dias_tipo2 = 28

if (0 <= ano <= ano_atual) and (0 < mes < 13):
        if (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
            if dia != dias_tipo1:
                print('Dia inválida.')
            else:
                print('data valida.')
        elif (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
            if dia != dias_tipo0:
                print('Dia inválida.')
            else:
                print('data valida.')
        elif (mes == 2):
            if (dia != dias_tipo2):
                print('Dia inválida.')
            else:
                print('data valida.')
