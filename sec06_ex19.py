numero = int(input('Informe um numero entre 100 e 999: '))
if 100 <= numero <= 999:
    centena = numero // 100
    dezena = (numero - (centena * 100)) // 10
    unidade = (numero - (centena * 100)) - (dezena * 10)
    print(f'O numero digitado foi {numero} e este possui {centena} centenas, {dezena} dezenas e {unidade} unidades')