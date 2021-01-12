numeros = []

for i in range(8):
    num = int(input(f'Informe o {i+1}º numero: '))
    numeros.append(num)
x = int(input("Informe um valor para X: "))
y = int(input("Informe um valor para Y: "))

print(numeros[x])
print(numeros[y])