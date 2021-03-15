tuple_imc = (18.5, 25, 30, 35, 40)

peso = float(input('Informe o seu peso atual: '))
altura = float(input('Informe a sua altura atual: '))

if altura > 0 and peso > 0:
    imc = peso / (altura ** 2)
    if imc < tuple_imc[0]:
        print('Abaixo do peso')
    elif tuple_imc[0] < imc < tuple_imc[1]:
        print('Saudável')
    elif tuple_imc[1] < imc < tuple_imc[2]:
        print('Pesso em excesso')
    elif tuple_imc[2] < imc < tuple_imc[3]:
        print('Obesidade Grau I')
    elif tuple_imc[3] < imc < tuple_imc[4]:
        print('Obesidade Grau II(Severa)')
    else:
        print('Obesidade Grau III(mórbida)')
else:
    print('Os dados informados são inválidos.')
