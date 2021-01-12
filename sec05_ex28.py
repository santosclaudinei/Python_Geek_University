x = int(input('Informe o valor de X: '))
y = int(input('Informe o valor de Y: '))
z = int(input('Informe o valor de Z: '))

opcao = int(input(f'Informe a opção de calculo que deseja:\n'
            '[1] - Géometrica\n'
            '[2] - Ponderada\n'
            '[3] - Harmônica\n'
            '[4] - Aritimética\n'
            'Qual deseja realizar: '))

if 1 <= opcao <= 4:
    if opcao == 1:
        media = (x * y * z) ** (1/3)
        print(media)
    elif opcao == 2:
        media = (x + 2 * y + 3 * z) / 6
        print(media)
    elif opcao == 3:
        media = 1 / (1 / x + 1 / y + 1 / z)
        print(media)
    else:
        media = x + y + z / 3
        print(media)
else:
    print('Opção inválida.')