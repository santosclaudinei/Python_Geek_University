notas = []
cont = 1

while cont < 16:
    nota = float(input(f'Informe a {cont}ª nota: '))
    notas.append(nota)
    cont += 1

soma = sum(notas)
media = soma / cont

print(soma)
print(f'{media:.2f}')