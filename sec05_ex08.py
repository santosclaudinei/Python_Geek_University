nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if (0 < nota2 < 10.0) and (0 < nota1 < 10.0):
    print(f"A media do aluno é {(nota1 + nota2) / 2}")
else:
    print("Uma ou mais notas estão invalidas.")