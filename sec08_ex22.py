def imprimirSimbolo(num):
    simbolo = '!'
    tamanho = num + 1
    for i in range(tamanho):
        print(f'{i * simbolo}')

num = int(input('Informe o número de ocorrências de um símbolo: '))
imprimirSimbolo(num)
