distancia = float(input('Informe uma distancia percorrida em quilometros:  '))
qtdLitros = float(input('Informe a quantidade de gasolina consumida no percusso em litros: '))
consumo = distancia / qtdLitros

if 0 <= consumo:
    if consumo < 8:
        print(f'Carro faz {consumo:.2f} km com 1 litro. Venda o carro!')
    elif 8 <= consumo <= 12:
        print(f'Carro faz {consumo:.2f} km com 1 litro. Econômico!')
    else:
        print(f'Carro faz {consumo:.2f} km com 1 litro. Super Econômico!')
else:
    print(f'Carro faz {consumo:.2f} km com 1 litro. Não é possível avaliar!')