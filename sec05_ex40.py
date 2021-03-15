"""
Custo do consumidor é:
soma do custo da fabrica
comissão do distribuidor
impostos

Obs: comissao e impostos são calculadas em cima do custo da fabrica.

custo da fabrica até 12000 - distribuidor 5% - impostos isento
custo da fabrica até 12000 a 25000 - distribuidor 10% - impostos 15%
custo da fabrica acima de 25000 - distribuidor 15% - impostos 20%
"""
distribuidor = (5, 10, 15)
impostos = (0, 15, 20)

custo_fabrica = float(input('Informe o custo da fabrica para construir o veiculo: '))
while custo_fabrica > 0:
    if custo_fabrica <= 12000:
        perc_distribuidor = distribuidor[0] / 100
        perc_impostos = impostos[0] / 100
        custo_distribuidor = custo_fabrica + (custo_fabrica * perc_distribuidor)
        custo_impostos = (custo_fabrica * perc_impostos)
    elif 12000 < custo_fabrica <= 25000:
        perc_distribuidor = distribuidor[1] / 100
        perc_impostos = impostos[1] / 100
        custo_distribuidor = custo_fabrica + (custo_fabrica * perc_distribuidor)
        custo_impostos = (custo_fabrica * perc_impostos)
    else:
        perc_distribuidor = distribuidor[2] / 100
        perc_impostos = impostos[2] / 100
        custo_distribuidor = custo_fabrica + (custo_fabrica * perc_distribuidor)
        custo_impostos = (custo_fabrica * perc_impostos)
    custo_consumidor = custo_fabrica + custo_distribuidor + custo_impostos
    print(f'O custo da fabrica foi: R$ {custo_fabrica}\n'
          f'O custo do distribuidor foi R$ {custo_distribuidor}\n'
          f'O custo dos impostos foi: R$ {custo_impostos}\n'
          f'O valor final para o consumidor foi: R$ {custo_consumidor}')
    break
else:
    print('O custo da fabrica que foi informado é inválido.')