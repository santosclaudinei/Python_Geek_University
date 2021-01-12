from random import randint
lista = []
impares = []

for i in range(10):
    lista.append(randint(0,50))

tamanho = len(lista)
for i in range(tamanho):
    if lista[i] % 2 == 1:
        impares.append(lista[i])

print(f'A lista de números é {lista}')
print(f'A partir da lista de números separamos os ímpares que são: {impares}')
