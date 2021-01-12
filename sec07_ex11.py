notas = []
cont = 1
soma_pos = 0
soma_neg = 0

while cont < 11:
    nota = float(input(f'Informe a {cont}ª nota: '))
    notas.append(nota)
    cont += 1

for numeros in notas:
    if numeros > 0:
        soma_pos = soma_pos + numeros
    elif numeros < 0:
        soma_neg += 1

print(soma_neg)
print(soma_pos)
