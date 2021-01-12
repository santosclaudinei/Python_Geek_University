valores = []

for i in range(5):
    valor = int(input(f'Informe o {i+1}º valor: '))
    valores.append(valor)

print(f'O indice do maior numero é {valores.index(max(valores))}')
print(f'O indice do menor numero é {valores.index(min(valores))}')


