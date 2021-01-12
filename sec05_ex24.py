valor = float(input('Informe o valor do produto: '))
estado = input('Escolha dentre os estados abaixo:\n'
               '[MG] - MINAS GERAIS\n'
               '[SP] - SÃO PAULO\n'
               '[RJ] - RIO DE JANEIRO\n'
               '[MS] - MATO GROSSO DO SUL\n'
               'Qual é a sua escolhar: ')

if estado in 'MGmg' or estado in 'SPsp' or estado in 'RJrj' or estado in 'MSms':
    if estado in 'MGmg':
        print(f'O valor final do produto é {valor + (valor * 0.07)}')
    elif estado in 'SPsp':
        print(f'O valor final do produto é {valor + (valor * 0.12)}')
    elif estado in 'RJrj':
        print(f'O valor final do produto é {valor + (valor * 0.15)}')
    else:
        print(f'O valor final do produto é {valor + (valor * 0.08)}')
else:
    print('Estado digitado é inválido.')