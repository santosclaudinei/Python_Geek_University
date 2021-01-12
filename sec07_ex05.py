numeros = []

for i in range(10):
    n = int(input(f'Informe o {i+1}º numero: '))
    numeros.append(n)

for num in numeros:
    if num % 2 == 0:
        print(num)