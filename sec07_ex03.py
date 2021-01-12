elementos = []
quadrado = []
for i in range(10):
    numero = float(input(f'Informe o {i+1}º numero: '))
    elementos.append(numero)
    quadrado.append(numero ** 2)


print('Os elementos da lista são: \n')
for numeros in elementos:
    print(numeros)

print('O quadrado dos elementos da lista são: \n')
for numeros in quadrado:
    print(numeros)
