def arvore(largura):
    tamanho = largura + 1
    for i in range(1, tamanho):
        anterior = i - 1
        simbolo = '*'
        print(f'{(anterior + i) * simbolo} ')


largura = int(input('Informe a largura: '))
arvore(largura)