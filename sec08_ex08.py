def calculaHipotenusa(catA, catB):
    hipotenusa = (catA ** 2 + catB ** 2) ** (1/2)
    return hipotenusa


a = float(input('Informe o valor para o cateto A: '))
b = float(input('Informe o valor para o cateto B: '))
calculo = calculaHipotenusa(a, b)
print(f'Os catetos foram {a} e {b} que resultaram na hipotenusa {calculo:.2f}')
