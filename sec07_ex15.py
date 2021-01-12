from collections import defaultdict

numbers = [3, 2, 4, 7, 3, 8, 2, 3, 8, 1, 3, 2, 4, 7, 3, 8, 2, 3, 8, 1]

repeat = defaultdict(list)

""" 
Percorre a lista numbers e cada elemento que ele encontra cria um dicionario onde a chave
é o elemento e o valor vira uma lista com as ocorrencias do elemento dentro da lista
"""

for key, value in enumerate(numbers):
    repeat[value].append(key)

for value in repeat:
    if len(repeat[value]) > 1:
        print(value, repeat[value])
