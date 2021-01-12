contribuicaoAmigo1 = float(input("Você vai colaborar com quanto: "))
contribuicaoAmigo2 = float(input("Você vai colaborar com quanto: "))
contribuicaoAmigo3 = float(input("Você vai colaborar com quanto: "))

titulo = contribuicaoAmigo1 + contribuicaoAmigo2 + contribuicaoAmigo3
valorPremio = float(input("Informe o valor do premio: "))

porcAmigo1 = ((contribuicaoAmigo1 * 100) / titulo) / 100
porcAmigo2 = ((contribuicaoAmigo2 * 100) / titulo) / 100
porcAmigo3 = ((contribuicaoAmigo3 * 100) / titulo) / 100
print(porcAmigo1)

premioAmigo1 = int(valorPremio * porcAmigo1)
premioAmigo2 = int(valorPremio * porcAmigo2)
premioAmigo3 = int(valorPremio * porcAmigo3)

print(f"A contribuição do amigo 1 foi R$ {contribuicaoAmigo1}, do amigo 2 foi de R$ {contribuicaoAmigo2} e"
      f"do amigo 3 foi de R$ {contribuicaoAmigo3}.\n"
      f"O valor do titulo foi de R$ {titulo} e esta concorrendo ao premio de R$ {valorPremio}."
      f"Caso o bilhete seja premiado os premios serão:\n"
      f"- Amigo 1 embolsará o valor de R$ {premioAmigo1} que equivale a {porcAmigo1:.2f}% do valor investido.\n"
      f"- Amigo 1 embolsará o valor de R$ {premioAmigo2} que equivale a {porcAmigo2:.2f}% do valor investido.\n"
      f"- Amigo 1 embolsará o valor de R$ {premioAmigo3} que equivale a {porcAmigo3:.2f}% do valor investido.")


