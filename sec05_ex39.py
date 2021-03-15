limiar_salario = (500, 1000, 1500, 2000, 2001)
limiar_reajuste = (25, 20, 15, 10, 0)
limiar_bonus = (0, 100, 200, 300, 500)
limiar_tempo = (1, 3, 6, 11)

salario = float(input('Informe o seu salário atual: '))
tempo_servico = float(input('Informe o seu tempo de serviço: '))

if salario > 0 and tempo_servico > 0:
    if salario <= limiar_salario[0]:
        if tempo_servico < limiar_tempo[0]:
            bonus = limiar_bonus[0]
            reajuste = limiar_reajuste[0]
        elif limiar_tempo[0] < tempo_servico <= limiar_tempo[1]:
            bonus = limiar_bonus[1]
            reajuste = limiar_reajuste[1]
        elif limiar_tempo[1] < tempo_servico <= limiar_tempo[2]:
            bonus = limiar_bonus[2]
            reajuste = limiar_reajuste[2]
        elif limiar_tempo[2] < tempo_servico <= limiar_tempo[3]:
            bonus = limiar_bonus[3]
            reajuste = limiar_reajuste[3]
        else:
            bonus = limiar_bonus[4]
            reajuste = limiar_reajuste[4]
        sal_reajustado = salario + (salario * reajuste / 100)
        novo_salario = sal_reajustado + bonus
    elif limiar_salario[0] < salario <= limiar_salario[1]:
        if tempo_servico < limiar_tempo[0]:
            bonus = limiar_bonus[0]
            reajuste = limiar_reajuste[0]
        elif limiar_tempo[0] < tempo_servico <= limiar_tempo[1]:
            bonus = limiar_bonus[1]
            reajuste = limiar_reajuste[1]
        elif limiar_tempo[1] < tempo_servico <= limiar_tempo[2]:
            bonus = limiar_bonus[2]
            reajuste = limiar_reajuste[2]
        elif limiar_tempo[2] < tempo_servico <= limiar_tempo[3]:
            bonus = limiar_bonus[3]
            reajuste = limiar_reajuste[3]
        else:
            bonus = limiar_bonus[4]
            reajuste = limiar_reajuste[4]
        sal_reajustado = salario + (salario * reajuste / 100)
        novo_salario = sal_reajustado + bonus
    elif limiar_salario[1] < salario <= limiar_salario[2]:
        if tempo_servico < limiar_tempo[0]:
            bonus = limiar_bonus[0]
            reajuste = limiar_reajuste[0]
        elif limiar_tempo[0] < tempo_servico <= limiar_tempo[1]:
            bonus = limiar_bonus[1]
            reajuste = limiar_reajuste[1]
        elif limiar_tempo[1] < tempo_servico <= limiar_tempo[2]:
            bonus = limiar_bonus[2]
            reajuste = limiar_reajuste[2]
        elif limiar_tempo[2] < tempo_servico <= limiar_tempo[3]:
            bonus = limiar_bonus[3]
            reajuste = limiar_reajuste[3]
        else:
            bonus = limiar_bonus[4]
            reajuste = limiar_reajuste[4]
        sal_reajustado = salario + (salario * reajuste / 100)
        novo_salario = sal_reajustado + bonus
    elif limiar_salario[2] < salario <= limiar_salario[3]:
        if tempo_servico < limiar_tempo[0]:
            bonus = limiar_bonus[0]
            reajuste = limiar_reajuste[0]
        elif limiar_tempo[0] < tempo_servico <= limiar_tempo[1]:
            bonus = limiar_bonus[1]
            reajuste = limiar_reajuste[1]
        elif limiar_tempo[1] < tempo_servico <= limiar_tempo[2]:
            bonus = limiar_bonus[2]
            reajuste = limiar_reajuste[2]
        elif limiar_tempo[2] < tempo_servico <= limiar_tempo[3]:
            bonus = limiar_bonus[3]
            reajuste = limiar_reajuste[3]
        else:
            bonus = limiar_bonus[4]
            reajuste = limiar_reajuste[4]
        sal_reajustado = salario + (salario * reajuste / 100)
        novo_salario = sal_reajustado + bonus
    else:
        if tempo_servico < limiar_tempo[0]:
            bonus = limiar_bonus[0]
            reajuste = limiar_reajuste[0]
        elif limiar_tempo[0] < tempo_servico <= limiar_tempo[1]:
            bonus = limiar_bonus[1]
            reajuste = limiar_reajuste[1]
        elif limiar_tempo[1] < tempo_servico <= limiar_tempo[2]:
            bonus = limiar_bonus[2]
            reajuste = limiar_reajuste[2]
        elif limiar_tempo[2] < tempo_servico <= limiar_tempo[3]:
            bonus = limiar_bonus[3]
            reajuste = limiar_reajuste[3]
        else:
            bonus = limiar_bonus[4]
            reajuste = limiar_reajuste[4]
        sal_reajustado = salario + (salario * reajuste / 100)
        novo_salario = sal_reajustado + bonus

    print(f'O seu salario era R$ {salario} e o seu tempo de serviço é de {tempo_servico} anos.\n'
          f'Dessa forma você obteve o reajuste de {reajuste}%  e bonus de R$ {bonus}.\n'
          f'Seu novo salário é de R$ {novo_salario}')
