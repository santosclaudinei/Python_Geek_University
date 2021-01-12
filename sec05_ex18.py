opcao = int(input(""" Escolha uma das opções abaixo: 
\t[1] -   SOMAR
\t[2] -   SUBTRAIR
\t[3] -   MULTIPLICAR
\t[4] -   DIVIDIR

Qual é a sua escolha: 
"""))

if 0 < opcao < 5:
    num1 = int(input("Informe um numero: "))
    num2 = int(input("Informe outro numero: "))
    if opcao == 1:
        print(f'O resultado da soma foi {num1 + num2}')
    elif opcao == 2:
        print(f'O resultado da subtração foi {num1 - num2}')
    elif opcao == 3:
        print(f'O resultado da multiplicação foi {num1 * num2}')
    else:
        print(f'O resultado da divisão foi {num1 / num2}')
else:
    print('Opção invalida.')