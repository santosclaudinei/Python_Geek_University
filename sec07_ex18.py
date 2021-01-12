from random import randint
lista = []
cont = 0
for i in range(11):
    lista.append(randint(1,100))

x = int(input('Informe um numero: '))
tamanho = len(lista)
for i in range(tamanho):
    if lista[i] % x == 0:
        print(lista[i])
        cont +=1
print(f'Dos numeros {lista} {cont} são multiplos de {x}. Confira acima! ')