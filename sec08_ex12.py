def decompor(centena, dezena, unidade):
    resultado = centena + dezena + unidade
    return resultado

numero = int(input('Informe um numero inteiro maior que zero: '))
if numero > 0:
    centena = numero // 100
    dezena = (numero - (centena * 100)) // 10
    unidade = (numero - (centena * 100)) - (dezena * 10)
    resultado = decompor(centena, dezena, unidade)
    print(f'O numero informado foi {numero} e quando decomposto teve o resultado de {resultado}')
else:
    print('Número Inválido.')