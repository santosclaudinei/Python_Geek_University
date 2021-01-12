def somaNumeros(num1, num2):
    if num1 and num2 > 0:
        limite = num2
        inicio = num1 + 1
        soma = 0
        for i in range(inicio, limite):
            soma += i
        return soma
    else:
        print('Um ou os dois numéros que foram digitados são negativos:')



num1 = int(input('Informe o numero que deseja como ínicio limiar: '))
num2 = int(input('Informe o numero que deseja como fim limiar: '))
resultado = somaNumeros(num1, num2)
print(f'O resultado da soma entre os numeros de {num1} a {num2} foi {resultado}')