preco_produto = float(input('Informe o preço antigo do produto: '))

if (preco_produto > 0):
    if (preco_produto <= 50):
        novo_preco = preco_produto + (preco_produto * 0.05)
    elif (50 < preco_produto <= 100):
        novo_preco = preco_produto + (preco_produto * 0.10)
    else:
        novo_preco = preco_produto + (preco_produto * 0.15)
else:
    print('Preço do produto está errado.')


if (novo_preco <= 80):
    print('Barato')
elif (80 < novo_preco <= 120):
    print('Normal')
elif (120 < novo_preco <= 200):
    print('Caro')
else:
    print('Muito Caro')
