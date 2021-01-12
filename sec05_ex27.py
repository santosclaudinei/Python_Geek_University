idade = int(input('Informe a idade do nadador: '))
if idade > 0:
    if 1 <= idade <= 4:
        print('Ainda não tem idade para prática')
    elif 5 <= idade <= 7:
        print('Infatil A')
    elif 8 <= idade <= 10:
        print('Infatil B')
    elif 11 <= idade <= 13:
        print('Juvenil A')
    elif 14 <= idade <= 17:
        print('Juvenil B')
    else:
        print('Senior')
else:
    print('Idade inválida')