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
# for numeros in a:
#     c.append(numeros)
# for num in b:
#     c.append(num)
#
# print(c)

# Com Compreensão de Listas

a = []
b = []
c = []

for i in range(1, 5):
    a.append(int(input(f'Informe o {i}º numero que será armazenado no vetor A: ')))
    b.append(int(input(f'Informe o {i}º numero que será armazenado no vetor B: ')))

# [c.append(numeros) for numeros in a]
# [c.append(num) for num in b]
tamA = len(a)
tamB = len(b)
for num, numeros in zip(a, b):
    if tamA <= 4:
        c.append(num)
    if tamB:
        c.append(numeros)

print(c)

