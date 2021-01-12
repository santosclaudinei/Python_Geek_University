comprimento = float(input("Informe o comprimento do terreno: "))
largura = float(input("Informe a largura do terreno: "))
valorMetroTela = float(input("Informe o valor do metro da tela: "))

area = largura * comprimento
qtdTela = area * valorMetroTela

print(f"A área do terreno é de {area} m² e vai precisar invesir R$ {qtdTela:.2f} em tela para cercar")
