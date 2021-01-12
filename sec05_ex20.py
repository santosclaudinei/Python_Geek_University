a = int(input("Informe o lado A do triangulo: "))
b = int(input("Informe o lado B do triangulo: "))
c = int(input("Informe o lado C do triangulo: "))

if (a - b) < c and (a + b) > c:
    if (a - c) < b and (a + c) > b:
        if (b - c) < a and (b + c) > a:
            print(f'Os lados {a}, {b} e {c} podem formar um triangulo!')

if (a == b) and (a == c) and (b == c):
        print(f'Os valores digitados foram {a}, {b} e {c}.', end=' ')
        print(f'Formam um TRIÂNGULO EQUILATÉRO.')
elif (a != b) and (a != c) and (b != c):
    print(f'Os valores digitados foram {a}, {b} e {c}.', end=' ')
    print(f'Formam um TRIÂNGULO ESCALENO.')
else:
    print(f'Os valores digitados foram {a}, {b} e {c}.', end=' ')
    print(f'Formam um TRIÂNGULO ISÓCELES.')