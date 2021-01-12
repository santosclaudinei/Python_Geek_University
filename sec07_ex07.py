elementos = []
maior = 0

for i in range(10):
    num = int(input(f'Informe o {i+1}º numero: '))
    elementos.append(num)

for numeros in elementos:
    print(f'{numeros}', end=' ')

for numeros in elementos:
    if numeros > maior:
        maior = numeros

print(f'\nO maior é {maior}')
print(f'O indice do maior é {elementos.index(maior)}')