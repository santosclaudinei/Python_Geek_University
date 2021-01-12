notas = []

for i in range(1,4):
    nota = float(input(f"informe a {i}ª nota: "))
    notas.append(nota)

laboratorio, mensal, final = notas
media = (((laboratorio * 2) + (mensal * 3) + (final * 5))/ 10)

if (0 < media < 3.0):
    print("Aluno foi reprovado.")
elif (3.0 <= media < 5.0):
    print("Aluno está na recuperação.")
else:
    print("Aluno foi aprovado.")