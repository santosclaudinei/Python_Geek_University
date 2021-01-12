lista = []
for i in range(1, 51):
    lista.append((i+5*i) % (i+1))

tamanho = len(lista)
for i in range(tamanho):
    print(lista[i])

