cont_pares, cont_ocorrencia,  = 0, 0
while True:
    numero = int(input('Informe um número: '))
    if numero == 1000:
        break
    elif numero > 0 and numero % 2 == 0:
        cont_pares += 1
        cont_ocorrencia += 1
    else:
        cont_ocorrencia += 1

print(f'O numero de dados digitados foi {cont_ocorrencia} e o numero de pares foi {cont_pares}')