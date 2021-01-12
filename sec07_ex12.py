valores = []

for i in range(5):
    valor = int(input(f'Informe o {i+1}º valor: '))
    valores.append(valor)

print(f'Os valores informados foram: ')
for numeros in valores:
    print(f'{numeros}', end=' ')

print(f'\nO maior numero é {max(valores)}')
print(f'A media dos numeros é {sum(valores)/i}')