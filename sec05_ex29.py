from random import randint

cont = 1
erro, acerto = 0, 0

while cont <= 5:
    a = randint(0, 101)
    b = randint(0, 101)
    print(a)
    print(b)
    soma = a + b
    resposta = int(input('Qual é a soma de A + B? '))
    if resposta == soma:
        print('Parabéns! Você acertou.')
        acerto += 1
    else:
        print('Oops! Você errou.')
        erro += 1
    cont += 1

print(f'Voce acertou {acerto} vezes e errou {erro} vezes')