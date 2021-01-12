baseMenor = int(input("Informe o valor desta base: "))
baseMaior = int(input("Informe o valor desta base: "))
altura = int(input("Informe a altura: "))

if baseMenor and baseMaior > 0:
    print(f'O resultado do calculo da area do trapezio é {((baseMenor + baseMaior) * altura) / 2}')

else:
    print("Imossivel realizar o calculo de area.")
