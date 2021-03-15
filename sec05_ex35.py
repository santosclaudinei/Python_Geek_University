data = input('Informe a data no formato [DD/MM/AAAA] para verificar se ela é valida: ')
data_form = data.split('/')
dia = int(data_form[0])
mes = int(data_form[1])
ano = int(data_form[2])
dias_tipo1 = 31
dias_tipo0 = 30

if (ano % 4) == 0 and (ano % 100 != 0) or (ano % 400 == 0):
    dias_tipo2 = 29
else:
    dias_tipo2 = 28

if (ano >= 0) and (1 <= mes <= 12):
        if (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
            if dia != dias_tipo1:
                print('Dia inválido para esse mês.')
            else:
                print(f'{dia}/{mes}/{ano}')
        elif (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
            if dia != dias_tipo0:
                print('Dia inválido para esse mês.')
            else:
                print(f'{dia}/{mes}/{ano}')
        elif (mes == 2):
            if (dia != dias_tipo2):
                print('Dia inválido para esse mês.')
            else:
                print(f'{dia}/{mes}/{ano}')
