nota = float(input('Informe a nota final do aluno: '))
frequencia = int(input('Informe o numero de faltas que o aluno obteve: '))

if (nota and frequencia >= 0):
    if (9.0 <= nota <= 10.0):
        if (frequencia <= 20):
            print('Conceito "A".')
        else:
            print('Conceito "B".')
    elif (7.5 <= nota <= 8.9):
        if (frequencia <= 20):
            print('Conceito "B".')
        else:
            print('Conceito "C".')
    elif (5.0 <= nota <= 7.4):
        if (frequencia <= 20):
            print('Conceito "C".')
        else:
            print('Conceito "D".')
    elif (4.0 <= nota <= 4.9):
        if (frequencia <= 20):
            print('Conceito "D".')
        else:
            print('Conceito "E".')
    else:
        print('Conceito "E".')
else:
    print('Nota ou Frequencia Invalida.')