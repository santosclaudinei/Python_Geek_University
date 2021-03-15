valor_venda = float(input('Informe o valor da venda mensal: '))

if valor_venda >= 100000:
    comissao = 700 + (valor_venda * 0.16)
    print(f'A comissão recebida por vender {valor_venda} é {comissao}')
elif 80000 <= valor_venda < 100000:
    comissao = 650 + (valor_venda * 0.14)
    print(f'A comissão recebida por vender {valor_venda} é {comissao}')
elif 60000 <= valor_venda < 80000:
    comissao = 600 + (valor_venda * 0.14)
    print(f'A comissão recebida por vender {valor_venda} é {comissao}')
elif 40000 <= valor_venda < 60000:
    comissao = 550 + (valor_venda * 0.14)
    print(f'A comissão recebida por vender {valor_venda} é {comissao}')
elif 20000 <= valor_venda < 40000:
    comissao = 500 + (valor_venda * 0.14)
    print(f'A comissão recebida por vender {valor_venda} é {comissao}')
else:
    comissao = 400 + (valor_venda * 0.14)
    print(f'A comissão recebida por vender {valor_venda} é {comissao}')