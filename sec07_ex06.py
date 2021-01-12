elementos = []
maior = 0
menor = 0

for i in range(10):
    num = int(input(f'Informe o {i+1}º numero: '))
    elementos.append(num)

for numeros in elementos:
    if elementos[0]:
        if numeros > maior:
            maior = numeros
        elif numeros < maior:
            menor = numeros

print(maior)
print(menor)