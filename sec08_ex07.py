def conversaoTemperatura(temperatura):
    conversaoF = temperaturaC * (9 / 5) + 32
    return conversaoF


temperaturaC = float(input('Informe a temperatura em CELSIUS: '))
temperaturaF = conversaoTemperatura(temperaturaC)
print(f'A temperatura {temperaturaC}ºC convertira em Fahrenheit é {temperaturaF}ºF')
