# Sem Compreensão de Listas

# a = []
# b = []
# c = []
#
# for i in range(1, 5):
#     a.append(int(input(f'Informe o {i}º numero que será armazenado no vetor A: ')))
#     b.append(int(input(f'Informe o {i}º numero que será armazenado no vetor B: ')))
#
# tam = len(a)
# for numeros in range(tam):
#     c.append((a[numeros] - b[numeros]))
#
# print(c)

# Com Compreensão de Listas

a = []
b = []
c = []

for i in range(1, 5):
    a.append(int(input(f'Informe o {i}º numero que será armazenado no vetor A: ')))
    b.append(int(input(f'Informe o {i}º numero que será armazenado no vetor B: ')))

tam = len(a)
# Faz o FOR de acordo com a variável TAM e executa a subtração entre elementos da lista A e da lista B genrando a C
c = [a[numeros] - b[numeros] for numeros in range(tam)]

print(c)