print("""
TABELA DE PREÇOS
CODIGO  -           ITEM                PREÇOS
[100]   -       CACHORRO QUENTE         R$ 1.20     
[101]   -       BAURU SIMPLES           R$ 1.30
[102]   -       BAURU COM OVO           R$ 1.50
[103]   -       HAMBURGUER              R$ 1.20
[104]   -       CHEESEBURGUER           R$ 1.70
[105]   -       SUCO                    R$ 2.20
[106]   -       REFRIGERANTE            R$ 1.00

Informe ao sistema o CODIGO do item e a QUANTIDADE de itens que deseja: 
""")
codigo = int(input('Informe o codigo do produto desejado [Eles estão de 100 a 106]: '))
quantidade = int(input('Informe a quantidade de itens desejado: '))

if (100 <= codigo <= 106) and (quantidade > 0):
    if (codigo == 100) or (codigo == 103):
        print(f'O valor do seu pedido é {quantidade * 1.20:.2f}')
    elif (codigo == 101):
        print(f'O valor do seu pedido é {quantidade * 1.30:.2f}')
    elif (codigo == 102):
        print(f'O valor do seu pedido é {quantidade * 1.50:.2f}')
    elif (codigo == 104):
        print(f'O valor do seu pedido é {quantidade * 1.70:.2f}')
    elif (codigo == 105):
        print(f'O valor do seu pedido é {quantidade * 2.20:.2f}')
    else:
        print(f'O valor do seu pedido é {quantidade * 1.00:.2f}')
else:
    print('Codigo ou Quantidade invalido(s)')
