from _datetime import date

mes_31 = (1, 3, 5, 7, 8, 10, 12)
mes_30 = (4, 6, 9, 11)
meses = ('0', 'Janeiro', 'Fevereiro', 'Março', 'Abril',
         'Maio', 'Junho', 'Julho', 'Agosto',
         'Setembro', 'Outubro', 'Novembro', 'Dezembro')
ano_atual = date.today().year

dia = int(input('Digite o dia do seu nascimento: '))
mes = int(input('Digite o mês do seu nascimento: '))
ano = int(input('Digite o ano do seu nascimento: '))

while (0 < dia <= 31) and (0 < mes <= 12) and (0 < ano <= ano_atual):
    if mes in mes_31:
        while dia > 31:
            print('O dia informado é inválido')
            dia = int(input('Digite o dia do seu nascimento: '))
    elif mes in mes_30:
        while dia > 30:
            print('O dia informado é inválido')
            dia = int(input('Digite o dia do seu nascimento: '))
    else:
        if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
            while dia > 29:
                print('O dia informado é inválido')
                dia = int(input('Digite o dia do seu nascimento: '))
            while dia > 28:
                print('O dia informado é inválido')
                dia = int(input('Digite o dia do seu nascimento: '))

    print(f'Você nasceu em {dia} de {meses[mes]} de {ano}')
    break
else:
    print(f'A data digitada é inválida.')
