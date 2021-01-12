def custoBeneficio(distancia, consumo):
    autonomia = distancia/consumo
    return autonomia


distancia = float(input('Informe a distância percorrida: '))
consumo = float(input('Informe o consumo de combustivel na viagem: '))
resultado = custoBeneficio(distancia, consumo)
if resultado > 0:
    if resultado < 8:
        print(f'Venda o carro! Pois o consumo foi {resultado} e está alto ')
    elif 8 <= resultado < 12:
        print(f'Econômico! Pois o consumo foi {resultado} e está dentro da média ')
    else:
        print(f'Super Econômico! Pois o consumo foi {resultado} e está abaixo da média ')
else:
    print('O consumo ou a distância informados estão errados. favor verificar e tentar novamente. ')