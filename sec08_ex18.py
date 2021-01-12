def calculaExponenciacao(x, z):
    return x ** z


x = int(input('Informe um numero: '))
z = int(input('Informe outro numero: '))
resultado = calculaExponenciacao(x, z)
print(f'O resultado de {x} elevado a {z} potência foi {resultado}')