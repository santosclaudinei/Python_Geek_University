def data_de_nascimento(data):
    data, mes, ano = data.split('/')
    print(f'Você nasceu em {data} de {mes} de {ano}')
    """ A função recebe uma data num formato padrão e imprime no formato por extenso. """


data = input("Digite o da que você nasceu: ")
data_de_nascimento(data)
