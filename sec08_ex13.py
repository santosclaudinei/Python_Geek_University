def operacao(num1, num2, simbolo):
    if simbolo in '+' or '-' or '/' or '*':
        if simbolo == '+':
            return num1 + num2
        elif simbolo == '-':
            if num1 > num2:
                return num1 - num2
            else:
                return num2 - num1
        elif simbolo == '/':
            if num1 > num2 and num2 > 0:
                return num1 / num2
            elif num2 > num1 and num1 > 0:
                return num2 / num1
        else:
            return num1 * num2
    else:
        print('Não é possível realizar a opeção. Símbolo Incorreto.')


num1 = int(input('Informe um numero: '))
num2 = int(input('Informe outro numero: '))
simbolo = input('Informe um símbolo:\n'
                '[+] - Somar\n'
                '[-] - Subtrair\n'
                '[/] - Dividir\n'
                '[*] - Multiplicar\n'
                'Por favor informe o símbolo agora: ')
resultado = operacao(num1, num2, simbolo)
print(f'O resultado de {num1}, o simbolo {simbolo} e {num2} foi {resultado}')