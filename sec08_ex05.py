def volume_esfera(raio):
    volume = (4 / 3) * 3.14 * (raio ** 3)
    return volume


r = int(input("Informe o raio a ser calculado: "))
print(f"O volume da esfera é {volume_esfera(r):.2f}")