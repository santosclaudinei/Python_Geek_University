a = int(input('Informe um valor para A: '))
b = int(input('Informe um valor para B: '))
c = int(input('Informe um valor para C: '))

if a != 0:
    delta = b**2 - (4 * a * c)
    print(delta)
    if delta < 0:
        print('Não existe raiz.')
    elif delta > 0:
        x1l = (-b + (delta ** (1/2))) / 2 * a
        x2l = (-b - (delta ** (1/2))) / 2 * a
        print(x1l)
        print(x2l)
    else:
        xl = (-b + (delta ** (1/2))) / 2 * a
        print(xl)
else:
    print('Não é uma equação do segundo grau.')