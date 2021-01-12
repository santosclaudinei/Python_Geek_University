def imprimirSimbolo(largura):
    simbolo = '*'
    tamanho = 2 * largura + 1
    atual = 2
    for i in range(1, tamanho):
        if i <= largura:
            print(f'{i * simbolo}')
        else:
            print(f'{(i - atual) * simbolo}')
            atual += 2


largura = int(input('Informe o número de ocorrências de um símbolo: '))
imprimirSimbolo(largura)