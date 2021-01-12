sexo = input("Digite seu sexo: ")
altura = input("Digite sua altura: ")
if (sexo in "MmFF"):
    if (sexo  in "fF"):
        print(f"O seu IMC é {62.1 * float(altura) - 47}")
    else:
        print(f"O seu IMC é {72.7 * float(altura) - 58}")
else:
    print("Dados invalidos.")