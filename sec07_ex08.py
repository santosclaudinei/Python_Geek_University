valores = []

for i in range(10):
    num = int(input(f'Informe o {i+1}º numero: '))
    valores.append(num)

print(valores[::-1])