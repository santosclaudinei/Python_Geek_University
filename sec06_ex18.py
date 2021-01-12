cont = 0
maior, menor, ocorrencia = 0, 0, 0
quantidade = int(input('Informe a quantidade de numeros a serem lidos: '))

while cont < quantidade:
    numero = int(input(f'Informe o {cont} numero: '))
    if numero > maior:
        maior = numero
        if numero == maior:
            ocorrencia += 1
    else:
        menor = numero
    cont += 1

print(f'O maior numero entre os digitados é {maior} e alem da primeira vez que foi digitado '
      f'ocorreu mais {ocorrencia} vezes.')
