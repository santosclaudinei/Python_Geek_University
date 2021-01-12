from math import pi

def calculaVolume(altura, raio):
    volume = pi * altura * (raio ** 2)
    return volume


altura = float(input('Informe a altura do cilindro: '))
raio = float(input('Informe o raio do cilindro: '))
volume = calculaVolume(altura, raio)
print(f'A altura do triangulo é {altura} o {raio} e seu volume resultante é {volume:.2f}')
