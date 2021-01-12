# Importa de coleções o default dict para capturar os numeros repetidos.
from collections import defaultdict

notas = []

for i in range(10):
    notas.append(float(input(f'Informe a {i + 1}ª nota: ')))

# Define quem cuidará dos indices dos elementos repetidos.
chaves = defaultdict(list)

""" 
Percorre a lista numbers e cada elemento que ele encontra cria um dicionario onde a chave
é o elemento e o valor vira uma lista com as ocorrencias do elemento dentro da lista
"""

for chave, valor in enumerate(notas):
    # Adciona o indice dos elemtentos numa lista
    chaves[valor].append(chave)


for valor in chaves:
    # se houver valores repetidos ele mostra o numero e suas posições na lista
    if len(chaves[valor]) > 1:
        print(f'O valor {valor} apareceu nas posições {chaves[valor]}')
