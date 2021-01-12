lista = [1, -1, 2, 3, 4, -4, 6, 5, 7, -3]
tamanho = len(lista)

for i in range(tamanho):
    if lista[i] < 0:
        lista[i] = 0

print(lista)