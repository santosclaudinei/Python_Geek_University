def calcularMedias(nota1, nota2, nota3):
    opcao = input('Informe [A] para calcular a média aritimética ou [P] para média ponderada: ')
    if opcao in 'aA' or opcao in 'pP':
        if opcao in 'aA':
            print('A média escolhida foi ARITIMÉTICA')
            media = (nota1 + nota2 + nota3) / 3
            return media
        else:
            print('A média escolhida foi PONDERADA')
            media = (nota1 * 5 + nota2 * 3 + nota3 * 2) / 10
            return media


notas = []
for i in range(3):
    nota = float(input(f'Informe a {i+1}ª nota: '))
    notas.append(nota)

nota1, nota2, nota3 = notas
media = calcularMedias(nota1, nota2, nota3)
print(f'A média resultante foi {media}')