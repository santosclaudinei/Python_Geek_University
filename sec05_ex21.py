escolha = int(input(f"Dentre as oções abaixo selecione a desejada:\n "
                    f"[1] - Soma entre dois numero\n"
                    f" [2] - Diferença entre dois numeros\n"
                    f" [3] - Produto entre dois numeros\n"
                    f" [4] - Divisão entre dois numeros\n"
                    f"Digite a opção que deseja: "))

if 1 <= escolha <= 4:
    num1 = int(input('Informe um numero: '))
    num2 = int(input('Informe outro numero: '))
    if escolha == 1:
        print(f'A soma de {num1} e {num2} é {num1+num2}')
    elif escolha == 2:
        if num1 > num2:
            print(f'A diferença entre {num1} e {num2} é {num1 - num2}')
        else:
            print(f'A diferença entre {num1} e {num2} é {num2 - num1}')
    elif  escolha == 3:
        print(f'O produto entre {num1} e {num2} é {num1 * num2}')
    else:
        if num1 > num2 and num2 != 0:
            print(f'A divisão entre {num1} e {num2} é {num1 / num2}')
        elif num2 > num1 and num1 != 0:
            print(f'A divisão entre {num2} e {num1} é {num2 / num1}')
        else:
            print('Não é possivel realizar a divisão de um numero qualquer por zero.')
else:
    print('A opção digitada é inválida!')