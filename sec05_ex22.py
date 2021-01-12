idade = int(input('Informe sua idade: '))
tempo_contribuicao = int(input('Informe o tempo de contribuição: '))

if idade >= 65 or tempo_contribuicao >= 30 or (idade >= 60 and tempo_contribuicao >= 25):
    print('Já pode se aposentar.')
else:
    print('Ainda não pode se aposentar.')